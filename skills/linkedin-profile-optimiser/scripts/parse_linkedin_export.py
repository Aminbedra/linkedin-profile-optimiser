#!/usr/bin/env python3
"""
Parse a LinkedIn data export into a readable summary for auditing.

Usage:
    python parse_linkedin_export.py <path-to-zip-or-folder>

The script is intentionally defensive: LinkedIn changes file names and
columns over time, so it matches files by fuzzy name and reads whatever
columns are present rather than assuming a fixed schema.
"""

import csv
import io
import sys
import zipfile
from pathlib import Path


# Map a canonical section to the substrings that may appear in the file name.
FILE_HINTS = {
    "Profile": ["profile"],
    "Positions": ["position"],
    "Education": ["education"],
    "Skills": ["skill"],
    "Recommendations": ["recommendation"],
}

# For each section, the columns worth surfacing if they exist (case-insensitive).
COLUMNS_OF_INTEREST = {
    "Profile": ["First Name", "Last Name", "Headline", "Summary", "Industry",
                "Geo Location", "Location"],
    "Positions": ["Company Name", "Title", "Started On", "Finished On",
                  "Description"],
    "Education": ["School Name", "Degree Name", "Start Date", "End Date"],
    "Skills": ["Name"],
    "Recommendations": ["First Name", "Last Name", "Text", "Status"],
}


def load_csv_files(source: Path):
    """Return a dict of {filename: list_of_row_dicts} from a zip or folder."""
    files = {}
    if source.is_file() and source.suffix.lower() == ".zip":
        with zipfile.ZipFile(source) as zf:
            for name in zf.namelist():
                if name.lower().endswith(".csv"):
                    raw = zf.read(name).decode("utf-8", errors="replace")
                    files[Path(name).name] = list(csv.DictReader(io.StringIO(raw)))
    elif source.is_dir():
        for path in source.rglob("*.csv"):
            with open(path, encoding="utf-8", errors="replace") as fh:
                files[path.name] = list(csv.DictReader(fh))
    else:
        raise SystemExit(f"Provide a .zip file or a folder. Got: {source}")
    return files


def match_section(filename: str):
    low = filename.lower()
    for section, hints in FILE_HINTS.items():
        if any(h in low for h in hints):
            return section
    return None


def pick(row: dict, wanted: list):
    """Return wanted columns from a row, matching case-insensitively."""
    lower_map = {k.lower(): v for k, v in row.items()}
    out = {}
    for col in wanted:
        val = lower_map.get(col.lower())
        if val:
            out[col] = val
    return out


def summarise(files: dict):
    print("=" * 60)
    print("LINKEDIN EXPORT SUMMARY")
    print("=" * 60)

    matched = {}
    for fname, rows in files.items():
        section = match_section(fname)
        if section:
            matched.setdefault(section, []).extend(rows)

    if not matched:
        print("No recognised LinkedIn CSV files found.")
        print("Files present:", ", ".join(files) or "none")
        return

    # Profile
    if "Profile" in matched and matched["Profile"]:
        p = pick(matched["Profile"][0], COLUMNS_OF_INTEREST["Profile"])
        print("\n## Profile")
        for k, v in p.items():
            label = "About" if k == "Summary" else k
            print(f"- {label}: {v}")

    # Positions
    if "Positions" in matched:
        print(f"\n## Experience ({len(matched['Positions'])} roles)")
        for row in matched["Positions"]:
            r = pick(row, COLUMNS_OF_INTEREST["Positions"])
            title = r.get("Title", "Unknown role")
            company = r.get("Company Name", "Unknown company")
            start = r.get("Started On", "")
            end = r.get("Finished On", "Present")
            print(f"\n- {title} at {company} ({start} to {end})")
            desc = r.get("Description")
            if desc:
                print(f"  {desc.strip()[:400]}")

    # Education
    if "Education" in matched:
        print(f"\n## Education ({len(matched['Education'])} entries)")
        for row in matched["Education"]:
            r = pick(row, COLUMNS_OF_INTEREST["Education"])
            print(f"- {r.get('School Name', 'Unknown')}: "
                  f"{r.get('Degree Name', '')}".strip())

    # Skills
    if "Skills" in matched:
        names = [pick(r, ["Name"]).get("Name", "") for r in matched["Skills"]]
        names = [n for n in names if n]
        print(f"\n## Skills ({len(names)})")
        print(", ".join(names) if names else "None listed")

    # Recommendations
    if "Recommendations" in matched:
        recs = matched["Recommendations"]
        received = [r for r in recs
                    if pick(r, ["Status"]).get("Status", "").lower() != "sent"]
        print(f"\n## Recommendations ({len(recs)} total)")

    print("\n" + "=" * 60)
    print("Feed this summary into the Stage 1 audit. Note that some live "
          "profile elements (banner, photo quality) are not in the export.")


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    files = load_csv_files(Path(sys.argv[1]).expanduser())
    summarise(files)


if __name__ == "__main__":
    main()

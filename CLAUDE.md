# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

A Claude Code skill (`linkedin-profile-optimiser.skill`) that audits, scores, and rewrites LinkedIn profiles. The `.skill` file is a ZIP archive — unzip it to edit contents, re-zip to package it back up.

## Edit/pack workflow

```bash
# Unpack
unzip linkedin-profile-optimiser.skill -d linkedin-profile-optimiser/

# Edit files inside linkedin-profile-optimiser/

# Repack (from the parent directory)
zip -r linkedin-profile-optimiser.skill linkedin-profile-optimiser/
```

## Running the parser script

The Python script requires no external dependencies (stdlib only):

```bash
# From a LinkedIn data export zip
python linkedin-profile-optimiser/scripts/parse_linkedin_export.py /path/to/linkedin-export.zip

# Or from an unzipped folder
python linkedin-profile-optimiser/scripts/parse_linkedin_export.py /path/to/linkedin-export-folder/
```

## Skill architecture

The entry point is `SKILL.md`, which defines trigger conditions and a gated 6-stage workflow. Stages run as a guided conversation — not all at once.

**Stage flow:**
- **Stage 0: Intake** — Establish source material (pasted text, URL, or `.zip` export) and user's goal (target role, inbound leads, etc.)
- **Stage 1: Audit** — Score against `references/audit-rubric.md` (8 dimensions, 100-point scale: Headline 20pts, About 20pts, Experience 20pts, Keywords 15pts, Skills 10pts, Featured 5pts, Recommendations 5pts, Basics 5pts)
- **Stage 2: Report** — Use `assets/report-template.md` skeleton; order actions by impact, not section order
- **Stage 3: Rewrites** — Use formulas in `references/section-rewrites.md`; use `[bracketed placeholders]` for unknown facts, never fabricate
- **Stage 4: Keywords** — Use `references/keyword-discoverability.md`; produce a placement table (keyword → field)
- **Stage 5: Brand voice** — Use `references/brand-voice.md`; optional growth layer
- **Stage 6: CV/Word doc** — Hand off to the `docx` skill; do not hand-roll Word XML

**Reference files are loaded on-demand per stage**, not all upfront. Each stage explicitly names which file to read.

## Key constraints

- Never fabricate achievements, metrics, employers, or dates — use `[marked placeholders]` instead.
- When the user provides only a LinkedIn URL and it cannot be fetched, ask them to paste text or upload a screenshot.
- If the user asks for just one section (e.g. "rewrite my headline"), jump to that stage but offer surrounding stages afterwards.
- The `parse_linkedin_export.py` script matches CSV files by fuzzy filename hints because LinkedIn changes its export schema over time — do not assume fixed column names.

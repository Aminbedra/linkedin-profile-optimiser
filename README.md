# LinkedIn Profile Optimiser

A Claude skill that audits, scores, and rewrites your LinkedIn profile section by section, then optionally exports an ATS-friendly CV in Word format.

## What it does

- Scores your profile across 8 dimensions on a 100-point scale
- Produces a prioritised action list ordered by impact, not by section
- Rewrites your headline, About, and experience bullets using proven formulas
- Maps recruiter-search keywords to the right profile fields
- Defines a personal brand voice and content pillars
- Optionally generates an ATS-compliant Word CV

## Install

### Option A: Claude Code (recommended, two lines)

Inside a Claude Code session, run:

```
/plugin marketplace add Aminbedra/linkedin-profile-optimiser
/plugin install linkedin-profile-optimiser@amin-skills
```

Start a new session and the skill loads automatically.

### Option B: Claude.ai or Claude Desktop

Download `linkedin-profile-optimiser.skill` from this repo, then in Settings open Capabilities, upload the file, and toggle it on.

### Option C: Manual (Claude Code, no marketplace)

```
git clone https://github.com/Aminbedra/linkedin-profile-optimiser
cp -r linkedin-profile-optimiser/skills/linkedin-profile-optimiser ~/.claude/skills/
```

Confirm `~/.claude/skills/linkedin-profile-optimiser/SKILL.md` sits directly inside that folder, not one level deeper.

## How to use

Once installed, talk to Claude naturally. The skill triggers whenever you mention your LinkedIn profile, headline, About section, experience bullets, keywords, or recruiter discoverability. You do not need to invoke it by name.

Examples that trigger it:

```
"Can you improve my LinkedIn profile?"
"Rewrite my headline, I'm targeting senior product roles."
"Audit my LinkedIn and tell me what to fix first."
"Help me get found by more recruiters."
"Turn my LinkedIn into a CV."
```

### Providing your profile

You can give Claude your profile in three ways: paste the text from LinkedIn, share your public profile URL, or download your data from LinkedIn (Settings, Data Privacy, Get a copy of your data) and share the `.zip`.

### The workflow

The skill runs as a guided conversation, one stage at a time. After each stage Claude summarises what was produced and asks whether to continue. You can skip ahead: if you only want one thing, say so and it jumps straight there, then offers the rest afterwards.

| Stage | What happens |
| --- | --- |
| 0, Intake | Establish your source material and goal |
| 1, Audit | Score the profile across the 8 weighted dimensions |
| 2, Report | Prioritised action list, highest-leverage fixes first |
| 3, Rewrites | Ready-to-paste rewrites for headline, About, and experience |
| 4, Keywords | Keyword placement table mapping target terms to the right fields |
| 5, Brand voice | Positioning angle and content pillars |
| 6, CV export | ATS-compliant Word document built from your optimised profile |

## Parsing a LinkedIn data export

You can pre-process an export before sharing it:

```
python skills/linkedin-profile-optimiser/scripts/parse_linkedin_export.py /path/to/linkedin-export.zip
```

No external dependencies, pure Python standard library.

## Constraints

- Never fabricates achievements, metrics, employers, or dates. Unknown facts become clearly marked placeholders.
- LinkedIn's ranking algorithm is opaque, so improvements follow best practices, not guarantees.
- Your data export is your personal data, used only to help you and not retained.

## About the author

Amin Bedra is an ex-LinkedIn marketer who believes the career ladder is a game — the more people you help, the higher you can climb.

- Website: [aminbedra.com](https://www.aminbedra.com)
- Skill page: [linkedin-profile-optimiser.aminbedra.com](https://linkedin-profile-optimiser.aminbedra.com)
- Email: [hello@aminbedra.com](mailto:hello@aminbedra.com)

## License

MIT

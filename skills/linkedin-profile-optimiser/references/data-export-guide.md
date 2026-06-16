# LinkedIn Data Export Guide

LinkedIn lets a user download their own data as a `.zip` of CSV files. This is the richest, most reliable source for an audit because it is structured data straight from the source, not a screenshot you have to read by eye.

## How the user requests it

Tell the user, if they have not already exported it:
1. On LinkedIn, go to Settings & Privacy.
2. Open Data Privacy, then "Get a copy of your data".
3. Select the larger archive that includes profile, connections, and activity.
4. LinkedIn emails a download link, sometimes within minutes, sometimes up to 24 hours.

Set the expectation that it may not be instant, so they are not left waiting on a blank screen.

## What is inside (file names vary over time)

The archive typically contains CSV files such as:
- `Profile.csv` — name, headline, summary/About, location, industry.
- `Positions.csv` — roles, companies, titles, dates, descriptions.
- `Education.csv` — schools, degrees, dates.
- `Skills.csv` — listed skills.
- `Email Addresses.csv`, `Connections.csv`, and others.

File names and columns change periodically, so parse defensively and do not assume a fixed schema.

## How to use it

1. Run `scripts/parse_linkedin_export.py` against the unzipped folder or the `.zip` directly. It prints a readable summary of the key files.
2. Feed that summary into the Stage 1 audit exactly as you would pasted profile text.
3. The export will not contain everything visible on the live profile (for example, banner image quality), so mark those dimensions "Not visible, confirm".

## Privacy

This is the user's own personal data. Use it solely to help them with their profile in this session. Do not repurpose it or treat it as a contact list for any other task.

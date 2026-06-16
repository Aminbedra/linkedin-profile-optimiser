---
name: linkedin-profile-optimiser
description: Audits, scores, and rewrites a person's LinkedIn profile, then optionally produces an ATS-friendly CV in Word. Use this whenever the user shares LinkedIn profile text, a LinkedIn URL, or a LinkedIn data export and asks to improve, audit, optimise, rewrite, or "fix" any part of it; whenever they mention their headline, About/summary, experience bullets, skills, personal branding, recruiter discoverability, profile keywords, or being found by recruiters; or whenever they want their LinkedIn turned into a CV or resume. Trigger this even if the user does not say the word "skill" and even if they only mention one section, because most single-section requests benefit from the full audit context.
---

# LinkedIn Profile Optimiser

This skill turns a LinkedIn profile into a serviced, recruiter-ready asset. Treat the work like a full car service with separate bays: a diagnostic scorecard, a work order, the actual part replacements, an engine tune for discoverability, and an optional formal certificate (the CV). The user decides how many bays to visit.

## Operating principle: gated, not firehose

Do NOT dump every output at once. Run the workflow as a guided conversation. After each stage, summarise what was produced and ask whether to proceed to the next stage. This protects first-time users from overwhelm and lets power users skip ahead. If the user clearly asks for one specific thing ("just rewrite my headline"), jump straight to that stage, but still offer the surrounding stages afterwards.

Adapt to the user's field. This skill is general purpose, so never assume an industry. Infer it from their content, or ask one short question if it is genuinely unclear.

## Stage 0: Intake (always first)

Establish two things before doing anything else:

1. **The source material.** Accept any of: pasted profile text, a LinkedIn profile URL, screenshots, or a LinkedIn data export (a `.zip` the user downloaded from LinkedIn). If they paste only fragments, work with what is given and note the gaps.
2. **Their goal.** Ask what they are optimising *for*: a specific target role or title, inbound recruiter interest, client attraction, or general polish. The target is the yardstick for every later judgement, so do not skip it.

If the user provides a LinkedIn data export, read `references/data-export-guide.md` and use `scripts/parse_linkedin_export.py` to summarise it before auditing.

If the user provides only a URL and you cannot fetch it, ask them to paste the profile text or upload a screenshot. Do not invent profile content.

## Stage 1: Audit and scorecard

Read `references/audit-rubric.md` and score the profile against every dimension. Produce a scorecard showing each dimension, its mark, and a one-line reason. Lead with the overall score out of 100 so the user gets the headline number first.

Keep the tone constructive. The scorecard is a diagnostic, not a verdict on the person.

## Stage 2: Report and prioritised action list

Use `assets/report-template.md` as the skeleton. The action list must be ordered by impact, not by profile section order, so the user fixes the highest-leverage items first. Apply an 80/20 lens: surface the few changes that drive most of the improvement.

Offer before-and-after snippets for the top items here as a preview, then ask whether to proceed to full rewrites.

## Stage 3: Section rewrites (ready to paste)

Read `references/section-rewrites.md`. Rewrite the requested sections (headline, About, experience, skills) using the formulas and examples there. Output each rewrite as clean, ready-to-paste text in its own clearly labelled block. Where a section depends on facts you do not have (metrics, dates, employers), insert a clearly marked placeholder like `[add a number here, e.g. 30% pipeline growth]` rather than fabricating detail.

## Stage 4: Keyword and recruiter discoverability

Read `references/keyword-discoverability.md`. Identify the keywords the user's target role demands, check where they currently appear, and recommend specific placements across headline, About, skills, and job titles. Explain briefly why placement matters for LinkedIn and recruiter search.

## Stage 5: Personal brand voice and content angle

Read `references/brand-voice.md`. Help the user define a positioning angle and two or three content pillars they can post about. Keep this optional and clearly framed as the growth layer beyond a clean profile.

## Stage 7: Generate Claude Chrome MCP prompt (optional, on request)

When the user wants to continue working on their LinkedIn presence in a fresh Claude session via the Chrome MCP extension, generate a single self-contained prompt block they can paste directly.

The prompt must be entirely standalone — it cannot rely on any prior conversation. Structure it as follows:

**1. Identity and context block**
Who the user is, their target positioning, and their primary goal (e.g. inbound leads, target role, consulting pipeline). One short paragraph.

**2. Optimised profile snapshot**
Paste in the final versions of: headline, About, and the rewritten experience bullets (with any real metrics filled in). Use the exact text produced in Stages 3–4, not a summary.

**3. Keyword and brand voice summary**
A short paragraph naming the priority keywords and their placement status, plus the one-line positioning statement and three content pillars from Stage 5.

**4. Remaining placeholders**
List any `[bracketed placeholders]` still outstanding so the next Claude session knows exactly what facts are still needed.

**5. Opening instruction for the next session**
A clear directive telling Claude what to help with next. Offer the user three options to choose from before generating:
- **Content mode** — "Help me write LinkedIn posts based on my brand voice pillars."
- **Completion mode** — "Help me fill in the remaining metric placeholders by asking targeted questions."
- **Outreach mode** — "Help me draft personalised connection requests and InMail messages to ICP prospects."

Generate the full prompt block inside a single fenced code block so the user can copy it in one click. Label it clearly: `PASTE THIS INTO CLAUDE CHROME MCP`.

## Stage 6: ATS-friendly CV in Word (optional, on request)

When the user wants a CV or resume document, hand off to the `docx` skill in this environment to produce the actual Word file. Do not hand-roll Word XML.

ATS rules that must shape the document:
- Single-column layout, standard section headings (Summary, Experience, Skills, Education).
- No tables, text boxes, headers/footers, images, or icons for content an ATS must read.
- Standard fonts, simple bullet points, role titles and dates as plain text.
- Mirror the target-role keywords identified in Stage 4.

Gather the content first (pull from the profile and rewrites already produced), confirm the target role, then build the `.docx` and present it for download.

## Reference files

- `references/audit-rubric.md` — scoring dimensions, weights, and what good looks like.
- `references/section-rewrites.md` — headline, About, and experience rewrite formulas with examples.
- `references/keyword-discoverability.md` — how LinkedIn and recruiter search work and where to place keywords.
- `references/brand-voice.md` — positioning angles and content pillars.
- `references/data-export-guide.md` — what is inside a LinkedIn data export and how to read it.
- `assets/report-template.md` — the audit report skeleton.
- `scripts/parse_linkedin_export.py` — parses an exported LinkedIn `.zip`/CSV set into a readable summary.

## Boundaries

- Never fabricate achievements, metrics, employers, or dates. Use marked placeholders instead.
- Never claim a profile change guarantees a job or a specific search ranking. LinkedIn's algorithm is opaque and these are informed best practices, not certainties.
- A LinkedIn data export is the user's own personal data. Use it only to help them, and do not retain or repurpose it.

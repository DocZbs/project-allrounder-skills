---
name: building-project-presentations
description: Use when creating or revising a real PPTX for a vertical or horizontal project proposal defense, kickoff, progress review, technical review, acceptance, or closeout presentation.
---

# Building Project Presentations

## Overview

Turn verified project requirements and evidence into a decision-oriented presentation. Deliver a real `.pptx`, rendered and inspected—not an outline, slide script, or unverified success story.

**REQUIRED SUB-SKILL:** Use the installed **`presentations`** skill for PowerPoint construction, rendering, overflow tests, and final delivery. Follow its current toolchain and workspace rules rather than duplicating or replacing them here.

## Define the Communication Job

Before planning slides, complete [deck-brief.md](assets/deck-brief.md):

1. Identify the scene, intended audience, decision authority, duration, language, venue, and output path.
2. State: `By the end, [audience] should [understand/approve/decide] because [central evidence-backed takeaway].`
3. Freeze the controlling task book, contract, call, baseline, indicators, deliverables, reports, results, finance evidence, template, and confidentiality rules.
4. Separate verified evidence, provisional analysis, missing evidence, and forbidden claims.
5. Read [deck-router.md](references/deck-router.md) and choose exactly one primary scene.
6. Read [evidence-and-story.md](references/evidence-and-story.md), analyze an authorized/open same-scene reference deck when available, and create [slide-evidence-matrix.md](assets/slide-evidence-matrix.md).

If the audience, decision, controlling requirements, or evidence is unknown, produce a gap report and provisional storyboard. Do not fabricate a successful outcome or label the work final.

## Preflight Response Contract

Before beginning file creation, explicitly state:

1. Whether the deck can be final or must remain provisional, with unsupported claims listed.
2. The missing evidence or decisions required from the user.
3. The selected scene, audience decision, communication job, and narrative arc.
4. The authorized/open same-scene reference-deck plan, or the recorded reason none is available.
5. The delivery commitment: create the actual `.pptx` with `presentations`, add speaker notes/timing/questions, render every slide, inspect each render at full size, fix blocking defects, and report QA status.

## Build an Evidence-Led Story

- Give every slide one narrative job and one primary claim.
- Use takeaway titles that a presenter could say aloud; avoid topic-only titles and repeated slogans.
- Make each slide answer a question raised by the prior slide or create the next question.
- Show what evidence means for the audience's decision, not an inventory of activities.
- Match every indicator, deliverable, financial statement, and acceptance claim to a source and evidence path.
- Keep planning notes, time scaffolds, source-selection comments, and internal prompts out of visible slide copy; put useful talk track in speaker notes.
- Preserve the user's template and brand when supplied. Do not copy visual assets or layouts from unauthorized reference decks.

## Produce the Actual PPTX

1. Invoke `presentations` and choose its correct visual route: user template/reference, explicit custom styling, or its default layout system.
2. Create the deck in the user-requested location or the presentation skill's standard output path.
3. Use verified project visuals—charts, diagrams, architecture, maps, photographs, test evidence, or tables—only when they advance the current claim.
4. Keep main evidence legible at presentation distance; split dense evidence instead of shrinking it.
5. Add speaker notes with the claim, evidence interpretation, transition, caveat, and likely question for each substantive slide.
6. Allocate slide-level time and keep total planned speaking time within the requested duration, leaving room for transitions and questions.
7. Build an expert-question bank from weak evidence, boundaries, methods, variance, risk, budget, IP/data, operation, and acceptance criteria.
8. Export a real `.pptx`. Never substitute Markdown, PDF, images, or an outline unless the user explicitly requests that additional format.

## Corrective Quality Loop

Read [visual-quality-gates.md](references/visual-quality-gates.md) and run at least one defect-finding revision loop:

1. Run the presentation skill's programmatic overflow/bounds checks.
2. Render every final slide.
3. Inspect every slide individually at full size. A contact sheet is for deck flow only and cannot replace full-size inspection.
4. Record high, medium, and low defects with slide numbers.
5. Fix every high-severity defect and every feasible medium-severity defect.
6. Regenerate the PPTX, rerun checks, and re-inspect changed slides plus the complete deck flow.
7. Reconcile PPTX claims and numbers against the task book, contract, reports, source data, evidence files, and finance records.

The deck is not ready when it contains unsupported claims, missing central evidence, unintended overlap, overflow, clipping, unreadable content, broken connectors, distorted/cropped figures, unresolved placeholders, inconsistent numbers, or absent required notes.

## Output Contract

Deliver:

1. Final `.pptx` path.
2. Scene, audience, decision, and duration.
3. Source/reference-deck provenance summary.
4. Evidence and content coverage result.
5. Render/overflow/overlap/crop/legibility QA result and any disclosed limitation.
6. Speaker-notes and timing status.
7. Expert-question bank location or inclusion status.
8. Blockers that prevent a formal-final or pass/acceptance claim.

## Common Mistakes

- Giving a polished outline instead of creating the file.
- Using an agenda as the narrative.
- Reporting work performed instead of evidence and decision impact.
- Declaring an indicator passed from a result value without checking target, method, period, exclusions, and evidence.
- Reusing proposal-defense storytelling for acceptance.
- Treating a contact sheet or successful export as visual QA.
- Shrinking text or evidence to make an overcrowded slide fit.
- Ending on a generic “Thank you” instead of resolving the opening decision.

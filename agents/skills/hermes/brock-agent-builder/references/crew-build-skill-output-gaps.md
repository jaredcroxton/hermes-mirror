# Crew Build Skill Output Gaps — 26 June 2026

## Gap 1: No animation injection

Build skills (slide-deck-builder, cinematic-build, scroll-journey) reference animation skills in their design review gates but never generate animation code in the HTML output.

Symptom: beautiful static pages with no motion. The gate confirms animation quality standards are met, but no `<script>` block with GSAP or Motion code exists in the output.

Fix: add an animation injection step to each build skill's Workflow, after HTML generation and before the design review gate. Generate a `<script>` block with the appropriate animation engine for the output.

## Gap 2: PDF output poor quality

HTML-to-browser-PDF conversion strips premium styling. Background colours, fonts, and layout degrade because no `@media print` stylesheet exists.

Fix: add `## Print and PDF` section to every build skill's output template. Include `@media print` with page breaks at slide/section boundaries, `print-color-adjust: exact`, font fallbacks, and margin control.

## Gap 3: Navigation invisible on dark backgrounds

Slide-deck-builder produces navigation arrows that are invisible against dark backgrounds due to contrast issues.

Fix: ensure navigation elements have sufficient contrast against the chosen colour scheme. Add explicit colour rules for navigation in the output template.

## Gap 4: Delivery format not asked

Build skills don't ask whether the business wants HTML, PDF, PowerPoint, or Word output.

Fix: add Question 8 to Discovery section: "How should this be delivered? PowerPoint (.pptx), Word (.docx), HTML, PDF, or Both."

## Gap 5: Fresh install directory not found

`.claude/crew-state/` doesn't exist on fresh install. Step 0 assumes it does. Skills should create the directory if absent, or scaffold it.

## Date

Discovered 26 June 2026 during LearnOS slide deck review and Mac Mini fresh-install test.

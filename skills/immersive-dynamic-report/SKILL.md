---
name: immersive-dynamic-report
description: Create or upgrade a versioned AI intelligence or world-trend report into an immersive, visually distinctive HTML reading experience. Use when an Agent team must publish a rich standalone report, a 20-card research deck, an evidence-led story page, or a safe dynamic HTML reader with motion, charts, source traceability, and non-investment-advice boundaries.
---

# Immersive Dynamic Report

Turn a completed information run into a standalone reading experience, not a
dashboard screenshot or a stack of RSS summaries. Build the report from the
fixed 20-card evidence deck in [references/report-grammar.md](references/report-grammar.md).

## Non-negotiable contract

- Publish an immutable document version. Open a report by document_id plus
  version, never by a moving latest pointer.
- Keep every fact, metric, chart value, and relationship traceable to evidence,
  source URL, timestamp, and data cutoff.
- Mark every card as observed, inferred, or gap. A gap is a designed research
  task, not blank space.
- Do not infer revenue, valuation, Capex, company financials, or geographic
  facts from RSS headlines. Show a named proxy or a research-gap card instead.
- Keep research/simulation and non-investment-advice disclosures visible.

## Design direction

Choose a visual identity tied to the report’s subject:

- Use a cinematic research-room surface for AI intelligence: midnight blue,
  mineral mint, signal blue, warm coral, and restrained gold.
- Use a world-atlas or editorial-observatory surface for world trends: deep
  navy, copper, fog white, and scenario-colored accents.
- Make the hero a thesis: title, cutoff, and the strongest evidenced finding.
  Do not substitute generic gradient KPI tiles for the actual research claim.
- Treat typography as hierarchy: an editorial display face for the thesis, a
  readable body face for reasoning, and monospace only for evidence metadata.
- Pick one signature interaction. The default is an evidence orbit around a
  full-screen report canvas plus a 20-card chapter rail. Do not sprinkle
  unrelated effects across every component.

## Publishing workflow

1. **Certify inputs.** Checker/Data Engineer verifies source count, domain
   diversity, timestamps, units, citations, and missing-data conditions.
2. **Build the narrative.** Lead and Editor write one thesis, a concise
   evidence-led lede, and card order. Keep counterevidence visibly present.
3. **Compile every card.** Use the fixed IDs from the report grammar. Render
   available data as a suitable chart; render unavailable data as a gap with
   coverage, missing field, next Agent, and next action.
4. **Produce the document.** Generate static, sanitized HTML with semantic
   sections, text alternatives, ID anchors, data-card-id, citations, and a
   strict CSP. Use CSS/SVG/HTML data views; do not add untrusted scripts.
5. **Place it in the reader.** The reader must fetch the exact version, show
   version/cutoff/source metrics, and place the document in a strict sandboxed
   canvas. The chapter rail may target the report’s stable anchors.
6. **Animate with restraint.** Use a page-load sequence, a subtle ambient
   orbit, progress, or a one-shot card entrance. Respect reduced motion; never
   animate numbers into invented values.
7. **Audit before release.** Verify small/mobile layouts, keyboard focus,
   reader error state, citations, card IDs, and the non-investment disclaimer.

## Roles

- **Scout / Web Collector:** deliver timestamped source records and source
  metadata for the evidence and source-mix cards.
- **Checker / Data Engineer:** certify comparable metrics, chart input, units,
  freshness, and citation coverage.
- **Lead / Data Analyst / Market Mapper:** provide thesis, clustering,
  relationship paths, scenarios, and calibrated risks.
- **Editor / Red Team:** shape the reading sequence and preserve uncertainty,
  alternative explanations, and open questions.
- **Publisher / Presenter:** render the standalone HTML, reading shell, card
  anchors, responsive behavior, and accessible motion.

## Safety and accessibility

- Keep the report iframe sandboxed without scripts or same-origin privileges.
- Do not place an entire report, raw HTML, access token, or API key in a URL.
- Use a live loading state and a precise recovery message on failed versions.
- Keep contrast high, controls keyboard-operable, and focus visible.
- Put accessible text alternatives beside charts; motion must be optional.


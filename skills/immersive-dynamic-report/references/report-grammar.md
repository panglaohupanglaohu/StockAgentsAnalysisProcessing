# Report grammar

Use this compact grammar when compiling the standalone reader. The page keeps
the 20 cards in a stable order so citations, deep links, tests, and report
history remain meaningful.

| ID | Card | Visual treatment | Required truth label |
| --- | --- | --- | --- |
| cover | Thesis / cutoff | Cinematic thesis hero | observed |
| editor-note | Why it matters | Editorial note + three claims | observed/inferred |
| contents | Method | Evidence contract and scope | observed |
| signal-landscape | Topic mix | Ranked bars | observed |
| evidence-pulse | Volume + freshness | Timeline / pulse | observed |
| two-state-gap | Signal comparison | Dumbbell or gap | observed/gap |
| confidence-bubble | Signal versus confidence | Bubble / ranked proxy | observed/inferred |
| evidence-donut | Source quality mix | Donut + legend | observed |
| top-three | Leading themes | Comparable cards | observed |
| source-ranking | Source coverage | Horizontal rank | observed |
| dual-track | Two explanatory paths | Dual track | inferred/gap |
| second-tier | Long tail | Secondary cards | observed |
| focal-signal | Strongest signal | Focus card | observed |
| flow-map | Event to effect | Flow map | inferred |
| pareto | Concentration | Pareto | observed |
| evidence-hub | Relationships | Hub/spoke | observed/inferred |
| uncertainty | Counterevidence | Uncertainty field | observed/gap |
| adoption-cost-proxy | Mechanism | Proxy curve / gap | inferred/gap |
| risk-quadrant | Risk posture | Four-quadrant | inferred |
| closing | Monitor list | Six takeaways | observed/inferred/gap |

## Visual reference synthesis

Use these as technique references, never as copied assets or data:

- Anthropic frontend-design: make a subject-specific design plan, give
  typography and motion a real purpose, and take one restrained visual risk.
- html-ppt-skill: use tokenized layouts, keyboard-first navigation, a clear
  deck sequence, and one coherent animation system.
- AI Animation card-theater: a sidebar narrative and card sequence can make
  the report feel like an explorable story, but charts remain evidence-led.
- ppt-master global AI capital example: use high-contrast data journalism,
  clear labels, comparable charts, and explicit research gaps.

## Reader implementation shape

~~~text
new-tab report-viewer.html?document_id=…&version=…
  → fetch immutable JSON snapshot
  → render title / cutoff / real evidence metrics
  → iframe exact render endpoint with a strict sandbox
  → chapter rail links to stable card anchors
~~~

Do not loosen the sandbox to measure iframe height or inject runtime code. Use
a viewport-sized report canvas and native report scrolling instead.

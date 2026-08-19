# Qwen3.8-27B on a 24GB local demo machine

Use this note when Jared wants to demo a local model in a workshop or stakeholder setting on a 24GB machine.

## Decision rule

For a live demo, optimise for reliability and perceived responsiveness over maximum benchmark quality. The audience notices freezing, first-token delay, and rambling before they notice small quant-quality differences.

## Recommended setup

- Model: `Qwen3.8-27B`
- Preferred quant: `Q4_K_XL` if available, otherwise `Q4_K_M`
- Approx size target: 13 to 16GB
- Context cap: 8K for live workshop demos
- Hardware assumption: 24GB total memory or VRAM hard ceiling, not 24GB free on a bigger machine

## Avoid by default

- `Q5_K_M` around 17.8GB for live demos unless tested hard on the exact machine. It may fit, but leaves too little headroom once macOS, browser, slides, screen sharing, and KV cache are active.
- `Q6_K`, `Q8_0`, and BF16 on 24GB demo machines.
- Very low quants such as Q2 or Q3 for a paid room. They may be faster, but the quality loss can show up as wrong facts, repetition, or tangents.
- Running the advertised maximum context. Long context increases memory pressure and slows responses.

## Demo operating checklist

1. Quit other model runtimes and heavy apps before loading the model.
2. Cap context at 8K unless a longer-context use case is central to the demo.
3. Pre-warm the model before the audience arrives with one throwaway prompt.
4. Use three short scripted prompts tested the night before.
5. Keep the demo story simple: local AI running privately on a normal machine.

## Positioning note

Do not sell the demo as "the biggest model." Sell the practical outcome: private local AI, no cloud dependency, usable speed, and enough intelligence to make the concept real.
# DGX Spark Local Model Stack

Use when choosing local models for DGX Spark, ASUS Ascent GX10, or similar 128GB NVIDIA GB10 local AI appliances.

## Core judgement

The best model to run day to day is not the biggest model the machine can technically load.

For AgentOS and Hermes, optimise for:

- stability
- speed
- memory headroom
- tool use
- concurrent agents
- sandbox overhead
- vector stores and logs
- reliable response quality

## Recommended model lanes

### Daily AgentOS model

Use a 70B to 72B class instruct model as the default local brain.

Examples:

- Qwen3 72B Instruct, quantised
- Llama 3.3 70B, quantised

Use for:

- most Hermes agents
- general reasoning
- research
- planning
- document work
- operational tasks
- agent loops

Why: this tier fits comfortably in 128GB and leaves room for the rest of the system.

### Premium local reasoning model

Use a 120B class model for high-value reasoning.

Example family:

- NVIDIA Nemotron 120B class, quantised

Use for:

- Brock-level strategy
- complex business reasoning
- product architecture
- governance documents
- long-form synthesis
- high-value planning

Why: 120B at 4-bit or 5-bit is realistic on 128GB while still leaving some operational headroom.

### Fast utility model

Use a 30B class or smaller model for fast work.

Examples:

- Qwen3-Coder 30B-A3B
- Nemotron 30B class
- 8B or 14B utility model

Use for:

- routing
- extraction
- classification
- summarisation
- quick coding
- background jobs
- cheap repeated loops

### Stretch/showcase model

NVIDIA says DGX Spark supports models up to 200B parameters.

Treat 200B as showcase or specialist mode, not the default. At this size, memory is tight after KV cache, context, tools, agents, sandboxes, and background services.

## Rough memory guide

Approximate model weight memory only, before real runtime overhead and KV cache.

70B:

- 8-bit: about 84GB with 20% headroom
- 6-bit: about 63GB with 20% headroom
- 5-bit: about 52GB with 20% headroom
- 4-bit: about 42GB with 20% headroom

120B:

- 6-bit: about 108GB with 20% headroom
- 5-bit: about 90GB with 20% headroom
- 4-bit: about 72GB with 20% headroom

200B:

- 4-bit: about 120GB with 20% headroom
- 3-bit: about 90GB with 20% headroom

## Qwen3-Coder 480B-A35B caution

Large MoE models can look attractive because only some parameters are active at once. Do not assume active parameters equal local memory needs.

Unless the runtime has a clever expert-loading strategy, local memory still needs to deal with model weights. A 480B model is not a clean 128GB target except with very aggressive quantisation and likely compromises.

For coding on DGX Spark, prefer:

- Qwen3-Coder 30B-A3B for fast coding and tool work
- 70B class coding/instruct model for stronger local quality
- Claude/Codex from the MacBook for the hardest production builds

## Recommended starting stack

1. Qwen3 72B Instruct, 4-bit or 5-bit: default local brain.
2. NVIDIA Nemotron 120B class, 4-bit: premium reasoning mode.
3. Qwen3-Coder 30B-A3B: fast coding/tool model.
4. Small 8B or 14B model: routing, extraction, classification, background jobs.

## Rule of thumb

Use 70B for daily operations, 120B for premium reasoning, and 200B only as stretch/test mode.

AgentOS needs a working system, not a benchmark flex.

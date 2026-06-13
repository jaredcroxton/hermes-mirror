---
name: llm-inference-operations
description: Use when discovering, downloading, quantizing, serving, benchmarking, or operating LLMs locally or on GPU infrastructure with Hugging Face, llama.cpp, vLLM, W&B, or lm-eval.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [llm, inference, huggingface, llama-cpp, vllm, evaluation, wandb, gpu]
    related_skills: [private-ai-gpu-prototyping]
---

# LLM Inference Operations

## Overview

This umbrella covers the operational path from model discovery to serving and evaluation: Hugging Face Hub discovery/download, local GGUF/llama.cpp inference, high-throughput vLLM serving, experiment tracking with W&B, and benchmark runs with lm-evaluation-harness.

## When to Use

- Find or download models/datasets from Hugging Face.
- Run local GGUF inference with llama.cpp or llama-cpp-python.
- Serve OpenAI-compatible endpoints with vLLM.
- Benchmark models with lm-evaluation-harness.
- Track training/evaluation experiments or artifacts in W&B.
- Choose infrastructure for a private AI/GPU prototype.

## Workflow map

### Model discovery and download
- Use Hugging Face Hub search/list commands first.
- Capture license, file size, quantization, and hardware requirements before downloading.

### Local inference: llama.cpp / GGUF
- Match quantization to available RAM/VRAM.
- Prefer small smoke tests before long generations.
- For server mode, verify the OpenAI-compatible endpoint with a real request.

### GPU serving: vLLM
- Use vLLM when throughput, batching, tensor parallelism, or production-style OpenAI API serving matters.
- Validate CUDA/GPU visibility, model compatibility, context length, and memory headroom before launch.

### Evaluation and tracking
- Use lm-evaluation-harness for benchmark suites and repeatable eval commands.
- Use W&B for runs, sweeps, artifacts, dashboards, and reproducible experiment metadata.

## Infrastructure judgement

For private-cloud or client-site prototypes, start with the cheapest reversible test: local Mac/Ollama if sufficient, low-cost EC2 GPU trial if not, and strict spend controls. Surface quota blockers early; new AWS accounts often need GPU quota requests.

For DGX Spark, ASUS Ascent GX10, or similar 128GB NVIDIA GB10 appliances, use `references/dgx-spark-local-model-stack.md` before recommending a local model stack. Default guidance: 70B to 72B quantised models for daily AgentOS operations, 120B class models for premium local reasoning, and 200B class models only as stretch/showcase mode because operational headroom matters more than benchmark size.

## Verification Checklist

- [ ] Model/license/hardware assumptions are documented.
- [ ] A smoke inference or health request succeeded.
- [ ] Benchmark/tracking commands saved outputs in a reproducible location.
- [ ] Cloud resources have explicit stop/cleanup instructions.

# Mastering Agentic AI Certification: Prerequisite Resource Pack

This pack is designed for builders joining the Mastering Agentic AI certification. 

## How to Use This Pack

Learners do not need to complete every optional resource before class. The recommended path is to finish the core resources for each week in order, then use the optional resources for depth, capstone prep, or specialization.

| Week | Theme | Best outcome before joining live sessions |
|---|---|---|
| Week 1 | Gen AI Building Blocks | Learners can explain tokens, embeddings, attention, prompting, model selection, structured outputs, and multimodal APIs. |
| Week 2 | RAG and Context Engineering | Learners can reason about retrieval, chunking, embeddings, reranking, hybrid search, GraphRAG, and n8n workflow automation. |
| Week 3 | The Agentic Leap | Learners understand agent loops, ReAct, MCP, A2A, tool use, memory, LangGraph, n8n, and multi-agent design. |
| Week 4 | Evals, Observability and Monitoring | Learners can define eval types, instrument traces, use LLM-as-judge carefully, and compare LangSmith, Langfuse, and Phoenix. |
| Week 5 | Finetuning and Local Models | Learners know when to finetune, how LoRA/QLoRA work, how to prepare data, and how to run local models. |
| Week 6 | Security and Production Readiness | Learners can identify core LLM risks, prompt injection, guardrails, privacy issues, red-teaming workflows, and go-live checks. |
| Week 7 | AI Career Launchpad and AI-Native | Learners can map AI roles, salary signals, portfolio strategy, LinkedIn/GitHub positioning, and AI-native productivity workflows. |

## Week 1: Gen AI Building Blocks

Understand the engine before you drive it.

### Learning Objective

Build a working mental model of modern LLMs: how tokens become embeddings, how attention works, why context windows matter, how prompting and structured outputs shape behavior, and how to choose across closed-source, open-source, hosted, and local model ecosystems.

### Core Prerequisite Resources

| Order | Resource | Type | Time | Why it belongs | Covers |
|---|---|---:|---|---|---|
| 1 | [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g), Andrej Karpathy | YouTube video | 1 hr | One of the clearest practitioner introductions to LLM training, inference, and product implications. | Tokens, pretraining, inference, RLHF, tool use, scaling, model behavior. |
| 2 | [Attention Is All You Need](https://arxiv.org/abs/1706.03762), Vaswani et al. | Paper | 2-3 hrs | The canonical Transformer paper from Google researchers and the foundation for modern LLM architecture. | Self-attention, multi-head attention, positional encoding, encoder-decoder architecture. |
| 3 | [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/), Jay Alammar | Blog | 45-60 min | The best visual companion to the original Transformer paper. | Q/K/V intuition, attention heads, encoder-decoder flow. |
| 4 | [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI), Andrej Karpathy | YouTube video | 3.5 hrs, segmentable | Comprehensive end-to-end explanation of the LLM build stack and modern post-training patterns. | Tokenization, pretraining data, GPT internals, SFT, RLHF, tool use, hallucinations. |
| 5 | [Hugging Face LLM Course, Chapters 1-3](https://huggingface.co/learn/llm-course/chapter1/1) | Course/docs | 2-3 hrs | Hugging Face is the default open-source model and tooling hub for builders. | Transformers, tokenizers, pipelines, model APIs, fine-tuning basics. |
| 6 | [ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/courses/chatgpt-prompt-eng), DeepLearning.AI and OpenAI | Short course | 1.5 hrs | Compact, builder-focused course from Andrew Ng and OpenAI’s Isa Fulford. | Zero-shot, few-shot, chain-of-thought patterns, role prompting, API use. |
| 7 | [Anthropic Prompt Engineering Overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) and [Interactive Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | Docs and GitHub tutorial | 1-2 hrs | Official Anthropic guidance for production-quality Claude prompting. | Prompt structure, XML tags, role design, failure modes, prompt chaining. |
| 8 | [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs), [Function Calling](https://developers.openai.com/api/docs/guides/function-calling), and [Developer Quickstart](https://developers.openai.com/api/docs/quickstart) | Official docs | 1-1.5 hrs | Official reference for reliable outputs, tool calls, and API mechanics. | JSON schemas, function calling, model parameters, structured output contracts. |
| 9 | [OpenAI Images and Vision](https://developers.openai.com/api/docs/guides/images-vision), [OpenAI Audio](https://developers.openai.com/api/docs/guides/audio), and [Gemini Prompt Design Strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies) | Official docs | 1 hr | Gives learners a practical multimodal overview from two major AI platforms. | Text, image, audio, vision prompting, multimodal input/output patterns. |
| 10 | [OpenRouter API Reference](https://openrouter.ai/docs/api/reference/overview), [Hugging Face Open LLM Leaderboard](https://huggingface.co/open-llm-leaderboard), and [Chatbot Arena](https://openlm.ai/chatbot-arena/) | Docs and benchmarks | 45-60 min | Covers the model-selection landscape: hosted routing, open model evaluation, and arena-style human preference rankings. | Closed vs. open models, routing, model comparison, benchmarks, trade-offs. |
| 11 | [A Visual Guide to Attention Variants in Modern LLMs](https://magazine.sebastianraschka.com/p/visual-attention-variants), Sebastian Raschka | Technical blog | 45-60 min | Connects the original Transformer with modern attention variants used in current open-weight models. | MHA, GQA, MLA, sliding-window attention, modern model architecture. |

### Optional Deeper Dives

| Resource | Type | Time | Best for |
|---|---|---:|---|
| [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html), Andrej Karpathy | Video series | 8-10 hrs | Learners who want to build neural nets and GPT-like models from scratch. |
| [Build a Large Language Model From Scratch](https://github.com/rasbt/LLMs-from-scratch), Sebastian Raschka | Book and code | Self-paced | Hands-on learners who want implementation depth. |
| [Stanford CS324: Large Language Models](https://stanford-cs324.github.io/winter2022/) | Course notes | Reference | Learners who want a rigorous academic framing of LLMs and their impacts. |

## Week 2: Grounding AI with RAG and Context Engineering

Stop hallucinations. Anchor AI in your data.

### Learning Objective

Understand why prompting alone is insufficient for enterprise systems, how retrieval and context engineering work, and how to design a RAG pipeline with chunking, embeddings, hybrid search, reranking, evaluation, GraphRAG, and workflow automation.

### Core Prerequisite Resources

| Order | Resource | Type | Time | Why it belongs | Covers |
|---|---|---:|---|---|---|
| 1 | [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401), Lewis et al. | Paper | 1.5-2 hrs | The original RAG paper from Meta AI Research. | Parametric vs. non-parametric memory, dense retrieval, RAG-Sequence, RAG-Token. |
| 2 | [An Intuitive Introduction to Text Embeddings](https://stackoverflow.blog/2023/11/09/an-intuitive-introduction-to-text-embeddings/), Stack Overflow | Blog | 30 min | Clear practitioner explanation before learners touch vector databases. | Embeddings, latent space, semantic similarity, vector search intuition. |
| 3 | [Dense Passage Retrieval for Open-Domain Question Answering](https://arxiv.org/abs/2004.04906), Karpukhin et al. | Paper | 1-1.5 hrs | Foundational dense retrieval paper from Facebook AI Research. | Dense vs. sparse retrieval, dual encoders, retrieval recall, FAISS. |
| 4 | [Retrieval Augmented Generation](https://learn.deeplearning.ai/courses/retrieval-augmented-generation), DeepLearning.AI and Weaviate | Short course | 3 hrs | Strong end-to-end RAG walkthrough with practical retrieval and evaluation coverage. | Vector DBs, BM25, semantic search, hybrid search, chunking, query parsing, evaluation. |
| 5 | [Context Engineering: LLM Memory and Retrieval for AI Agents](https://weaviate.io/blog/context-engineering), Weaviate | Engineering blog | 30 min | Clear explanation of context engineering beyond prompt wording. | Context assembly, memory types, retrieval context, agent context design. |
| 6 | [Chunking Strategies for RAG](https://weaviate.io/blog/chunking-strategies-for-rag), Weaviate | Engineering blog | 30 min | Chunking is a common failure point in RAG systems. | Fixed, recursive, sentence, semantic chunking, overlap trade-offs. |
| 7 | [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard), Hugging Face | Benchmark | 20-30 min | Practical reference for comparing embedding models across tasks. | Embedding model selection, retrieval benchmarks, model trade-offs. |
| 8 | [LlamaIndex RAG Docs](https://developers.llamaindex.ai/python/framework/understanding/rag/) and [Advanced RAG Cheat Sheet](https://www.llamaindex.ai/blog/a-cheat-sheet-and-some-recipes-for-building-advanced-rag-803a9d94c41b) | Official docs and blog | 1 hr | LlamaIndex is a widely used RAG-native framework. | Indexes, nodes, query engines, reranking, HyDE, multi-step retrieval, advanced patterns. |
| 9 | [OpenAI File Search RAG Cookbook](https://developers.openai.com/cookbook/examples/file_search_responses) | Official tutorial | 45 min | Shows a managed RAG path using OpenAI’s hosted vector store/file search workflow. | PDF ingestion, file search, source citations, managed retrieval. |
| 10 | [Microsoft GraphRAG Project](https://www.microsoft.com/en-us/research/project/graphrag/) and [GraphRAG Docs](https://microsoft.github.io/graphrag/) | Research project and docs | 45-60 min | Authoritative starting point for graph-enhanced retrieval. | GraphRAG, entity extraction, community summaries, structured knowledge retrieval. |
| 11 | [n8n AI Agent Node Docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/) and [Build an AI Workflow in n8n](https://docs.n8n.io/advanced-ai/intro-tutorial/) | Official docs | 1 hr | Directly supports the curriculum’s automation component. | Workflow automation, AI Agent node, tools, LangChain nodes, practical integrations. |

### Optional Deeper Dives

| Resource | Type | Time | Best for |
|---|---|---:|---|
| [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/), Lilian Weng | Technical blog | 1-1.5 hrs | Bridging Week 2 RAG/memory into Week 3 agents. |
| [Retrieval-Augmented Generation](https://www.pinecone.io/learn/retrieval-augmented-generation/), Pinecone Learn | Guide | 45 min | Learners who want a visual RAG pipeline reference. |
| [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), Anthropic | Engineering blog | 20 min | Learners who want current production agent context patterns. |

## Week 3: The Agentic Leap

When AI stops answering and starts acting.

### Learning Objective

Understand what makes a system agentic, how agent loops and planning patterns work, how tools and memory are managed, how MCP and A2A fit into the ecosystem, and how to orchestrate reliable agent workflows using LangGraph, OpenAI Agents SDK, and n8n.

### Core Prerequisite Resources

| Order | Resource | Type | Time | Why it belongs | Covers |
|---|---|---:|---|---|---|
| 1 | [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents), Anthropic | Engineering blog | 30 min | Clear production-focused distinction between workflows and agents. | Agent design, augmented LLMs, routing, orchestrator-workers, evaluator-optimizer, when not to use agents. |
| 2 | [ReAct: Synergizing Reasoning and Acting](https://arxiv.org/abs/2210.03629), Yao et al. | Paper | 25-45 min | Foundational agent loop paper behind many modern agent frameworks. | Thought-action-observation loop, reasoning traces, tool use, interpretability. |
| 3 | [Model Context Protocol Introduction](https://modelcontextprotocol.io/docs/getting-started/intro) and [MCP Specification](https://modelcontextprotocol.io/specification/2025-11-25) | Official docs | 30 min | Essential protocol for connecting agents to tools, resources, and external systems. | MCP hosts, clients, servers, resources, prompts, tools, JSON-RPC transport. |
| 4 | [Agent2Agent Protocol](https://github.com/a2aproject/A2A) | Official GitHub/spec | 20 min | Emerging protocol for agent-to-agent collaboration and capability discovery. | Agent cards, communication modes, discovery, task handoff, interoperability. |
| 5 | [OpenAI Function Calling](https://developers.openai.com/api/docs/guides/function-calling) and [Anthropic Tool Use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) | Official docs | 45 min | These are the raw mechanics behind tool-using agents. | Tool schemas, function calls, tool results, structured tool interfaces. |
| 6 | [Writing Effective Tools for AI Agents](https://www.anthropic.com/engineering/writing-tools-for-agents), Anthropic | Engineering blog | 20 min | Practical guide to agent-computer interface design. | Tool naming, descriptions, response design, token efficiency, tool evaluation. |
| 7 | [LangGraph Docs](https://langchain-ai.github.io/langgraph/) | Official docs | 40-60 min | LangGraph is a leading framework for stateful, reliable agent workflows. | State, nodes, edges, memory, durable execution, human-in-the-loop, subgraphs. |
| 8 | [AI Agents in LangGraph](https://www.deeplearning.ai/courses/ai-agents-in-langgraph), DeepLearning.AI and LangChain | Short course | 1.5 hrs | Hands-on agent construction from the LangChain team. | Agent loop, LangGraph basics, persistence, streaming, human-in-loop. |
| 9 | [OpenAI Agents SDK Guide](https://developers.openai.com/api/docs/guides/agents) | Official docs | 30 min | OpenAI’s first-party SDK for agent orchestration and handoffs. | Agents, orchestration, handoffs, guardrails, tracing, hosted tools, MCP. |
| 10 | [How We Built Our Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system), Anthropic | Engineering case study | 20 min | Production case study for delegation, parallelism, and multi-agent reliability. | Multi-agent delegation, orchestrator-worker pattern, context management, latency/cost trade-offs. |
| 11 | [n8n AI Agent Node Docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/) | Official docs | 30-45 min | Gives non-framework automation builders a practical way to wire agents into workflows. | Tool nodes, workflow orchestration, AI agents, automation triggers and actions. |

### Optional Deeper Dives

| Resource | Type | Time | Best for |
|---|---|---:|---|
| [LangGraph Academy: Intro to LangGraph](https://academy.langchain.com/courses/intro-to-langgraph) | Course | 4-6 hrs | Learners who want deeper LangGraph fluency. |
| [Google Agent Development Kit Tutorials](https://google.github.io/adk-docs/tutorials/) | Official docs | 1 hr | Learners comparing Google ADK with LangGraph and OpenAI Agents SDK. |
| [Hugging Face Agents Course: LangGraph Unit](https://huggingface.co/learn/agents-course/unit2/langgraph/introduction) | Course | 2 hrs | Learners who want additional visual reinforcement. |
| [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), Anthropic | Engineering blog | 20 min | Builders moving from toy agents to production agents. |

## Week 4: AI Evals, Observability and Monitoring

Shipping is just the beginning.

### Learning Objective

Move from "I hope this works" to "I can measure whether it works." Learners should understand offline and online evals, LLM-as-judge methodology, latency/cost/task-completion metrics, trace-based debugging, alerting, and regression testing.

### Core Prerequisite Resources

| Order | Resource | Type | Time | Why it belongs | Covers |
|---|---|---:|---|---|---|
| 1 | [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), Anthropic | Engineering blog | 35 min | One of the strongest practical eval references for agent systems. | Eval taxonomy, grader types, pass@k, agent eval categories, production monitoring. |
| 2 | [LLM-as-a-Judge: Complete Guide](https://hamel.dev/blog/posts/llm-judge/), Hamel Husain | Technical blog | 30 min | Practitioner-oriented guide focused on real eval implementation pitfalls. | Judge design, rubrics, human calibration, bias, when not to use judges. |
| 3 | [LLM Evals FAQ](https://hamel.dev/blog/posts/evals-faq/), Hamel Husain | Reference blog | 25 min | Useful field guide for common eval implementation questions. | Example counts, error analysis, monitoring vs. evals, Goodhart’s Law, eval-driven development. |
| 4 | [LangSmith Docs](https://docs.smith.langchain.com/) | Official docs | 45 min | Main managed observability and eval platform for LangChain/LangGraph workflows. | Tracing, datasets, evaluators, prompt management, monitoring. |
| 5 | [LangSmith Agent Trajectory Evaluations](https://docs.langchain.com/langsmith/trajectory-evals) | Official tutorial | 20 min | Addresses the unique challenge of evaluating an agent’s sequence of actions. | Tool-call trajectory matching, LLM-as-judge for trajectories, strict/subset/superset modes. |
| 6 | [Langfuse Observability Overview](https://langfuse.com/docs/observability/overview) and [Get Started](https://langfuse.com/docs/observability/get-started) | Official docs | 30-45 min | Strong open-source and self-hostable observability option. | Traces, sessions, observations, cost tracking, prompt management, evals, OpenTelemetry. |
| 7 | [Arize Phoenix Tracing Quickstart](https://docs.arize.com/phoenix/tracing/quickstart) and [Phoenix Evals Quickstart](https://docs.arize.com/phoenix/quickstart/evals) | Official docs | 45 min | Strong open-source tooling for traces, evals, and agent debugging. | OpenInference, tracing, RAG evals, hallucination evals, tool-call evals. |
| 8 | [Automated Testing for LLMOps](https://www.deeplearning.ai/courses/automated-testing-llmops), DeepLearning.AI and CircleCI | Short course | 52 min | Directly connects evals to CI/CD and release gates. | Rules-based evals, model-graded evals, CI pipelines, regression testing. |
| 9 | [OpenTelemetry GenAI Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) | Official spec | 20 min | Vendor-neutral standard behind many LLM observability integrations. | Spans, metrics, events, semantic conventions for GenAI systems. |

### Optional Deeper Dives

| Resource | Type | Time | Best for |
|---|---|---:|---|
| [AI Evals for Engineers](https://maven.com/parlance-labs/evals), Hamel Husain and Shreya Shankar | Paid course | 8 hrs async | Serious practitioners building eval programs. |
| [Calibrating LLM-as-a-Judge](https://www.langchain.com/articles/llm-as-a-judge), LangChain | Blog | 20 min | Learners implementing human correction loops. |
| [LLM-as-a-Judge Evaluator Templates](https://arize.com/llm-as-a-judge/), Arize | Guide | 20 min | Learners building reusable eval templates. |
| [Evaluating and Debugging Generative AI](https://www.deeplearning.ai/short-courses/evaluating-debugging-generative-ai/), DeepLearning.AI and W&B | Short course | 50 min | Learners who want a Weights & Biases angle. |

## Week 5: Finetuning and Local Models

Make AI yours. Run it on your terms.

### Learning Objective

Know when prompting, RAG, or finetuning is the right lever. Understand LoRA/QLoRA, data preparation, PEFT workflows, local inference, quantization, privacy benefits, and the basics of model serving.

### Core Prerequisite Resources

| Order | Resource | Type | Time | Why it belongs | Covers |
|---|---|---:|---|---|---|
| 1 | [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685), Hu et al. | Paper | 45-60 min | Foundational parameter-efficient finetuning method from Microsoft researchers. | Rank decomposition, adapter training, parameter efficiency, inference latency. |
| 2 | [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314), Dettmers et al. | Paper | 45-60 min | Canonical method for memory-efficient finetuning of quantized LLMs. | 4-bit NF4, double quantization, paged optimizers, large-model finetuning on constrained hardware. |
| 3 | [Hugging Face PEFT Docs](https://huggingface.co/docs/peft), [PEFT GitHub](https://github.com/huggingface/peft), and [PEFT Blog](https://huggingface.co/blog/peft) | Docs and code | 1-2 hrs | Production-standard open-source library for LoRA, QLoRA, and adapters. | LoRA, QLoRA, prompt tuning, IA3, adapter loading, merging, saving. |
| 4 | [Hugging Face Transformers Training Guide](https://huggingface.co/docs/transformers/en/training) | Official docs | 1 hr | Core training reference for the Transformers ecosystem. | Trainer API, training arguments, evaluation, checkpoints, mixed precision. |
| 5 | [Hugging Face LLM Course: SFT with TRL](https://huggingface.co/learn/llm-course/chapter11/1) | Course | 2-3 hrs | Hands-on supervised fine-tuning workflow using current Hugging Face tooling. | Chat templates, SFTTrainer, datasets, LoRA, evaluation. |
| 6 | [How to Fine-Tune Open LLMs in 2025 with Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2025), Philipp Schmid | Blog and code | 1-2 hrs | Current applied guide from a Hugging Face engineer. | QLoRA, data formatting, distributed training, Flash Attention, evaluation. |
| 7 | [Ollama](https://ollama.com) and [Ollama GitHub](https://github.com/ollama/ollama) | Tool/docs | 1 hr | Practical default for running local LLMs through CLI and REST API. | Local inference, model management, OpenAI-compatible API, custom models. |
| 8 | [llama.cpp Quantization Guide](https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md) | Docs | 1 hr | Foundational local inference and quantization ecosystem. | GGUF, quantization formats, CPU/GPU inference, conversion workflows. |
| 9 | [Fine-Tuning and Reinforcement Learning for LLMs](https://www.deeplearning.ai/courses/fine-tuning-and-reinforcement-learning-for-llms-intro-to-post-training), DeepLearning.AI | Course | 6 hrs | Useful bridge from SFT to broader post-training workflows. | SFT, RLHF, reward modeling, DPO/GRPO concepts, deployment criteria. |

### Optional Deeper Dives

| Resource | Type | Time | Best for |
|---|---|---:|---|
| [Fine-Tune Llama 3.1 Ultra-Efficiently with Unsloth](https://huggingface.co/blog/mlabonne/sft-llama3), Maxime Labonne | Blog and Colab | 1.5 hrs plus hands-on | Learners who want a practical Colab finetuning lab. |
| [PEFT Methods Deep-Dive](https://huggingface.co/blog/samuellimabraz/peft-methods), Hugging Face | Blog | 1 hr | Learners comparing LoRA variants and adapter methods. |
| [vLLM Documentation](https://docs.vllm.ai/) | Official docs | 1 hr | Learners who want an introduction to model serving infrastructure. |

## Week 6: AI Security and Production Readiness

The week that separates demos from deployments.

### Learning Objective

Identify real LLM risks, design mitigations, understand prompt injection, implement guardrails, protect PII, run red-team tests, and evaluate whether a system is ready for production deployment.

### Core Prerequisite Resources

| Order | Resource | Type | Time | Why it belongs | Covers |
|---|---|---:|---|---|---|
| 1 | [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) and [2025 PDF](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf) | Reference | 1.5-2 hrs | OWASP is the standard application-security reference, and the LLM Top 10 is the baseline for GenAI threat modeling. | Prompt injection, sensitive data disclosure, excessive agency, supply chain, vector/embedding weaknesses. |
| 2 | [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) and [GenAI Profile NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) | Framework | 2-3 hrs | Federal-standard risk framework for AI governance and controls. | Govern, Map, Measure, Manage, trustworthiness, GenAI risk categories. |
| 3 | [NIST Adversarial Machine Learning Taxonomy](https://csrc.nist.gov/pubs/ai/100/2/e2025/final) | Technical report | 1-2 hrs | Authoritative taxonomy of adversarial ML attacks and mitigations. | Evasion, poisoning, extraction, inversion, supply-chain attacks. |
| 4 | [MITRE ATLAS](https://atlas.mitre.org) | Knowledge base | 1-2 hrs | ATT&CK-style framework for adversarial threats to AI systems. | Tactics, techniques, procedures, real-world case studies, mitigations. |
| 5 | [Microsoft PyRIT Announcement](https://www.microsoft.com/en-us/security/blog/2024/02/22/announcing-microsofts-open-automation-framework-to-red-team-generative-ai-systems/), [PyRIT GitHub](https://github.com/Azure/PyRIT), and [Red Teaming 100 GenAI Products](https://www.microsoft.com/en-us/security/blog/2025/01/13/3-takeaways-from-red-teaming-100-generative-ai-products/) | Tool and blogs | 1-2 hrs | Practical red-teaming framework from Microsoft’s AI Red Team. | Automated adversarial testing, multi-turn attacks, scoring, safety categories. |
| 6 | [Practical LLM Security Advice from the NVIDIA AI Red Team](https://developer.nvidia.com/blog/practical-llm-security-advice-from-the-nvidia-ai-red-team/) and [Agentic Code Execution Risks](https://developer.nvidia.com/blog/how-code-execution-drives-key-risks-in-agentic-ai-systems/) | Engineering blogs | 45 min | Real production security lessons for LLM and agent systems. | RAG access control, markdown injection, sandboxing, remote code execution risk. |
| 7 | [NVIDIA Garak](https://github.com/NVIDIA/garak) | Tool | 1 hr | Vulnerability scanner for LLM applications maintained by NVIDIA. | Prompt injection probes, leakage, jailbreaks, hallucination testing, CI integration. |
| 8 | [NVIDIA NeMo Guardrails Docs](https://docs.nvidia.com/nemo/guardrails/latest/index.html) and [Guardrails AI Docs](https://guardrailsai.com/guardrails/docs) | Official docs | 1-2 hrs | Covers two prominent guardrail approaches: programmable rails and validation-first rails. | Input/output rails, Colang, validators, safety constraints, structured validation. |
| 9 | [Langfuse Observability Docs](https://langfuse.com/docs/observability/overview) | Official docs | 45-60 min | Complements security with production monitoring and trace review. | Traces, prompt versions, token cost, sessions, evals, monitoring. |
| 10 | [Microsoft Responsible AI Standard v2](https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-Responsible-AI-Standard-v2-General-Requirements-3.pdf) | Reference document | 1.5 hrs | Operational responsible-AI controls from a major AI lab and enterprise deployer. | Impact assessment, accountability, transparency, privacy, reliability, human oversight. |

### Optional Deeper Dives

| Resource | Type | Time | Best for |
|---|---|---:|---|
| [DataTalks.Club MLOps Zoomcamp](https://datatalks.club/blog/mlops-zoomcamp.html) | Course | Targeted modules | Learners who need broader MLOps/production infrastructure context. |
| [NeMo Guardrails Tutorials](https://docs.nvidia.com/nemo/guardrails/latest/getting-started/tutorials/index.html) | Docs | 1-2 hrs | Learners implementing programmable guardrails. |
| [OWASP GenAI Security Project](https://genai.owasp.org/) | Project hub | Reference | Learners tracking evolving AI security guidance. |



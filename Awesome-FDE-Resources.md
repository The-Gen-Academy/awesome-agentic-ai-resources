# Awesome FDE Resources

> A curated collection of resources for aspiring and practicing
> Forward Deployed Engineers.

Forward Deployed Engineers combine software engineering, AI application
development, enterprise integration, product judgment, and customer
communication to deliver production systems in real-world environments.

This repository collects high-quality learning materials, practical
guides, case studies, tools, and career resources for developing those
capabilities.

## Contents

- [Start Here](#start-here)
  - [What is a Forward Deployed Engineer?](#what-is-a-forward-deployed-engineer)
- [Understanding the FDE Role](#understanding-the-fde-role)
- [Core Skills](#core-skills)
- [Portfolio Projects](#portfolio-projects)
- [Interview Preparation](#interview-preparation)

## Start Here

### What is a Forward Deployed Engineer?

A **Forward Deployed Engineer (FDE)** is a software engineer who works
closely with customers or end users to understand difficult operational
problems and deliver working technical solutions.

Unlike a traditional product engineer, who usually builds against an
internal product roadmap, an FDE helps discover the problem, define the
desired outcome, build and integrate the solution, deploy it in the
customer’s environment, and measure whether it creates real value.

The typical FDE delivery cycle is:

> **Discover → Define → Prototype → Integrate → Productionize → Measure → Generalize**

FDE responsibilities commonly include:

- Interviewing users and mapping their workflows
- Converting ambiguous requirements into a focused technical plan
- Building production-quality software, data pipelines, integrations,
  or AI agents
- Working with APIs, cloud infrastructure, authentication, permissions,
  and customer data
- Testing, monitoring, evaluating, and supporting deployed systems
- Explaining technical decisions to engineers, executives, and
  nontechnical stakeholders
- Turning lessons from individual deployments into reusable product
  capabilities

The exact role varies between companies. Some FDEs primarily build
products, while others focus on AI applications, enterprise integrations,
infrastructure, industry-specific deployments, or technical pre-sales.
An FDE opportunity should therefore be evaluated by its responsibilities,
not by its title alone.

### FDE vs Related Roles

The boundaries between forward deployed engineering and related roles vary between companies. The clearest distinction is usually the combination of customer proximity, hands-on engineering, and production ownership.

#### FDE vs Product Engineer

A product engineer usually works from an internally defined product roadmap and builds features intended for a broad group of users.

An FDE works more directly with a particular customer or operational team. The FDE helps discover the problem, adapts the solution to the customer’s environment, supports its deployment, and brings lessons from the field back into the core product.

#### FDE vs Solutions Engineer

A solutions engineer commonly focuses on demonstrations, technical validation, proofs of concept, and helping customers evaluate or purchase a product.

An engineering-focused FDE generally has deeper implementation and production ownership. This can include writing production code, creating integrations, handling deployment constraints, monitoring the system, and improving it after launch.

Some commercially aligned FDE roles also support pre-sales activities, so candidates should examine the actual responsibilities rather than relying only on the job title.

#### FDE vs Technical Consultant

A technical consultant may advise customers, design solutions, and sometimes build software.

An FDE is typically embedded more closely in the delivery cycle and remains accountable for turning a problem into a working production system. FDEs also commonly convert lessons from customer-specific deployments into reusable tools, product features, or implementation patterns.

### Common FDE Archetypes

The FDE title covers several related but distinct roles.

#### Product-Builder FDE

Builds full-stack solutions for strategic customers and converts successful customer-specific work into reusable product capabilities.

#### Applied AI or Agent FDE

Builds production AI applications involving models, agents, retrieval, tool use, evaluations, guardrails, and human escalation.

#### Integration and Implementation FDE

Connects products to customer systems through APIs, webhooks, data pipelines, identity systems, cloud environments, and legacy infrastructure.

#### Revenue or Pre-Sales FDE

Supports technical discovery, proofs of concept, customer onboarding, executive presentations, adoption, and account expansion while retaining hands-on engineering responsibilities.

#### Domain-Specialist FDE

Combines engineering ability with expertise in a particular industry, such as healthcare, legal services, finance, semiconductors, or manufacturing.

#### Infrastructure, Security, or Government FDE

Focuses on secure deployment, networking, identity and access management, compliance, self-hosted environments, reliability, and mission-specific requirements.

#### Robotics or Physical-Systems FDE

Deploys and supports software in physical environments such as robotics, manufacturing, autonomous systems, or industrial operations. These roles may involve hardware integration and substantial customer-site work.

## Understanding the FDE Role
- [Forward Deployed Engineer at OpenAI](https://openai.com/careers/forward-deployed-engineer-%28fde%29-seattle-seattle/) — A first-party role description showing how FDEs own customer discovery, technical scoping, system design, implementation, production rollout, adoption, and product feedback.

- [How Forward Deployed Engineering Is Redefining Client Transformation](https://www.ibm.com/think/perspectives/how-forward-deployed-engineering-is-redefining-client-transformation) — An overview of forward deployed engineering as an embedded, outcome-focused operating model rather than simply a new engineering job title.

- [Forward Deployed Units: IBM Consulting’s Field Model for Scaling AI](https://www.ibm.com/think/perspectives/forward-deployed-units-ibm-consulting-field-model-scaling-ai-transformation) — Explains how multidisciplinary forward deployed teams combine engineering, business context, AI, and change management to deliver production outcomes.

## Core Skills

### Production Software Engineering

FDEs need strong software-engineering fundamentals to build, integrate,
deploy, and operate reliable customer-facing systems.

- [The Python Tutorial](https://docs.python.org/3/tutorial/) — The official introduction to Python’s core language features, data structures, modules, error handling, and standard library. Best suited to readers who already understand basic programming.

- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/) — A practical guide to building Python APIs with request validation, authentication, error handling, testing, databases, and deployment.

- [PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html) — The official introductory guide to relational databases and SQL using PostgreSQL, including queries, joins, aggregates, transactions, and advanced database features.

- [Docker Get Started](https://docs.docker.com/get-started/) — Docker’s official introduction to containers, images, application packaging, persistent data, multi-container applications, and deployment workflows.

### AI Application Engineering

FDEs working with AI systems need to understand how to design agents,
connect them to tools and knowledge, evaluate their behavior, and manage
production risks.

- [A Practical Guide to Building AI Agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) — Introduces agent use-case selection, model and tool design, instructions, orchestration patterns, and guardrails for production systems.

- [Introducing Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval) — Explains retrieval-augmented generation, embeddings, BM25, chunking, contextual retrieval, reranking, and the trade-offs involved in grounding AI applications on external knowledge.

- [Working with Evals](https://developers.openai.com/api/docs/guides/evals) — A practical guide to creating evaluation datasets, testing model behavior, defining grading criteria, and comparing application performance across changes.

- [OWASP Top 10 for LLM and Generative AI Applications](https://genai.owasp.org/initiatives/top-10-for-llm-and-genai/) — A security reference covering risks such as prompt injection, sensitive-information disclosure, improper output handling, excessive agency, and insecure model or data supply chains.

### Enterprise Integration and Deployment

FDEs frequently deploy software into customer environments with existing
identity systems, cloud infrastructure, security controls, and delivery
processes.

- [OAuth 2.0 and OpenID Connect Protocols](https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols) — Explains authentication and authorization concepts including identity providers, clients, protected resources, access tokens, ID tokens, refresh tokens, and common OAuth flows.

- [Best Practices for Using Webhooks](https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks) — Covers secure webhook delivery, secret validation, event handling, response timing, redelivery, and protection against replay attacks.

- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — A framework for designing and reviewing secure, reliable, efficient, cost-effective, and sustainable cloud workloads.

- [GitHub Actions Quickstart](https://docs.github.com/en/actions/get-started/quickstart) — Introduces continuous integration and delivery workflows for automatically building, testing, and deploying software.

- [Kubernetes Concepts](https://kubernetes.io/docs/concepts/overview/) — The official introduction to Kubernetes architecture, workloads, services, storage, configuration, security, policies, and cluster administration.

### Product and Customer Skills

FDEs must understand user workflows, define the right problem, manage
trade-offs, establish success measures, and communicate clearly with
technical and nontechnical stakeholders.

- [User Research in Discovery](https://www.gov.uk/service-manual/user-research/user-research-in-discovery) — A practical guide to identifying users, understanding their current workflows, uncovering problems, conducting interviews and observation, and using evidence to scope a service.

- [Technical Writing Courses for Engineers](https://developers.google.com/tech-writing/overview) — Google’s courses on writing clear technical documentation, organizing information, explaining complex ideas, and communicating effectively with technical audiences.

- [Measuring the Success of Your Service](https://www.gov.uk/service-manual/measuring-success/measuring-the-success-of-your-service) — Guidance on defining meaningful performance measures and combining operational metrics with user research to determine whether a service is producing the intended outcome.

## Portfolio Projects

A strong FDE portfolio should demonstrate the ability to take a real
operational problem from discovery through production—not only build a
technical demo.

A portfolio project should ideally include:

- A real user, customer, or operational workflow
- A clearly defined problem and measurable outcome
- Messy, incomplete, or permission-controlled data
- APIs, webhooks, or third-party integrations
- An AI component with documented failure modes
- Automated tests and an evaluation dataset
- Authentication, authorization, privacy, and security decisions
- Deployment instructions, monitoring, and rollback planning
- An architecture diagram and important technical decisions
- A short demonstration explaining user value and engineering trade-offs

## Interview Preparation

FDE interview processes vary between companies, but commonly assess
practical coding, system design, problem decomposition, customer judgment,
communication, and production ownership.

- [Forward Deployed Engineer Interview Guide](https://www.theforwarddeployed.io/interview/method) — An FDE-specific overview of interview stages, coding screens, decomposition exercises, unfamiliar codebases, AI system design, customer simulations, and leadership discussions.

- [Forward Deployed Engineer Interview Questions](https://fdepulse.com/career/forward-deployed-engineer-interview-questions/) — Practice questions covering coding, system design, customer scenarios, deployment automation, and behavioral interviews.

- [OpenAI Interview Guide](https://openai.com/interview-guide/) — OpenAI’s official explanation of its application process, skills assessments, pair coding, technical tests, final interviews, communication expectations, and policies regarding AI tools.

- [Anthropic Careers: How We Hire](https://www.anthropic.com/careers) — Anthropic’s official guidance on live coding, debugging, technical trade-offs, permitted documentation use, prior experience, and nontechnical interview discussions.

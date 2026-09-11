# Awesome FDE Resources

> A curated collection of resources for Forward Deployed Engineers who
> discover customer problems and deliver production AI solutions.

## Contents

1. Understanding the FDE Role
2. Customer Discovery & Problem Framing
3. Solution Design
4. Building & Evals
5. Integrations & Enterprise Engineering
6. Production & Deployment
7. Working With Customers & Stakeholders
8. Adoption & Change Management
9. Measuring Business Impact
10. Turning Field Learning Into Product
11. FDE Case Studies
12. FDE Careers & Interviews
13. Technical Foundations
14. FDE Playbook

## 1. Understanding the FDE Role

Forward Deployed Engineers work closely with customers to turn ambiguous,
high-value problems into production systems.

The role sits at the intersection of:

- Customer discovery
- Software and AI engineering
- Enterprise deployment
- Product judgment
- Stakeholder communication
- Adoption and measurable business outcomes

Unlike a traditional software engineering role, the work does not end when
code ships. FDEs stay close to the customer, learn from real deployments,
and feed those learnings back into the product.

### Resources

#### [Palantir — Forward Deployed Engineering](https://www.palantir.com/docs/foundry/architecture-center/overview)

**Type:** Primary source  
**Level:** Beginner  
**Focus:** FDE philosophy

A useful introduction to the original Forward Deployed Engineering model.
It explains how engineers work close to real operational problems and use
what they learn in the field to shape the core product

---

#### [OpenAI — Forward Deployed Engineer](https://openai.com/careers/forward-deployed-engineer-%28fde%29-sf-san-francisco/)

**Type:** Role overview  
**Level:** Beginner  
**Focus:** Modern AI FDE

Shows what FDE work looks like in an AI company today: discovery, technical
scoping, system design, building, production rollout, adoption, evaluation,
and feeding deployment learnings back into product and research.

---

#### [Vannevar Labs — Forward Deployed Engineering](https://vannevarlabs.com/blog/forward-deployed-engineering/)

**Type:** Engineering article  
**Level:** Beginner–Intermediate  
**Focus:** Embedded engineering

Explains why engineers need to embed with users to understand what should
actually be built, and how customer understanding can drive new products.

---

#### [The Definitive Guide to Forward Deployed Engineering](https://nextplayso.substack.com/p/the-definitive-guide-to-forward-deployed)

**Type:** Practitioner guide  
**Level:** Beginner–Intermediate  
**Focus:** FDE operating model

A practitioner perspective from the former leader of Palantir's Project
Frontline program, covering what FDEs actually do, why the model works,
and common misconceptions about the role.

## 2. Customer Discovery & Problem Framing

Before designing a solution, an FDE needs to understand how the customer
currently works, where the real problem occurs, and why solving it matters.

This includes:

* Understanding users and stakeholders
* Mapping existing workflows
* Identifying pain points and bottlenecks
* Separating symptoms from root causes
* Understanding technical and organizational constraints
* Defining measurable outcomes
* Deciding whether AI is actually appropriate

### Resources

#### [Learning About Users and Their Needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs)

**Type:** Guide
**Level:** Beginner
**Focus:** User research

A practical introduction to understanding what users are trying to accomplish
before deciding what should be built. Useful for avoiding the common mistake
of treating a customer's requested feature as the underlying problem.

---

#### [Writing an Effective Guide for a User Interview](https://www.nngroup.com/articles/interview-guide/)

**Type:** Guide
**Level:** Beginner
**Focus:** Stakeholder interviews

Explains how to prepare open-ended interview questions, organize an interview
guide, use follow-up questions, and avoid leading participants toward a
particular answer.

---

#### [Creating an Experience Map](https://www.gov.uk/service-manual/user-research/creating-an-experience-map/)

**Type:** Guide
**Level:** Beginner–Intermediate
**Focus:** Workflow mapping

Shows how to map a user's journey across actions, pain points, teams, systems,
and dependencies. Useful for FDEs trying to understand how work actually moves
through an organization before introducing automation or AI.

---

#### [5 Whys Analysis](https://www.atlassian.com/team-playbook/plays/5-whys)

**Type:** Framework
**Level:** Beginner
**Focus:** Root-cause analysis

A simple technique for repeatedly asking why a problem occurs in order to move
past visible symptoms and identify the underlying cause.

---

#### [Framework for Innovation — Double Diamond](https://www.designcouncil.org.uk/resources/framework-for-innovation/)

**Type:** Framework
**Level:** Beginner–Intermediate
**Focus:** Problem framing

Introduces the Double Diamond approach: explore the problem broadly, define the
right challenge, develop possible solutions, and test them.

Useful for FDEs working with ambiguous customer requests where the original
problem statement may change as more context is discovered.

---

#### [Identifying and Scaling AI Use Cases](https://openai.com/business/guides-and-resources/identifying-and-scaling-ai-use-cases/)

**Type:** Guide
**Level:** Beginner–Intermediate
**Focus:** AI opportunity identification

A practical guide for identifying areas where AI can create meaningful
business value and prioritizing use cases based on their potential impact.

Useful after customer discovery when deciding whether the problem actually
benefits from AI and which opportunity is worth pursuing first.

---

#### [Project Poster](https://www.atlassian.com/team-playbook/plays/project-poster)

**Type:** Framework
**Level:** Beginner
**Focus:** Opportunity framing

A collaborative framework for documenting the problem, assumptions, possible
solutions, scope, and intended outcome before committing significant
engineering effort.

Useful for turning discovery findings into a shared problem statement that
customer and engineering teams can align around.

---

#### [Define What Success Looks Like](https://www.gov.uk/service-manual/service-standard/point-10-define-success-publish-performance-data)

**Type:** Guide
**Level:** Beginner
**Focus:** Success metrics

Guidance for defining measurable outcomes before delivery begins.

Useful for ensuring an FDE engagement is evaluated based on changes to the
customer's workflow or business outcome rather than whether a technically
impressive system was built.

## 3. Solution Design

Once the customer problem is clear, an FDE needs to decide how the solution
should actually work.

The goal is not to make every step autonomous or AI-powered. Good solution
design means choosing the simplest architecture that can reliably solve the
customer's problem.

This includes:

* Breaking workflows into individual tasks
* Identifying deterministic vs model-driven steps
* Choosing between prompting, RAG, tools, workflows, and agents
* Designing human-review and escalation points
* Defining model inputs, outputs, and context
* Planning integrations and permissions
* Considering latency, cost, reliability, and safety
* Anticipating failure modes and fallback behavior

### Resources

#### [A Practical Guide to Building AI Agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)

**Type:** Guide
**Level:** Beginner–Intermediate
**Focus:** Agent design

Explains when an agent is appropriate, how models, tools, and instructions
fit together, and how to think about guardrails and human intervention.

Useful for FDEs deciding whether a customer workflow actually requires an
agent or can be solved with a simpler architecture.

---

#### [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents)

**Type:** Engineering guide
**Level:** Intermediate
**Focus:** Workflows vs agents

Distinguishes predictable workflows from more autonomous agents and recommends
starting with simple, composable patterns before adding unnecessary complexity.

Especially useful for FDEs because customer problems often do not require
fully autonomous systems.

---

#### [Application Design for AI Workloads](https://learn.microsoft.com/en-us/azure/well-architected/ai/application-design)

**Type:** Architecture guide
**Level:** Intermediate–Advanced
**Focus:** Production AI architecture

Covers the architectural components of AI applications, including models,
orchestration, knowledge sources, tools, agents, and supporting application
layers.

Useful for moving from a proof of concept to a system that can fit into a
customer's broader technical environment.

---

### Cohort-Based Learning

#### [Mastering Agentic AI](https://maven.com/aishwarya-srinivasan/mastering-ai-agents)

**Type:** Cohort-based course
**Level:** Intermediate
**Focus:** Production AI systems

Covers LLM application foundations, RAG and context engineering, agent
architectures, orchestration, MCP and A2A, evaluations, observability,
security, and production readiness.

*Created by The Gen Academy, the maintainers of this resource collection.*


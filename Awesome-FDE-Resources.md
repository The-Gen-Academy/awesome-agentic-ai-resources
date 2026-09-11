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

## 4. Building & Evals

An FDE should build the smallest end-to-end version of a solution that can be
tested inside a realistic customer workflow.

The goal is not just to create a convincing demo. The system needs to perform
the intended task reliably, handle important failure cases, and improve the
customer outcome it was designed for.

This includes:

* Building a small end-to-end vertical slice
* Testing with realistic customer inputs
* Creating representative evaluation datasets
* Defining clear success criteria
* Testing tool calls and integrations
* Reviewing agent traces and outcomes
* Identifying and classifying failures
* Turning failures into regression tests
* Measuring latency and cost
* Re-running evals as the system changes

### Resources

#### [Working with Evals](https://developers.openai.com/api/docs/guides/evals)

**Type:** Documentation
**Level:** Intermediate
**Focus:** Building evaluation workflows

A practical guide to creating evaluation datasets, defining evaluation
criteria, running evals, and comparing different versions of an AI system.

Useful for FDEs who need to turn customer requirements and observed failures
into repeatable tests before deploying changes.

---

#### [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

**Type:** Engineering guide
**Level:** Intermediate–Advanced
**Focus:** Agent evaluation

A detailed guide to evaluating agentic systems using tasks, trials, graders,
execution traces, and real-world outcomes.

Particularly useful for FDEs building systems that call tools or take actions,
where evaluating only the final model response may miss important failures.

---

#### [Production ML Systems: Deployment Testing](https://developers.google.com/machine-learning/crash-course/production-ml-systems/deployment-testing)

**Type:** Engineering guide
**Level:** Intermediate
**Focus:** End-to-end system testing

Explains why production AI and ML systems need testing beyond model quality,
including input validation, infrastructure compatibility, pipeline integration,
and end-to-end testing.

Useful for FDEs because failures in customer deployments often happen at the
boundaries between models, data, infrastructure, and external systems rather
than inside the model itself.

## 5. Integrations & Enterprise Engineering

FDEs rarely build systems in isolation. A solution usually needs to connect
with the customer's existing APIs, databases, applications, identity systems,
and internal infrastructure.

Strong integration design means understanding not only how two systems connect,
but how the connection behaves when authentication expires, requests fail,
events arrive twice, schemas change, or one system becomes unavailable.

This includes:

* APIs and service integration
* Authentication and authorization
* OAuth and permissions
* Webhooks and event-driven systems
* Data synchronization
* Retries and idempotency
* Rate limits and timeouts
* Legacy and enterprise systems
* Integration failure handling
* AI tool and MCP integrations

### Resources

#### [Determine Integration Requirements — Microsoft](https://learn.microsoft.com/en-us/power-platform/architecture/key-concepts/integration-patterns/requirements)

**Type:** Architecture guide
**Level:** Intermediate
**Focus:** Integration design

Provides a structured way to evaluate an integration based on data volume,
frequency, direction of data flow, and the capabilities of each connected
system.

Useful for FDEs because integration design should begin with customer and
system constraints rather than immediately choosing an API or architecture.

---

#### [Enterprise Integration Patterns — Gregor Hohpe & Bobby Woolf](https://www.enterpriseintegrationpatterns.com/)

**Type:** Reference / Book
**Level:** Intermediate–Advanced
**Focus:** Enterprise messaging patterns

A foundational collection of patterns for connecting applications using
messaging and asynchronous communication.

Useful for understanding recurring integration problems such as message
routing, transformation, delivery, coordination, and communication between
systems that were not originally designed to work together.

---

#### [Best Practices for Using Webhooks — GitHub](https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks)

**Type:** Documentation
**Level:** Intermediate
**Focus:** Event-driven integrations

Covers practical webhook concerns including event filtering, secrets,
verification, fast acknowledgement, redelivery, and protecting against
duplicate or replayed events.

Useful for FDEs building integrations where customer systems need to react
reliably to events from external applications.

---

#### [Idempotent Requests — Stripe](https://docs.stripe.com/api/idempotent_requests)

**Type:** Documentation
**Level:** Intermediate
**Focus:** Reliable API calls

Explains how idempotency keys allow an application to safely retry an
operation without accidentally performing the same action multiple times.

This is especially important for FDEs building agents or automated workflows
that can trigger real-world actions such as creating records, sending
requests, or modifying customer systems.

---

#### [Authorization Code Flow with PKCE — Auth0](https://auth0.com/docs/get-started/authentication-and-authorization-flow/authorization-code-flow-with-pkce)

**Type:** Documentation
**Level:** Intermediate
**Focus:** Authentication and authorization

Explains the OAuth Authorization Code Flow with Proof Key for Code Exchange
and how applications securely obtain authorization to access APIs.

Useful for understanding the authentication layer behind many SaaS and
enterprise API integrations.

---

#### [Model Context Protocol — Architecture](https://modelcontextprotocol.io/specification/architecture)

**Type:** Protocol documentation
**Level:** Intermediate
**Focus:** AI tool integrations

Introduces the architecture behind MCP and how AI applications can connect
to external tools, resources, and systems through a standardized protocol.

Useful for FDEs building AI systems that need structured access to customer
applications, data sources, and internal tools.

## 6. Production & Deployment

A solution that works in a demo or development environment is not automatically
ready for a customer's organization.

FDEs need to turn prototypes into systems that are secure, observable,
reliable, and maintainable inside the customer's real environment.

This includes:

* Development, staging, and production environments
* Secrets and identity management
* Access controls and least privilege
* Data security and privacy
* Rate limits, retries, and fallbacks
* Logging, monitoring, and observability
* Reliability and failure recovery
* Versioning and rollback
* Gradual production rollout
* Incident response
* Operational ownership
* AI risk management

### Resources

#### [API Deployment Checklist — OpenAI](https://developers.openai.com/api/docs/guides/deployment-checklist)

**Type:** Deployment guide
**Level:** Intermediate
**Focus:** Production AI applications

A practical checklist for taking an AI application into production, covering
security, API access, reliability, latency, cost, rate limits, and operational
considerations.

Useful for FDEs moving from a working prototype to a customer-facing production
system where reliability and operational constraints matter.

---

#### [Design Principles for AI Workloads — Microsoft Azure](https://learn.microsoft.com/en-us/azure/well-architected/ai/design-principles)

**Type:** Architecture guide
**Level:** Intermediate–Advanced
**Focus:** Production AI architecture

Applies the Azure Well-Architected principles of reliability, security, cost
optimization, operational excellence, and performance efficiency specifically
to AI workloads.

Useful for thinking beyond model quality and considering the complete system
that needs to operate reliably inside an enterprise environment.

---

#### [Monitoring Distributed Systems — Google SRE](https://sre.google/sre-book/monitoring-distributed-systems/)

**Type:** Engineering guide
**Level:** Intermediate
**Focus:** Monitoring and observability

Introduces fundamental principles for monitoring production systems, including
latency, traffic, errors, and saturation.

Useful for FDEs because once a solution is deployed, teams need visibility into
whether the system is healthy, how users are experiencing it, and where failures
are occurring.

---

#### [Update a Deployment Without Downtime — Kubernetes](https://kubernetes.io/docs/tasks/run-application/update-deployment-rolling/)

**Type:** Documentation / Tutorial
**Level:** Intermediate
**Focus:** Rollouts and rollback

Demonstrates how rolling deployments can introduce new application versions
gradually while maintaining availability, as well as how to roll back when a
release causes problems.

Useful for understanding an important production principle: deployments should
be reversible rather than one-way changes to a customer's environment.

---

#### [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

**Type:** Framework
**Level:** Intermediate–Advanced
**Focus:** AI risk and governance

A framework for identifying, assessing, governing, and managing risks associated
with AI systems throughout their lifecycle.

Useful for FDEs working with enterprise customers where production deployment
may involve security, privacy, governance, compliance, safety, and organizational
risk requirements.

## 7. Working With Customers & Stakeholders

Forward Deployed Engineering is not only about building the right system.
FDEs also need to keep users, technical teams, decision-makers, and internal
partners aligned while the solution is being developed and deployed.

This means translating between business problems and technical decisions,
setting expectations, communicating trade-offs, gathering feedback, and
maintaining trust when requirements or constraints change.

This includes:

* Technical discovery conversations
* Stakeholder identification and alignment
* Setting expectations and communication cadence
* Explaining technical trade-offs
* Running project kickoffs
* Demonstrating work in progress
* Gathering and responding to feedback
* Communicating blockers and risks
* Working across engineering, product, sales, and customer teams
* Keeping stakeholders aligned as scope changes

### Resources

#### [A Guide for Successful Client Assessments and Discoveries — Thoughtworks](https://www.thoughtworks.com/en-in/insights/blog/digital-innovation/client-assessments-discoveries-part-1-people)

**Type:** Practitioner guide
**Level:** Intermediate
**Focus:** Client engagement and stakeholder alignment

Covers the people side of technical customer engagements, including identifying
stakeholders, agreeing on expectations, defining roles and responsibilities,
establishing communication cadence, and maintaining transparency.

Useful for FDEs because successful customer work depends on getting access to
the right people and keeping technical and business stakeholders aligned
throughout an engagement.

---

#### [Stakeholder Project Communication Plan — Atlassian](https://www.atlassian.com/team-playbook/plays/stakeholder-communications-plan)

**Type:** Framework
**Level:** Beginner–Intermediate
**Focus:** Stakeholder communication

Provides a practical framework for identifying who needs to be involved or
informed, what information each group needs, which communication channels to
use, and how frequently updates should happen.

Useful for FDEs managing deployments involving customer engineers, end users,
executives, security teams, product teams, and other stakeholders with very
different information needs.

---

#### [Project Kickoff — Atlassian](https://www.atlassian.com/team-playbook/plays/project-kickoff)

**Type:** Framework
**Level:** Beginner
**Focus:** Project alignment

Provides a structure for getting project sponsors, delivery teams, and
stakeholders aligned on goals, responsibilities, expectations, and how the
project will operate.

Useful at the beginning of an FDE engagement to make sure both the customer and
delivery team understand what is being built, why it matters, who owns which
decisions, and how progress will be evaluated.

---

#### [Run Effective Demo Meetings — Atlassian](https://www.atlassian.com/team-playbook/plays/run-demo-meetings)

**Type:** Practical guide
**Level:** Beginner
**Focus:** Customer demos and feedback

Explains how to structure demos so they show tangible progress, gather useful
feedback, align stakeholders around goals, and identify necessary changes.

Useful for FDEs because customer demos should not simply showcase technology.
They are opportunities to validate whether the solution actually fits the
workflow and expectations discovered earlier.

---

#### [End-to-End Demo — Atlassian](https://www.atlassian.com/team-playbook/plays/end-to-end-demo)

**Type:** Framework
**Level:** Beginner–Intermediate
**Focus:** Iterative customer feedback

Encourages teams to demonstrate the complete user experience early and
repeatedly rather than waiting until individual components are polished.

Useful for FDEs because showing an end-to-end workflow often exposes missing
requirements, integration problems, and incorrect assumptions much earlier
than reviewing individual features in isolation.

## 8. Adoption & Change Management

A technically successful deployment does not create value if people do not
actually use it.

FDEs need to understand why users adopt or reject a new system, help teams
transition from existing workflows, and make sure the solution becomes part
of normal day-to-day work.

This includes:

* Understanding barriers to adoption
* Communicating why the change matters
* Training users and support teams
* Building confidence and trust
* Supporting users during rollout
* Collecting feedback from real usage
* Measuring adoption
* Identifying workflow friction
* Reinforcing new ways of working
* Sustaining adoption after launch

### Resources

#### [Define a Strategy for Adoption and Change Management — Microsoft](https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/implementation-strategy-define-strategy-adoption-change-management)

**Type:** Implementation guide
**Level:** Intermediate
**Focus:** Adoption strategy

Explains why technically successful projects can still fail to deliver business
value when users do not adopt the new system.

Covers executive sponsorship, employee engagement, communication, project-team
involvement, and the relationship between user experience and successful
technology adoption.

Useful for FDEs because deployment success should be measured by whether the
solution becomes useful inside the customer's real workflow, not simply whether
it goes live.

---

#### [The Prosci ADKAR Model](https://www.prosci.com/methodology/adkar)

**Type:** Change management framework
**Level:** Beginner–Intermediate
**Focus:** Individual adoption

Introduces the ADKAR model:

* Awareness
* Desire
* Knowledge
* Ability
* Reinforcement

The framework helps explain why users may resist or fail to adopt a new system
even when the technology itself works.

Useful for FDEs diagnosing whether an adoption problem comes from lack of
understanding, motivation, training, capability, or reinforcement.

---

#### [Encouraging People to Use Your Digital Service — GOV.UK](https://www.gov.uk/service-manual/helping-people-to-use-your-service/encouraging-people-to-use-your-digital-service)

**Type:** Service design guide
**Level:** Beginner
**Focus:** Adoption barriers

Recommends researching people who are not using a new service rather than
assuming why adoption is low.

Covers common barriers such as lack of awareness, difficulty using the system,
lack of confidence, concerns about security, and preference for existing
workflows.

Useful for FDEs because poor adoption can reveal problems in the product,
workflow, training, or trust rather than simple resistance to change.

---

#### [Measuring Digital Take-Up — GOV.UK](https://www.gov.uk/service-manual/measuring-success/measuring-digital-take-up)

**Type:** Measurement guide
**Level:** Beginner–Intermediate
**Focus:** Adoption metrics

Explains how to establish a baseline and measure how many users move toward a
new digital workflow over time.

Useful for FDEs because adoption should be measured rather than inferred from
successful deployment or positive stakeholder feedback.

---

#### [Change Management Communication — Atlassian](https://www.atlassian.com/team-playbook/plays/change-management-communication-with-video)

**Type:** Practical framework
**Level:** Beginner
**Focus:** Communicating change

Provides a simple structure for explaining what is changing, why the change
matters, how users will be affected, what success looks like, and where users
can provide feedback.

Useful during an FDE rollout because users are more likely to adopt a new
workflow when they understand both the reason for the change and how it affects
their daily work.

---

#### [Manage Changes During Transition and Handover — Microsoft](https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/change-management-transition-handover)

**Type:** Implementation guide
**Level:** Intermediate
**Focus:** Sustaining adoption

Covers the transition from implementation to ongoing operation, including
knowledge transfer, training support teams, measuring usage, addressing
technology and process barriers, and sustaining the change after go-live.

Useful for FDEs preparing to move from hands-on deployment work toward long-term
customer ownership of the system.

## 9. Measuring Business Impact

An FDE engagement is successful only if the deployed system improves a real
customer outcome.

Technical quality and adoption matter, but they are not the final measure of
success. FDEs need to connect the system's performance to changes in the
customer's workflow, operating costs, revenue, risk, or user experience.

This includes:

* Defining success before deployment
* Establishing a baseline
* Measuring workflow outcomes
* Tracking time saved and productivity gains
* Measuring cost reduction or revenue impact
* Evaluating completion and error rates
* Measuring quality alongside speed
* Comparing outcomes before and after deployment
* Tracking total cost of operation
* Connecting technical metrics to business KPIs

### Resources

#### [How to Set Performance Metrics for Your Service — GOV.UK](https://www.gov.uk/service-manual/measuring-success/how-to-set-performance-metrics-for-your-service)

**Type:** Measurement guide
**Level:** Beginner–Intermediate
**Focus:** Metrics and baselines

Explains how to start from the purpose of a service, define intended benefits,
turn those benefits into measurable hypotheses, and establish meaningful
performance metrics.

It also emphasizes establishing a baseline so improvements can be compared
against the previous workflow rather than judged in isolation.

Useful for FDEs because success metrics should be defined before a solution is
built, not added after deployment.

---

#### [Using Performance Data to Improve Your Service — GOV.UK](https://www.gov.uk/service-manual/measuring-success/using-data-to-improve-your-service-an-introduction)

**Type:** Measurement guide
**Level:** Beginner
**Focus:** Operational outcomes

Introduces practical metrics such as cost per transaction, user satisfaction,
completion rate, and adoption.

Useful for FDEs because it connects usage data to whether a service is actually
helping users complete work more successfully and efficiently.

---

#### [A Scorecard for the AI Age — OpenAI](https://openai.com/index/a-scorecard-for-the-ai-age/)

**Type:** Business framework
**Level:** Intermediate
**Focus:** AI economics and productivity

Proposes evaluating AI based on the amount of useful work completed rather than
relying only on traditional software metrics such as seats or active users.

It focuses on questions such as:

* How much useful work gets completed?
* What does a successful task cost?
* How often is the work correct?
* Does the economics improve as usage grows?

Useful for FDEs connecting model or agent performance to the economic value
created for the customer.

---

#### [From Promise to Impact: How Companies Can Measure the Full Value of AI — McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/from-promise-to-impact-how-companies-can-measure-and-realize-the-full-value-of-ai)

**Type:** Business framework
**Level:** Intermediate–Advanced
**Focus:** Enterprise AI value

Introduces a layered approach for measuring AI initiatives from technical
performance and user engagement through strategic outcomes and financial
impact.

Examples include revenue growth, cost-to-serve reduction, margin improvement,
and total cost of ownership.

Useful for FDEs working with enterprise stakeholders who need evidence that an
AI deployment is producing measurable business value rather than simply
achieving technical milestones.

---

#### [How Evals Drive the Next Chapter in AI for Businesses — OpenAI](https://openai.com/index/evals-drive-next-chapter-of-ai/)

**Type:** Business and evaluation guide
**Level:** Intermediate
**Focus:** Connecting evals to business objectives

Explains a simple cycle:

**Specify → Measure → Improve**

The idea is to define what a good business outcome looks like, test the system
under realistic conditions, and improve it based on observed failures.

Useful for FDEs because evaluation criteria should ultimately reflect what the
customer considers successful rather than only model-level benchmarks.

## 10. Turning Field Learning Into Product

One of the most distinctive parts of Forward Deployed Engineering is what
happens after solving an individual customer's problem.

FDEs are in a position to see recurring workflow problems, missing platform
capabilities, integration patterns, and model limitations before those patterns
are obvious from inside the core product team.

The goal is to distinguish one-off customer requirements from insights that can
improve the product for many customers.

This includes:

* Identifying recurring customer problems
* Distinguishing bespoke requirements from reusable patterns
* Turning successful implementations into reusable components
* Codifying architectures and delivery patterns
* Sharing field feedback with product and research teams
* Identifying product gaps from deployment failures
* Creating internal playbooks and reference architectures
* Generalizing integrations and evaluation methods
* Influencing product and model roadmaps
* Reducing repeated custom work across engagements

### Resources

#### [Forward Deployed Engineering — Palantir Architecture Center](https://www.palantir.com/docs/foundry/architecture-center/overview)

**Type:** Primary source
**Level:** Beginner–Intermediate
**Focus:** Field-to-product feedback loops

Explains Palantir's Forward Deployed Engineering methodology, where engineers
work close to difficult customer problems while collaborating with core
engineering teams.

Field feedback is continuously synthesized into new product capabilities rather
than remaining isolated inside individual customer engagements.

Useful for understanding why Forward Deployed Engineering is not simply
implementation or consulting—it is also a mechanism for product development.

---

#### [Introducing OpenAI Frontier](https://openai.com/index/introducing-openai-frontier/)

**Type:** Primary source
**Level:** Beginner–Intermediate
**Focus:** Deployment-to-research feedback

Describes how Forward Deployed Engineers work alongside enterprise teams to
deploy agents in production while maintaining a direct connection to OpenAI
Research.

Deployment experience provides feedback not only about how applications should
change, but also about where models themselves need to improve.

Useful for understanding how field deployments can create a feedback loop
between customer problems, deployed systems, product development, and research.

---

#### [Forward Deployed Engineer — OpenAI](https://openai.com/careers/forward-deployed-engineer-%28fde%29-sf-san-francisco/)

**Type:** Role overview
**Level:** Intermediate
**Focus:** Codifying field patterns

OpenAI's FDE role explicitly includes turning successful deployment patterns
into tools, playbooks, and reusable building blocks.

It also describes sharing field feedback with Product and Research to help
identify where models and products succeed and where they need improvement.

Useful for showing that an FDE's responsibility extends beyond completing a
single deployment to improving how future deployments are built.

---

#### [Forward Deployed Software Engineer — OpenAI](https://openai.com/careers/forward-deployed-software-engineer-sf-san-francisco/)

**Type:** Role overview
**Level:** Intermediate
**Focus:** Reusable abstractions

Describes Forward Deployed Software Engineers as building abstractions from
customer problems that can improve the speed and quality of future FDE
engagements.

The role also involves contributing customer feedback to Product, Research,
and Applied Engineering teams and codifying lessons from deployments into
internal knowledge.

Useful for understanding the transition from solving a specific customer's
problem to creating reusable engineering capabilities.

---

#### [Who Are Palantir FDEs? — Palantir Developer Community](https://community.palantir.com/t/who-are-palantir-fdes/6847/4)

**Type:** Practitioner perspective
**Level:** Beginner–Intermediate
**Focus:** Product learning from the field

A perspective from a long-time Palantir FDE arguing that Forward Deployed
Engineering is not simply last-mile implementation.

The model involves taking ownership of customer outcomes and continuously
turning lessons from field deployments into improvements to the core platform.

Useful for understanding the mindset behind the field-to-product loop from a
practitioner who has worked inside the model for many years.

## 11. FDE Case Studies & Reference Implementations

Case studies help connect the individual skills in this collection into the
full lifecycle of a real deployment.

The most useful examples show more than which model or framework was used.
Look for how teams:

* Identified the original customer problem
* Worked within existing workflows and systems
* Designed the architecture
* Integrated enterprise data and tools
* Evaluated quality and failure modes
* Handled security and operational constraints
* Rolled the system out to real users
* Measured adoption and business impact
* Improved the system after deployment

### Resources

#### OpenAI Frontier — Enterprise Agent Deployments

**Type:** Deployment examples
**Level:** Intermediate
**Focus:** End-to-end enterprise AI

OpenAI describes several production deployments where agents are embedded into
important business workflows.

Examples include reducing manufacturing root-cause analysis from hours to
minutes, automating parts of a sales workflow, and using AI systems to improve
industrial production.

Useful for seeing how enterprise AI projects should ultimately be connected to
measurable workflow and business outcomes rather than standalone model demos.

---

#### Block — Internal AI Agent Deployment

**Type:** Case study
**Level:** Intermediate
**Focus:** Internal tools and enterprise adoption

Block deployed an internal AI agent that connects employees with company tools
and data, supports tasks such as querying information and generating SQL, and
helps automate internal workflows.

The case study is useful because it combines technical capability with
organization-wide adoption and measurable productivity gains.

---

#### Harvey — AI for Complex Legal Workflows

**Type:** Case study
**Level:** Intermediate
**Focus:** Human-in-the-loop enterprise AI

Harvey uses AI to turn complex legal tasks into structured workflows where the
system can ask follow-up questions, generate intermediate work, and allow human
review before producing the final result.

The deployment also had to satisfy enterprise security, privacy, compliance,
and regional data-processing requirements.

Useful for understanding how human review and enterprise constraints shape the
architecture of high-stakes AI systems.

---

#### Decagon — AI Customer Support Agents

**Type:** Case study
**Level:** Intermediate
**Focus:** Tool-integrated AI agents

Decagon builds customer-support agents that integrate with existing ticketing
systems, customer databases, and business processes rather than operating as
isolated chatbots.

Useful for studying how agents can combine model reasoning with enterprise
systems and structured workflows while still needing reliability and policy
compliance.

---

#### Sendbird — Enterprise AI Customer Service

**Type:** Case study
**Level:** Intermediate
**Focus:** Production reliability and scaling

Sendbird uses AI to power customer-support agents across a platform serving
thousands of businesses.

The case study covers the need to maintain accuracy, reliability, and
enterprise requirements while automating high-volume conversations.

Useful for understanding how an AI application changes when it has to operate
reliably across many customers rather than succeed in a controlled prototype.

---

#### Vannevar Labs — Forward Deployed Engineering

**Type:** Practitioner case study
**Level:** Intermediate
**Focus:** Building an FDE function

Vannevar Labs explains why its engineering organization introduced Forward
Deployed Engineers as it expanded across more customers, missions, and product
areas.

The article describes engineers embedding with users, learning their missions,
building alongside them, and turning that understanding into new product
capabilities.

Useful because it shows Forward Deployed Engineering being adopted as an
organizational model in response to real scaling and product-development
problems.

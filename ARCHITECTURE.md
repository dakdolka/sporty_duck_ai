# Sporty_duck_ai Architecture

> Living architecture document.
> This document describes the architectural principles, design decisions, and long-term vision of the project. It should evolve together with the codebase.

---

# Vision

Sporty_duck_ai is not designed to be a chatbot.

Its purpose is to become a long-term intelligent companion capable of building an increasingly accurate understanding of its user.

The system should gradually learn:

* user preferences;
* habits;
* goals;
* communication style;
* long-term context;
* personal knowledge.

The quality of the assistant is measured not only by the quality of individual responses, but by the quality of its understanding of the user.

---

# Core Principles

## AI is only one component

The language model is an implementation detail.

Business logic must never depend on a specific provider.

Current provider:

* Gemini

Future providers may include:

* OpenAI
* Ollama
* Anthropic
* Local models

Replacing the provider should require changes only inside the provider implementation.

---

## Domain-first architecture

Business logic is the core of the system.

Infrastructure exists only to support it.

The application should never depend directly on:

* databases;
* messaging platforms;
* AI providers;
* schedulers;
* caching systems.

Infrastructure depends on the application, never the other way around.

---

## Replaceable interfaces

User interaction should not affect business logic.

The assistant may be accessed through different interfaces:

* Telegram
* REST API
* CLI
* Discord
* Web
* Voice

All interfaces communicate with the same application layer.

---

## Memory is the product

Conversations are temporary.

Memory is permanent.

The primary objective of the system is not to answer questions, but to improve its internal model of the user.

Every interaction should contribute to that model.

---

## Explicit responsibilities

Every component has exactly one responsibility.

Examples:

**Repository**

Stores and retrieves data.

**Provider**

Communicates with external services.

**Service**

Coordinates business scenarios.

**Pipeline**

Executes complex workflows.

**Worker**

Runs scheduled or background processes.

**Tool**

Performs one isolated action.

---

# Project Structure

```text
project/

app/
    Business logic

infrastructure/
    External integrations

transport/
    Machine interfaces

user_interfaces/
    Human interfaces

workers/
    Background processing
```

---

# Layer Responsibilities

## app

Contains the application's business logic.

Responsible for:

* services;
* pipelines;
* repositories interfaces;
* domain rules;
* orchestration.

Must never depend on infrastructure implementations.

---

## infrastructure

Contains implementations of external systems.

Examples:

* PostgreSQL
* Gemini
* Redis
* Schedulers
* File storage

---

## transport

Interfaces used by other software.

Examples:

* REST API
* WebSocket
* Future gRPC

Responsible only for request validation and response serialization.

---

## user_interfaces

Human-facing interfaces.

Examples:

* Telegram Bot

Responsible only for translating platform events into application contracts.

---

## workers

Background processing.

Examples:

* memory consolidation;
* summarization;
* nightly reflection;
* scheduled reminders.

Workers initiate business scenarios but never contain business logic.

---

# Request Flow

```text
User

↓

Transport / User Interface

↓

Service

↓

Pipeline

↓

Application Services

↓

Repositories / Providers

↓

Response
```

---

# Memory

Memory is the central domain object.

The system intentionally avoids prematurely separating memories into different categories.

Everything is represented as a MemoryItem.

Possible examples:

* observation
* preference
* experience
* conclusion
* reminder
* context
* long-term knowledge

Classification may become more sophisticated as the project evolves.

---

# Memory Origin

Every memory records how it was created.

Examples:

* USER_MESSAGE
* SYSTEM_INFERENCE
* USER_CORRECTION
* TOOL
* IMPORT

The origin affects confidence and future reasoning.

---

# Memory Lifecycle

```text
Conversation

↓

Memory Extraction

↓

Consolidation

↓

Inference

↓

Gap Detection

↓

Question Generation

↓

Memory Update
```

Memory is continuously refined rather than simply accumulated.

---

# Inference

The assistant is allowed to generate hypotheses.

Hypotheses are never treated as facts.

Generated knowledge must always remain distinguishable from user-provided information.

Confidence should evolve over time.

---

# Knowledge Gaps

Instead of pretending to know, the assistant should actively identify:

* uncertainty;
* contradictions;
* missing information;
* incomplete understanding.

Whenever appropriate, it should ask clarifying questions.

---

# Tools

The LLM never performs actions directly.

Instead, it expresses intentions.

Examples:

* RememberMemory
* AskUser
* CreateReminder
* CreateTask

The application decides whether and how those intentions are executed.

---

# Repository Philosophy

Repositories are responsible only for persistence.

They never contain business logic.

---

# Service Philosophy

Services coordinate business scenarios.

They prepare data, select pipelines, and orchestrate application components.

---

# Pipeline Philosophy

Pipelines implement complex workflows.

They combine multiple services into a single business process while remaining independent of transport and infrastructure.

---

# Long-Term Vision

## Stage 1

* Conversations
* Memory

## Stage 2

* Inference Engine
* Knowledge Gap Detection

## Stage 3

* Decision Engine
* Strategy Engine
* Prediction Engine

## Stage 4

* Self-improving memory
* Adaptive communication
* Confidence recalculation
* Autonomous reasoning

---

# Design Philosophy

The assistant should never pretend certainty.

It should ask when uncertain.

It should distinguish observations from assumptions.

Understanding is iterative.

Memory evolves.

Every conversation is an opportunity to improve the internal model of the user.

The ultimate objective is not to maximize response quality.

The ultimate objective is to maximize understanding.

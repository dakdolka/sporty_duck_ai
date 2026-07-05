# AI Companion Architecture

> Living architecture document.
> This document describes the architectural principles of the project and should evolve together with the codebase.

---

# Project Goals

The goal of this project is **not** to build a chatbot.

The goal is to build an AI companion capable of:

- remembering the user;
- learning from interactions;
- building long-term knowledge;
- generating hypotheses;
- identifying gaps in knowledge;
- adapting communication strategies over time.

---

# Architectural Principles

## 1. LLM is NOT the center of the system.

The LLM is only one component.

It should be replaceable without affecting the rest of the application.

Today:
- Gemini

Tomorrow:
- OpenAI
- Ollama
- Any local model

Changing the provider should not require changes to business logic.

---

## 2. Single Responsibility

Every component has exactly one responsibility.

Examples:

ConversationService
- orchestrates a conversation

MemoryService
- manages memory lifecycle

Repository
- stores and retrieves data

Tool
- performs one action

AI Provider
- communicates with the model

---

## 3. Business logic must not depend on infrastructure.

Application knows nothing about

- PostgreSQL
- Redis
- Gemini
- Telegram

It communicates only through abstractions.

---

## 4. Transport is replaceable.

Telegram is not part of business logic.

Possible transports:

- Telegram
- REST API
- CLI
- Discord
- WebSocket

All of them interact with the same Application layer.

---

## 5. Memory is the core of the project.

Conversation is temporary.

Memory is permanent.

The assistant should evolve primarily by improving its memory.

---

# Layers

project/

app/
- business logic

infrastructure/
- external dependencies

user_interfaces/
- user interaction

transport/
- machine interfaces

workers/
- background processing

---

# Responsibilities

## app/

Contains all business logic.

Should never know how external systems work.

---

## infrastructure/

Contains implementations of external services.

Examples:

- PostgreSQL
- Redis
- Gemini
- Scheduler

---

## user_interfaces/

Interaction with users.

Examples:

- Telegram Bot

---

## transport/

Communication with other software.

Examples:

- REST API

---

## workers/

Background jobs.

Examples:

- memory consolidation
- summarization
- nightly reflection

---

# Main Flow

Telegram/User

↓

ConversationService

↓

ConversationPipeline

↓

ContextService

↓

AIService

↓

ToolManager

↓

MemoryService

↓

Repositories

↓

Response

---

# Memory Model

The project does NOT distinguish between facts and events.

Everything is represented as a MemoryItem.

A MemoryItem may represent:

- an observation
- a preference
- a conclusion
- temporary context
- long-term knowledge

The type system may evolve later.

---

# Memory Origins

Every MemoryItem has an origin.

Possible origins:

- USER_MESSAGE
- SYSTEM_INFERENCE
- USER_CORRECTION
- IMPORT
- TOOL

This distinction is critical.

User observations are considered more reliable than system-generated conclusions.

---

# Memory Lifecycle

Conversation

↓

Memory Extraction

↓

Memory Consolidation

↓

Inference Generation

↓

Knowledge Gap Detection

↓

Question Generation

↓

Memory Update

---

# Inference

The system is allowed to generate its own conclusions.

Generated conclusions are NOT facts.

They must always be distinguishable from user-provided information.

Future inference quality should improve over time.

---

# Knowledge Gaps

The assistant should continuously identify:

- missing information
- contradictions
- uncertainty

Instead of guessing, it should ask the user.

---

# Tools Philosophy

LLM does not modify the database directly.

LLM expresses intentions.

Examples:

RememberMemory

AskUser

CreateReminder

CreateTask

ToolManager decides how those intentions are executed.

---

# Repository Philosophy

Repositories know only storage.

They never contain business logic.

---

# Services Philosophy

Services coordinate business processes.

They never communicate directly with databases.

They use repositories.

---

# Pipelines Philosophy

Complex workflows should live in pipelines.

Services should stay thin.

---

# Long-Term Roadmap

Stage 1

Conversation
Memory

Stage 2

Inference Engine

Knowledge Gap Analyzer

Stage 3

Strategies

Decision Engine

Prediction Engine

Stage 4

Self-learning loop

Confidence recalculation

Memory evolution

Adaptive communication

---

# Future Ideas

(Not implemented yet)

- Strategy Engine
- Decision Engine
- Prediction Engine
- Emotional State
- Personality Model
- Goal Tracking
- Relationship Graph
- Memory Graph
- Explainable Reasoning

# Design Philosophy

The assistant should not pretend to know.

When uncertain, it should ask.

When making assumptions, it should remember that they are assumptions.

Memory is not static.

Memory evolves.

Understanding is iterative.

Every conversation is an opportunity to improve the internal model of the user.

The goal is not to maximize response quality.

The goal is to maximize understanding.
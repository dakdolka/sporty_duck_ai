# Sporty_duck_ai

An experimental long-term Sporty_duck_ai built with a domain-first architecture.

The goal of this project is not to build another chatbot.

Instead, it aims to build an assistant capable of continuously improving its understanding of its user through persistent memory, inference, and long-term learning.

## Vision

The assistant should:

* remember users across conversations;
* build long-term knowledge;
* generate hypotheses;
* identify missing information;
* improve its internal model over time;
* adapt its communication strategy.

The project is designed with provider independence in mind, allowing AI models, transports, and infrastructure components to be replaced without affecting business logic.

## Architecture

The project follows a layered architecture.

```text
project/

app/
    Business logic

infrastructure/
    External integrations

transport/
    REST API and machine interfaces

user_interfaces/
    Telegram bot and future user interfaces

workers/
    Background processing
```

Business logic remains independent from infrastructure.

## Technology Stack

* Python 3.12+
* FastAPI
* SQLAlchemy 2
* Alembic
* PostgreSQL
* aiogram
* Dependency Injector
* Pydantic v2

## Current Status

The project is under active development.

The architecture is considered more important than the number of implemented features.

## Roadmap

* User onboarding
* Conversation pipeline
* Memory extraction
* Memory consolidation
* Inference engine
* Knowledge gap detection
* Decision engine
* Adaptive communication

## Contributing

The architecture intentionally prioritizes maintainability, explicit responsibilities, and replaceable components.

Contributions that preserve these principles are always welcome.

## License

MIT

# Project Rules

## Architecture

* Keep business logic independent from infrastructure.
* Prefer composition over inheritance.
* Every class has a single responsibility.
* Every file contains a single primary class.
* Complex workflows belong in pipelines.
* Services should remain thin and orchestrate business scenarios.
* Repositories contain persistence logic only.
* Providers communicate with external systems only.

---

## Code Style

* Use asynchronous APIs whenever possible.
* Prefer explicit code over implicit magic.
* Favor readability over cleverness.
* Avoid premature optimization.
* Keep abstractions simple.

---

## Dependencies

* No SQL outside repositories.
* No AI provider calls outside providers.
* No transport-specific logic outside transport and user interface layers.
* Business logic must not depend on implementation details.

---

## Contracts

* Validate every external input.
* Use dedicated contracts for communication between layers.
* Avoid leaking ORM models outside repositories.

---

## Documentation

* Every public method should have a concise docstring.
* Significant architectural decisions should be documented.
* New features should begin with an architecture discussion before implementation.

---

## Philosophy

Code should be easy to replace.

Code should be easy to understand.

Architecture should support growth rather than optimization.

Always optimize for maintainability before convenience.

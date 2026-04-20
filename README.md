# orbital-notify-py

Python service for tracking ISS flyovers and sending pass notifications.

## Overview

`orbital-notify` is a backend-focused project that tracks upcoming International Space Station (ISS) passes for a location and sends notifications before a visible flyover.

The goal of this project is to demonstrate practical backend engineering in Python through:

- third-party API integration
- scheduled/background job processing
- notification workflows
- persistence
- Docker-based local development
- clean project structure and documentation

## Why I built this

I wanted a project that feels like a real service rather than a toy app.

This system is meant to showcase the kind of backend work I enjoy:
- integrating with external APIs
- building reliable services
- modeling domain workflows
- creating software that can be run, tested, and extended

## Planned Features

### v0
- [ ] project scaffold
- [ ] basic API srv
- [ ] health check endpoint

### v1
- [ ] register a location to monitor
- [ ] fetch upcoming ISS passes from an external API
- [ ] store subscriptions in a database
- [ ] list upcoming passes for a location
- [ ] schedule notifications before a pass
- [ ] send notifications through a pluggable notifier interface

### v2
- [ ] retry logic for failed notifications
- [ ] structured logging
- [ ] configuration via environment variables
- [ ] integration tests for key workflows
- [ ] Docker Compose for local startup

### v3
- [ ] metrics endpoint
- [ ] deployable demo environment
- [ ] optional CLI for local testing and admin workflows

## Tech Stack

- Python
- SQLite or Postgres
- Docker / Docker Compose
- External ISS pass API

## Current Status

Early scaffold / active development.

## Development Goals

This project is intentionally being built in public as a portfolio-quality backend system. The emphasis is on:

- clarity
- correctness
- maintainability
- practical engineering tradeoffs

## Future Ideas

- support multiple notification channels
- support timezone-aware alerts
- compare visible vs non-visible passes
- expose a small CLI for testing subscriptions
- add deployment manifests

## License

MIT

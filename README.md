# orbital-notify-py

Go service for tracking ISS flyovers and sending pass notifications.

## Overview

`orbital-notify` is a backend-focused project that tracks upcoming International Space Station (ISS) passes for a location and sends notifications before a visible flyover.

The goal of this project is to demonstrate practical backend engineering in Go through:

- third-party API integration
- scheduled/background job processing
- notification workflows
- persistence
- Docker-based local development
- clean project structure and documentation

This structure keeps the project simple while leaving room to split components later if needed.

## Stack

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

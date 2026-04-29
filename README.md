# orbital-notify-py

Orbital Notify is a backend systems project evolving into an event-driven data pipeline for ingesting, processing, and notifying on ISS pass events, with reliability and observability built into the design.

## Overview

This project is designed as practical proof of backend and platform engineering skills, emphasizing:

- API integration
- data ingestion and processing
- background job execution
- reliability patterns
- observability
- deployable service architecture

The focus is not just building a feature, but building a system.

## Current Capabilities

Implemented:

- FastAPI service with modular routing
- Environment-based configuration
- Application lifecycle hooks
- Request logging and observability foundation
- Production-style application structure

In Progress:

- External event ingestion
- Scheduled processing jobs
- Persistence layer
- Metrics and reliability enhancements

## Target Architecture

```text
External ISS API
→ Ingestion Service
→ Validation / Normalization
→ Event Store
→ Pass Detection / Scheduling
→ Notification Dispatch
→ Metrics / Logs / Health Checks
```

## Roadmap

### Foundation (Complete)
- [x] Service scaffold
- [x] Health endpoints
- [x] Config management
- [x] Lifecycle management
- [x] Request logging

### Next
- [ ] Build orbital event ingestion service
- [ ] Persist events and subscriptions
- [ ] Add scheduled background processing
- [ ] Add retry and timeout policies
- [ ] Expose metrics endpoint

## Engineering Focus

This project is intentionally built around five core concerns:

- Reliability — retries, timeouts, failure handling
- Observability — logging, metrics, operational visibility
- API Design — clean interfaces and service boundaries
- Background Processing — scheduled and asynchronous work
- Deployment — Dockerized, runnable, and portable

## Tech Stack

- Python
- FastAPI
- SQLite / Postgres (planned)
- Docker / Docker Compose
- External ISS pass APIs

## Purpose

Orbital Notify is being developed as a small but realistic backend system and portfolio case study for data/platform-oriented engineering work.

## License

MIT

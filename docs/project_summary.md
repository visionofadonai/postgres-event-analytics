# PostgreSQL Event Analytics Service

## Purpose

This project simulates a backend event analytics system designed to explore PostgreSQL performance, backend architecture, and operational concerns at larger data volumes.

## Key Technical Areas

- PostgreSQL schema design
- time-series partitioning
- async FastAPI backend development
- query optimization with EXPLAIN ANALYZE
- aggregation pipelines
- connection pooling
- Nginx/systemd deployment
- structured logging and observability

## Scale

Tested with approximately:
- 1,000,000 events

## Architecture Highlights

- async PostgreSQL access using asyncpg
- background aggregation jobs
- layered application structure
- partitioned event storage
- deployment behind Nginx reverse proxy

## Major Engineering Concepts Explored

- planning vs execution time
- partition pruning
- connection lifecycle management
- API hardening
- request tracing and logging
- operational reliability

## Outcome

The project evolved from a simple CRUD-style API into a more production-oriented backend service emphasizing scalability, maintainability, and observability.

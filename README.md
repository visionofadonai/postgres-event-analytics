# PostgreSQL Event Analytics Service

Production-style backend analytics system built with:

- PostgreSQL
- FastAPI
- asyncpg
- Nginx
- Ubuntu Server

Features explored include:
- time-series partitioning
- async backend architecture
- aggregation pipelines
- query optimization
- structured logging
- deployment automation

Tested with approximately:
- 1,000,000 events

# PostgreSQL Event Analytics Service

A backend project that simulates a production-style **event analytics pipeline** using PostgreSQL, FastAPI, and Python.

This project is designed to demonstrate practical backend and database engineering skills through a system that ingests events, stores them efficiently, exposes analytics endpoints, and explores performance tuning at scale.

---

## Project Overview

Modern applications generate large volumes of user activity data such as:

- page views
- clicks
- signups
- purchases

This project simulates a simplified event tracking platform and focuses on how that data is:

- ingested
- stored
- partitioned
- queried
- aggregated
- exposed through a backend API

The goal is to build something closer to a real engineering system than a tutorial project.

---

## Current Scale

This project has been tested with approximately:

- **1,000,000 events**

This larger dataset makes query planning, indexing, partitioning, and aggregation more meaningful.

---

## Architecture

```text
Event Generator Script
        │
        ▼
FastAPI Backend API
        │
        ▼
PostgreSQL Database
        │
        ├── Raw Event Storage
        ├── Time-Based Partitioning
        └── Aggregated Metrics Tables
        │
        ▼
Analytics Endpoints
```

## Screenshots

### API Documentation

![Swagger Docs](screenshots/swagger.png)

### Query Analysis

![Explain Analyze](screenshots/explain.png)

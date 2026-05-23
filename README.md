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
- 1,000,000 ticket lifecycle events

# PostgreSQL Event Analytics Service

A backend project that simulates a production-style **ticket lifecycle event analytics pipeline** using PostgreSQL, FastAPI, and Python.

This project is designed to demonstrate practical backend and database engineering skills through a system that ingests ticket lifecycle events, stores them efficiently, exposes analytics endpoints, and explores performance tuning at scale.

---

## Project Overview

Modern applications generate large volumes of user activity data such as:

- page views
- clicks
- signups
- purchases

This project simulates a simplified ticket lifecycle event tracking platform and focuses on how that data is:

- ingested
- stored
- partitioned
- queried
- aggregated
- exposed through a backend API

Building on top of a well tested analytics platform, this project adds:

- support to workflow metrics
- operational reporting 
- support ticket lifecycle events

---

## Current Scale

This project has been tested with approximately:

- **1,000,000 ticket lifecycle events**

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

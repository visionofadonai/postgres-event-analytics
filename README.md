# PostgreSQL Event Analytics Service

A small backend system that simulates a production-style **event analytics pipeline**.

This project demonstrates practical database engineering, backend development, and performance tuning using PostgreSQL and Python.

The goal is to showcase **real engineering practices** rather than tutorial-style code.

---

# Project Overview

Modern applications collect large volumes of user activity events such as:

* page views
* clicks
* signups
* purchases

These events must be stored efficiently and queried for analytics.

This project simulates a simplified **event tracking platform** similar to systems used in analytics products and SaaS platforms.

---

# Architecture

```
Event Generator Script
        │
        ▼
FastAPI Backend API
        │
        ▼
PostgreSQL Database
        │
        ▼
Analytics Queries / Metrics
```

Components:

| Component               | Technology    |
| ----------------------- | ------------- |
| API Framework           | FastAPI       |
| Database                | PostgreSQL    |
| Language                | Python        |
| Server OS               | Ubuntu Server |
| Development Environment | VirtualBox VM |
| Database Tooling        | pgAdmin       |

---

# Features

### Event ingestion

Events are stored with flexible metadata using JSONB.

Example event:

```json
{
  "user_id": "11111111-1111-1111-1111-111111111111",
  "event_type": "page_view",
  "properties": {
    "page": "/product/12",
    "value": 0.42
  }
}
```

---

### REST API

Endpoints currently implemented:

```
POST /events
GET /metrics/events-per-hour
GET /health
```

Example:

```bash
curl -X POST http://localhost:8000/events
```

---

### Analytics Queries

The system supports time-based aggregation queries such as:

* events per hour
* events per type
* activity over time

Example query:

```sql
SELECT date_trunc('hour', occurred_at), count(*)
FROM events
GROUP BY 1
ORDER BY 1;
```

---

# Database Schema

```
events
```

| column      | type        |
| ----------- | ----------- |
| event_id    | BIGSERIAL   |
| user_id     | UUID        |
| event_type  | TEXT        |
| properties  | JSONB       |
| occurred_at | TIMESTAMPTZ |

Indexes implemented:

```
(event_type, occurred_at)
GIN index on JSONB properties
```

These indexes support efficient filtering and analytics queries.

---

# Performance Analysis

Example analytics query tested with `EXPLAIN ANALYZE`.

Dataset size: ~100k rows.

Performance improvements were observed after adding indexes on time-based columns.

Performance analysis documentation is located in:

```
/perf/query_analysis.md
```

---

# Project Structure

```
postgres-event-analytics

app/
  api/
    events.py
  db.py
  main.py
  models.py

scripts/
  generate_events.py

sql/
  schema.sql

docs/
  architecture.md

perf/
  query_analysis.md
```

---

# Running the Project

Start the API server:

```
uvicorn app.main:app --reload
```

Generate synthetic events:

```
python scripts/generate_events.py
```

Test the API:

```
curl http://localhost:8000/health
```

---

# Skills Demonstrated

This project highlights practical engineering skills:

* PostgreSQL schema design
* indexing strategies
* query performance analysis
* Python API development
* Linux-based backend development
* system architecture documentation

---

# Future Improvements

Planned upgrades:

* table partitioning for large event datasets
* connection pooling
* background aggregation jobs
* query caching
* monitoring dashboards


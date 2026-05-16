# Demo Walkthrough

## 1. System overview
- explain architecture
- explain event ingestion flow

## 2. Generate events
Run:
python scripts/generate_events.py

## 3. Show PostgreSQL event growth
SELECT count(*) FROM events;

## 4. Show analytics endpoints
GET /metrics/events-per-hour
GET /metrics/events-by-type

## 5. Explain partitioning
Describe time-based event partitions.

## 6. Show EXPLAIN ANALYZE
Demonstrate indexed query performance.

## 7. Show deployment
- systemd service
- nginx reverse proxy
- health endpoint

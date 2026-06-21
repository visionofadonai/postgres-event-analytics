# Interview Walkthrough

## Problem

Build a backend system capable of handling large ticket lifecycle datasets.

## Solution

FastAPI backend
PostgreSQL storage
Partitioned event tables
Aggregation jobs
Async database access

## Scale

~1 million ticket lifecycle events

## Key Challenges

- query performance
- partition design
- async migration
- deployment

## Lessons Learned

- indexes affect planning and execution differently
- partitioning changes query behavior
- maintainability becomes critical as systems grow

Event Analytics Project — Learning Summary
Project Goal

Build a small backend system that demonstrates practical engineering skills in:

PostgreSQL database engineering

Python backend development

API design

query optimization and performance analysis

Linux deployment

The system simulates a simplified event analytics pipeline similar to what many real applications use to track user activity.

System Architecture

Current architecture:

Event Generator Script
        │
        ▼
FastAPI Backend API
        │
        ▼
PostgreSQL Database
        │
        ▼
Analytics Queries

Components:

Layer	Technology
Operating System	Ubuntu Server (VirtualBox VM)
Language	Python
API Framework	FastAPI
Database	PostgreSQL
DB Tools	psql / pgAdmin
Version Control	Git
Repository Hosting	GitHub
Development Access	SSH
What Has Been Implemented
1. Ubuntu VM development environment

You created a development environment using:

Ubuntu Server

VirtualBox

SSH remote access

This simulates how many backend services run on Linux servers.

Concepts involved:

Linux server management

SSH access

package installation via apt

Python environments

running backend services

2. PostgreSQL database setup

You installed and configured PostgreSQL and created a working database.

Database created:

event_analytics

Core table:

events

Schema:

column	type
event_id	BIGSERIAL
user_id	UUID
event_type	TEXT
properties	JSONB
occurred_at	TIMESTAMPTZ

Concepts involved:

relational schema design

primary keys

timestamps

semi-structured data using JSONB

Why JSONB matters:

Many event pipelines store dynamic metadata that changes frequently.

Example:

{
 "page": "/product/12",
 "value": 0.44
}

PostgreSQL's JSONB allows querying flexible event attributes.

3. Indexing for performance

Indexes were added to improve query performance.

Examples implemented:

(event_type, occurred_at)

and

GIN index on JSONB properties

Concepts involved:

B-tree indexes

composite indexes

JSONB GIN indexes

query filtering optimization

4. Query performance analysis

Queries were tested using:

EXPLAIN ANALYZE

Example query:

SELECT date_trunc('hour', occurred_at), count(*)
FROM events
GROUP BY 1
ORDER BY 1;

You observed:

planning time differences

execution time differences

Important learning:

Adding an index can increase planning time because PostgreSQL evaluates more possible execution plans.

However indexes can significantly reduce execution time, which is what matters for performance.

Concepts involved:

query planner

cost estimation

sequential scan vs index scan

planning vs execution time

5. Python event generator

You implemented a script that generates synthetic events.

Purpose:

simulate user activity

populate the database

create realistic workloads for analytics queries

Example event:

{
  "user_id": UUID,
  "event_type": "page_view",
  "properties": {...},
  "occurred_at": timestamp
}

Concepts involved:

batch inserts

random data generation

workload simulation

This is important because many real systems are tested with synthetic workloads.

6. FastAPI backend service

A REST API was created using FastAPI.

Main application file:

app/main.py

Endpoints implemented:

GET /health
POST /events
GET /metrics/events-per-hour
GET /metrics/events-by-type

Concepts involved:

REST API design

request validation using Pydantic

JSON APIs

routing

backend service architecture

7. Database interaction layer

The API interacts with PostgreSQL using:

psycopg2

This layer handles:

database connections

executing queries

inserting events

Concepts involved:

database drivers

connection management

parameterized SQL queries

8. Git and GitHub integration

You initialized a Git repository and pushed the project to GitHub.

Concepts involved:

version control

commit history

repository structure

GitHub project visibility

Git commits now track the evolution of the system.

9. Documentation and project structure

You organized the repository into logical components:

app/
scripts/
sql/
docs/
perf/

This structure resembles how production backend repositories are organized.

Concepts involved:

modular code organization

documentation practices

reproducible project setup

What Engineering Skills This Demonstrates

Your project now demonstrates practical experience with:

Database engineering

schema design

indexing

query performance analysis

Backend development

REST API design

Python backend services

System architecture

event ingestion pipelines

analytics query patterns

Software engineering

Git workflows

documentation

structured repositories

Infrastructure basics

Linux server environments

SSH-based development

What To Study More Deeply

These topics will make this project much stronger.

PostgreSQL

Focus on:

index types

query planner

VACUUM and ANALYZE

table partitioning

connection pooling

transaction isolation

Recommended study topics:

PostgreSQL execution plans
PostgreSQL partitioned tables
PostgreSQL JSONB querying
Backend architecture

Focus on:

API architecture

dependency injection

background jobs

connection pools

async database access

Topics:

FastAPI async architecture
SQLAlchemy
connection pooling
Data systems

This project resembles simplified versions of systems used for:

event tracking

analytics pipelines

logging systems

telemetry collection

Understanding real systems like:

Segment
Snowplow
ClickHouse
Kafka pipelines

will deepen your understanding.

What the System Can Do Right Now

Current capabilities:

ingest events via API

generate synthetic workload

store events in PostgreSQL

query analytics metrics

measure query performance

This represents a basic event analytics service.

Key Learning Outcome

The most important takeaway so far:

You have moved from:

IT support environment

to building:

a working backend data system

That transition — from operating systems to building systems — is the key step toward backend or data engineering roles.

Next Major Technical Upgrade

The next improvement that will dramatically increase your understanding is:

PostgreSQL time-partitioned tables

This is commonly used for:

analytics pipelines

logging systems

telemetry platforms

Learning this will deepen your understanding of:

large datasets

storage design

query optimization

data lifecycle management

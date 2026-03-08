# PostgreSQL Event Analytics Service (Portfolio Project)

## Project Goal

Build a production-style backend system that demonstrates practical
PostgreSQL engineering, Python backend development, and Linux deployment
skills.

This project simulates an **event analytics platform** similar to
systems used in real products to track user behavior.

The goal is to demonstrate:

-   PostgreSQL schema design
-   Indexing strategies
-   Query optimization using EXPLAIN ANALYZE
-   Python API development (FastAPI)
-   Backend architecture patterns
-   Linux service deployment using Nginx
-   Professional documentation suitable for recruiters

This project is designed to be completed over **12 weeks of part‑time
work (evenings/weekends)**.

------------------------------------------------------------------------

# System Architecture

Client / Event Generator \| v FastAPI Application (Python) \| v
PostgreSQL Database \| v Aggregated Metrics Tables \| v Nginx Reverse
Proxy

------------------------------------------------------------------------

# Core Features

### Event ingestion

Application receives simulated events such as:

-   page_view
-   click
-   signup
-   purchase

### Queryable API

Example endpoints:

POST /events\
GET /events\
GET /metrics

### Data engineering components

-   Time-series event storage
-   Partitioned PostgreSQL tables
-   JSONB event properties
-   Query optimization
-   Aggregated analytics tables

------------------------------------------------------------------------

# Technology Stack

  Layer             Technology
  ----------------- ---------------
  OS                Ubuntu Server
  Database          PostgreSQL
  Backend           Python
  API Framework     FastAPI
  Reverse Proxy     Nginx
  DB Management     pgAdmin
  Version Control   Git + GitHub

------------------------------------------------------------------------

# Database Schema (Concept)

events

  column        type
  ------------- -------------
  event_id      BIGSERIAL
  user_id       UUID
  event_type    TEXT
  properties    JSONB
  occurred_at   TIMESTAMPTZ

Indexes to implement later:

-   event_type + occurred_at
-   partial index on purchase events
-   GIN index on JSONB properties

------------------------------------------------------------------------

# 12 Week Milestone Plan

## Week 1 --- Project Initialization

Deliverables:

-   GitHub repository created
-   README committed
-   SSH access confirmed
-   PostgreSQL connection verified

Tasks:

-   install git
-   create project folder
-   create python virtual environment
-   connect to postgres using psql
-   confirm pgadmin connection

------------------------------------------------------------------------

## Week 2 --- Database Design

Deliverables:

-   SQL schema file committed
-   events table created

Tasks:

-   design event schema
-   create SQL migration script
-   test inserts manually
-   add initial indexes

------------------------------------------------------------------------

## Week 3 --- Data Generator

Deliverables:

-   Python script generating synthetic events

Tasks:

-   generate fake user IDs
-   randomly create events
-   insert into PostgreSQL
-   verify row growth

------------------------------------------------------------------------

## Week 4 --- Query Exploration

Deliverables:

-   example query scripts

Tasks:

-   write queries for:
    -   events by type
    -   events by user
    -   events by time window
-   run EXPLAIN ANALYZE
-   record performance notes

------------------------------------------------------------------------

## Week 5 --- FastAPI Setup

Deliverables:

-   FastAPI server running locally

Tasks:

-   install fastapi
-   install uvicorn
-   build first endpoint

GET /health

------------------------------------------------------------------------

## Week 6 --- Event API

Deliverables:

API endpoints:

POST /events\
GET /events

Tasks:

-   integrate PostgreSQL connection
-   insert events via API
-   query events

------------------------------------------------------------------------

## Week 7 --- Metrics Queries

Deliverables:

analytics queries

Examples:

-   events per hour
-   active users per day
-   purchases per day

------------------------------------------------------------------------

## Week 8 --- Aggregated Tables

Deliverables:

metrics table or materialized view

Tasks:

-   create daily metrics table
-   write aggregation SQL
-   refresh metrics script

------------------------------------------------------------------------

## Week 9 --- Query Optimization

Deliverables:

performance report

Tasks:

-   analyze slow queries
-   add indexes
-   compare EXPLAIN output

------------------------------------------------------------------------

## Week 10 --- Nginx Deployment

Deliverables:

FastAPI running behind nginx

Tasks:

-   install nginx
-   configure reverse proxy
-   expose API endpoint

------------------------------------------------------------------------

## Week 11 --- Documentation

Deliverables:

-   architecture diagram
-   performance tuning notes
-   API documentation

------------------------------------------------------------------------

## Week 12 --- Portfolio Polish

Deliverables:

-   clean repository
-   recruiter‑friendly README
-   demo recording

------------------------------------------------------------------------

# Project Folder Structure

project-root

app/ api.py db.py models.py

scripts/ generate_events.py

sql/ schema.sql queries.sql

docs/ architecture.md performance.md

README.md

------------------------------------------------------------------------

# How Recruiters Should Evaluate This Project

This repository demonstrates:

-   relational data modeling
-   PostgreSQL performance tuning
-   backend API design
-   Linux deployment skills
-   production-style documentation

------------------------------------------------------------------------

# Next Improvements (Future Work)

-   table partitioning
-   connection pooling
-   async database queries
-   monitoring dashboards
-   load testing

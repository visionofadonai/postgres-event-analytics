**********************
EXPERIMENT 1 — Index vs No Index
**********************
Analysis for following analysis at 1 Million rows
EXPLAIN ANALYZE
SELECT count(*)
FROM events
WHERE event_type = 'page_view';

RESULTS:
Scan Type: No Index
Planning Time: 0.691 ms
Execution Time: 66.282 ms

Scan Type: Index added on event_type
Planning Time: 2.079 ms
Execution Time: 40.128 ms

======

Analysis for following analysis at 1 Million rows
SELECT count(*)
FROM events
WHERE event_type = 'page_view'
AND date(occurred_at) = '2026-03-12'

RESULTS:
Scan Type: Composite Index - No Index
Planning Time: 1.476 ms
Execution Time: 112.313  ms

Scan Type: Composite Index - Index added
Planning Time: 1.423 ms
Execution Time: 73.800 ms


**********************
EXPERIMENT 2 — JSONB Query Performance
**********************

EXPLAIN ANALYZE
SELECT *
FROM events
WHERE properties->>'page' = '/product/12';

RESULTS:
Scan Type: No Index
Planning Time: 0.110 ms
Execution Time: 230.415 ms

Scan Type: GIN Index (18.626s)
Planning Time: 0.456 ms / 0.199 ms
Execution Time: 168.522 ms / 147.862 ms

Scan Type: Expression Index (2.464s)
Planning Time: 1.375 ms / 0.274 ms
Execution Time: 89.913 ms / 51.852 ms


**********************
Experiment 3 — Query Planner Behavior
**********************

Explain Analyze
SELECT *
FROM events
WHERE (properties->>'value') > '0.5'

RESULTS:
Scan Type: No Expression Index
Planning Time: 0.204 ms
Execution Time: 476.237 ms

Scan Type: No Expression Index + SeqScan OFF
Planning Time: 0.177
Execution Time: 394.427 ms

Scan Type: With Expression Index (6.880s)
Planning Time: 2.064 ms
Execution Time: 215.525 ms

Scan Type: With Expression Index + SeqScan OFF
Planning Time: 0.205 ms 
Execution Time: 237.210 ms

****
Experiment 3 extended queries
****

EXPLAIN ANALYZE
SELECT *
FROM events
WHERE event_id > 40000;

RESULTS:
Scan Type: No Index   
Planning Time: 0.207 ms
Execution Time: 147.845 ms

Scan Type: No Index + SeqScan OFF
Planning Time: 0.333 ms
Execution Time: 872.873 ms

Scan Type: Index 
Planning Time: 0.162 ms / 0.355 ms
Execution Time: 154.841 ms / 169.259 ms

Scan Type: Index + SeqScan OFF
Planning Time: 7.769 ms / 0.709 ms
Execution Time: 229.036 ms / 217.237 ms




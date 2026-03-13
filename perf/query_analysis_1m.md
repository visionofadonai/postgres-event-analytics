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




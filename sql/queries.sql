-- baseline query
EXPLAIN ANALYZE
SELECT event_type, count(*) FROM events
WHERE occurred_at >= now() - interval '1 day'
GROUP BY event_type;

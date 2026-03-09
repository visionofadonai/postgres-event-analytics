EXPLAIN ANALYZE
SELECT date_trunc('hour', occurred_at), count(*)
FROM events
GROUP BY 1
ORDER BY 1;

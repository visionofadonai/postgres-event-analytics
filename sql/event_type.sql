EXPLAIN ANALYZE
SELECT count(*)
FROM events
WHERE event_type = 'page_view'
and date(occurred_at) = '2026-03-12'


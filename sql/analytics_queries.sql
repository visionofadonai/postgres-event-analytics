-- events per hour
SELECT date_trunc('hour', occurred_at) AS hour,
       count(*)
FROM events
GROUP BY hour
ORDER BY hour;

-- events per type
SELECT event_type,
       count(*)
FROM events
GROUP BY event_type
ORDER BY count DESC;

-- activity in last 24 hours
SELECT count(*)
FROM events
WHERE occurred_at > now() - interval '24 hours';

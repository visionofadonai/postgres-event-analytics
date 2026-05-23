SELECT status, count(*)
FROM tickets
GROUP BY status;

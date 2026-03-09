Query: events per hour aggregation

Dataset size: 100k rows

EXPLAIN ANALYZE results:

Before index:
Planning Time: 0.23 ms
Execution Time: 120 ms

After index (occurred_at):
Planning Time: 0.45 ms
Execution Time: 14 ms

Conclusion:
Index significantly reduced execution time for time-window queries.

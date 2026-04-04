Migrated events_per_hour endpoint to asyncpg.

Observed:
- improved concurrency
- reduced blocking
- cleaner async query execution

Difference:
psycopg2 → synchronous
asyncpg → non-blocking

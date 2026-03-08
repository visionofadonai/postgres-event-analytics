                                                  QUERY PLAN                                                   
---------------------------------------------------------------------------------------------------------------
 HashAggregate  (cost=382.00..382.04 rows=4 width=15) (actual time=4.842..4.844 rows=4 loops=1)
   Group Key: event_type
   Batches: 1  Memory Usage: 24kB
   ->  Seq Scan on events  (cost=0.00..332.00 rows=9999 width=7) (actual time=0.014..2.827 rows=10000 loops=1)
         Filter: (occurred_at >= (now() - '1 day'::interval))
 Planning Time: 1.294 ms
 Execution Time: 4.940 ms
(7 rows)

                                                  QUERY PLAN                                                   
---------------------------------------------------------------------------------------------------------------
 HashAggregate  (cost=382.00..382.04 rows=4 width=15) (actual time=4.490..4.492 rows=4 loops=1)
   Group Key: event_type
   Batches: 1  Memory Usage: 24kB
   ->  Seq Scan on events  (cost=0.00..332.00 rows=9999 width=7) (actual time=0.014..2.730 rows=10000 loops=1)
         Filter: (occurred_at >= (now() - '1 day'::interval))
 Planning Time: 1.395 ms
 Execution Time: 4.587 ms
(7 rows)


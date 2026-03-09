                                                    QUERY PLAN                                                     
-------------------------------------------------------------------------------------------------------------------
 HashAggregate  (cost=4143.96..4144.00 rows=4 width=15) (actual time=46.189..46.191 rows=4 loops=1)
   Group Key: event_type
   Batches: 1  Memory Usage: 24kB
   ->  Seq Scan on events  (cost=0.00..3644.09 rows=99975 width=7) (actual time=0.224..28.114 rows=100003 loops=1)
         Filter: (occurred_at >= (now() - '1 day'::interval))
         Rows Removed by Filter: 10002
 Planning Time: 1.498 ms
 Execution Time: 46.319 ms
(8 rows)

                                                        QUERY PLAN                                                        
--------------------------------------------------------------------------------------------------------------------------
 GroupAggregate  (cost=12305.45..14505.55 rows=110005 width=16) (actual time=38.073..49.307 rows=3 loops=1)
   Group Key: (date_trunc('hour'::text, occurred_at))
   ->  Sort  (cost=12305.45..12580.46 rows=110005 width=8) (actual time=36.876..41.716 rows=110005 loops=1)
         Sort Key: (date_trunc('hour'::text, occurred_at))
         Sort Method: quicksort  Memory: 3073kB
         ->  Seq Scan on events  (cost=0.00..3094.06 rows=110005 width=8) (actual time=0.021..29.897 rows=110005 loops=1)
 Planning Time: 0.630 ms
 Execution Time: 49.590 ms
(8 rows)


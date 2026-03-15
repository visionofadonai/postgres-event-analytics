CREATE TABLE IF NOT EXISTS events
(
    event_id bigint NOT NULL,
    user_id uuid NOT NULL,
    event_type text COLLATE pg_catalog."default" NOT NULL,
    properties jsonb,
    occurred_at timestamp with time zone DEFAULT now()
) PARTITION BY RANGE (((occurred_at AT TIME ZONE 'UTC')::date));

CREATE TABLE public.events_1 PARTITION OF public.events
    FOR VALUES FROM ('2026-01-01') TO ('2026-02-01')
TABLESPACE pg_default;

CREATE TABLE public.events_2 PARTITION OF public.events
    FOR VALUES FROM ('2026-02-01') TO ('2026-03-01')
TABLESPACE pg_default;

CREATE TABLE public.events_3 PARTITION OF public.events
    FOR VALUES FROM ('2026-03-01') TO ('2026-04-01')
TABLESPACE pg_default;

CREATE TABLE public.events_4 PARTITION OF public.events
    FOR VALUES FROM ('2026-04-01') TO ('2026-05-01')
TABLESPACE pg_default;

CREATE TABLE public.events_5 PARTITION OF public.events
    FOR VALUES FROM ('2026-05-01') TO ('2026-06-01')
TABLESPACE pg_default;

CREATE TABLE public.events_6 PARTITION OF public.events
    FOR VALUES FROM ('2026-06-01') TO ('2026-07-01')
TABLESPACE pg_default;

CREATE INDEX IF NOT EXISTS event_id_idx
    ON events USING btree (event_id ASC NULLS LAST);

CREATE INDEX IF NOT EXISTS exp_propertiespage_idx
    ON events USING btree ((properties ->> 'page'::text) COLLATE pg_catalog."default" ASC NULLS LAST);

CREATE INDEX IF NOT EXISTS exp_propertiesvalue_idx
    ON events USING btree ((properties ->> 'value'::text) COLLATE pg_catalog."default" ASC NULLS LAST);

CREATE INDEX IF NOT EXISTS idx_event_type
    ON events USING btree (event_type COLLATE pg_catalog."default" ASC NULLS LAST);

CREATE INDEX IF NOT EXISTS idx_event_type_time
    ON events USING btree (event_type COLLATE pg_catalog."default" ASC NULLS LAST, occurred_at ASC NULLS LAST);

CREATE INDEX IF NOT EXISTS idx_events_occurred_at
    ON events USING btree (occurred_at ASC NULLS LAST);

CREATE INDEX IF NOT EXISTS idx_properties_gin
    ON events USING gin (properties);

CREATE INDEX IF NOT EXISTS idx_purchase_time
    ON events USING btree (occurred_at ASC NULLS LAST)
    WHERE event_type = 'purchase'::text;



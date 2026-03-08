CREATE TABLE events (
    event_id BIGSERIAL PRIMARY KEY,
    user_id UUID NOT NULL,
    event_type TEXT NOT NULL,
    properties JSONB,
    occurred_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_event_type_time
ON events(event_type, occurred_at);

CREATE INDEX idx_properties_gin
ON events USING GIN(properties);

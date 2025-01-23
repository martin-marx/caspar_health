--Scripts to migrate tables to the DB
CREATE TABLE patients (
    patient_id INTEGER,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    country VARCHAR(255),
    processing_date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE exercises (
    id BIGINT,
    external_id INTEGER,
    minutes INTEGER,
    completed_at TIMESTAMPTZ,
    updated_at TIMESTAMPTZ
);

CREATE TABLE steps (
    id BIGINT,
    external_id INTEGER,
    steps INTEGER,
    submission_time TIMESTAMPTZ,
    updated_at TIMESTAMPTZ
);
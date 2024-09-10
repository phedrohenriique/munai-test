
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE IF NOT EXISTS
  munai.public.patients (
    patient_uuid uuid PRIMARY KEY NOT NULL DEFAULT uuid_generate_v4 (),
    created_at timestamp without time zone NOT NULL DEFAULT now(),
    patient_name character varying (60) NULL,
    updated_at timestamp without time zone NULL
  );
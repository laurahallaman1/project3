-- Table: public.freedom_idx_2019

DROP TABLE public.freedom_idx_2019;

CREATE TABLE public.freedom_idx_2019
(
    iso_code character varying COLLATE pg_catalog."default" NOT NULL,
    year integer NOT NULL,
    country character varying COLLATE pg_catalog."default" NOT NULL,
    region character varying COLLATE pg_catalog."default" NOT NULL,
    hf_score numeric,
    hf_rank numeric,
    hf_quartile integer,
    CONSTRAINT freedom_idx_2019_pkey PRIMARY KEY (iso_code, year)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.freedom_idx_2019
    OWNER to postgres;
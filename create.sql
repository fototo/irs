
CREATE TABLE irs_nonprofit (
    url character varying(1200),
    filename character varying(100) NOT NULL,
    doctype character varying(100),
    year character varying(100),
    idstr character varying(100),
    text character varying(1200),
    formtype character varying(100),
    date character varying(100),
    size character varying(100),
    assetts numeric(20,2),
    hashstr character varying(1200),
    md5 character varying(1200),
    body_tsv tsvector
);



CREATE INDEX irs_nonprofit_filename_idx ON irs_nonprofit USING btree (filename);

CREATE INDEX irs_nonprofit_tsv ON irs_nonprofit USING gin (body_tsv);

CREATE TRIGGER irs_nonprofit_tsvectorupdate BEFORE INSERT OR UPDATE ON irs_nonprofit FOR EACH ROW EXECUTE PROCEDURE tsvector_update_trigger('tsv_body', 'pg_catalog.english', 'text');



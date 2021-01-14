CREATE SCHEMA AccessLog;

CREATE TABLE AccessLog.Log (
    id          BIGSERIAL   PRIMARY KEY NOT NULL,
    level       VARCHAR(16),
    ts          TIMESTAMP               NOT NULL,
    remote_addr INET                    NOT NULL,
    remote_port SMALLINT                NOT NULL,
    method      VARCHAR(8),
    path        TEXT,
    query       TEXT,
    duration    REAL,
    size        INTEGER,
    status      SMALLINT
);

CREATE INDEX ts_index ON AccessLog.Log (ts);

CREATE USER grafanareader WITH PASSWORD 'NuM28hvDYohFNGciWxKz';
GRANT USAGE ON SCHEMA AccessLog TO grafanareader;
GRANT SELECT ON AccessLog.Log TO grafanareader;

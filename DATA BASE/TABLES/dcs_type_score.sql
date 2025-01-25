-- =========================================
-- R15-Concepto de notas por curso
-- =========================================
CREATE TABLE dcs_type_score (
    id serial primary key,
    score_name      varchar(20)   not null,
    score_desc      varchar(255)  not null,
    score_fecini    timestamp     not null,
    score_fecfin    timestamp     not null,

    -- Columnas de control
    us_creation_date timestamp      default current_timestamp,
    us_creation_user varchar(15)    default 'user.test',
    us_update_date   timestamp      default current_timestamp,
    us_update_user   varchar(15)    default 'user.test'
)
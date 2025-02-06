-- =========================================
--  Table of labels general
-- =========================================
CREATE TABLE sett_general_label(
    code_lab        VARCHAR(255)    NOT NULL,
    language_lab    CHAR(2)         NOT NULL,
    description_lab VARCHAR(255)    NOT NULL,
    width_lab       INT,
    heigth_lab      INT,

    -- Columnas de control 
    us_creation_date timestamp      default current_timestamp, 
    us_creation_user varchar(15)    default 'user.test',
    us_update_date   timestamp      default current_timestamp,
    us_update_user   varchar(15)    default 'user.test',
    PRIMARY KEY (code_lab, language_lab)
)
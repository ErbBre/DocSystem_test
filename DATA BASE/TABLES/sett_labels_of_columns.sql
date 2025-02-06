-- =========================================
--  Table of label's columns in diferente languages
-- =========================================
CREATE TABLE sett_labels_of_columns(
    tabname             varchar(255) NOT NULL,
    colname             varchar(255) NOT NULL,
    language_code       CHAR(2)      NOT NULL,
    col_description     VARCHAR(255) NOT NULL,
    width               INT,
    heigth              INT,

    -- Columnas de control 
    us_creation_date timestamp      default current_timestamp, 
    us_creation_user varchar(15)    default 'user.test',
    us_update_date   timestamp      default current_timestamp,
    us_update_user   varchar(15)    default 'user.test',

    PRIMARY KEY (tabname, colname, language_code)
)
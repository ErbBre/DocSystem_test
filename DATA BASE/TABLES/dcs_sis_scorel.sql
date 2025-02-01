-- =========================================
-- R13- Sistema de calificaciones lineas
-- =========================================

/*Columnas:

linid autoincrementable PK
headid ( id de la cabecera dcs_sis_scoreh) llave foranea
nombre - puede ser nulo
descripción - puede ser nulo
valor de inicio del rango (campo decimal) no nulo
valor final del rango (campo decimal) no nulo

*/
CREATE TABLE dcs_sis_scorel (
    linid               SERIAL          PRIMARY     KEY,
    headid              INT             NOT NULL,
    scr_name            VARCHAR(50),
    scr_description     VARCHAR(100),
    scr_ini             DECIMAL(10,2)   NOT NULL,
    scr_fin             DECIMAL(10,2)   NOT NULL,

    -- Foreign keys
    foreign key (headid) references dcs_sis_scoreh(cabid) 
)
-- =========================================
-- R9-Tabla registro de sesiones
-- =========================================

CREATE TABLE dcs_sesions(
    id              serial primary key,                 -- PK
    id_user         int         not null,               -- id del usuario
    id_key_access   int         not null,               -- id de la llave de acceso
    ip_adress       varchar(40),                        -- ip del dispositivo desde donde se conecto
    sesion_start    timestamp,                           -- Fecha de inicio de sesion
    sesion_end      timestamp,                           -- Fecha de cuando perdio la conexión o cerró sesion

    -- Columnas de control 
    us_creation_date    timestamp   default current_timestamp, 
    us_creation_user    varchar(15) default 'user.test',
    us_update_date      timestamp   default current_timestamp,
    us_update_user      varchar(15) default 'user.test',

    -- Check de fecha final mayor que fecha inicial
    check(sesion_start > sesion_end),

    -- Foreign keys
    foreign key (id_user) references dcs_user_access_system(id),
    foreign key (id_key_access) references dcs_key_access_log(id)
    
)

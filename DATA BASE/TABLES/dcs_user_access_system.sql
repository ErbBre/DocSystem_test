-- =========================================
-- R1-Tabla datos personales de maestros(profesores)
-- =========================================

CREATE TABLE dcs_user_access_system(
    id                  serial primary key,                          
    names               varchar(45)     not null,               -- Nombres
    last_names          varchar(45)     not null,               -- Apellidos
    identific           varchar(20)     not null,               -- DNI en el caso de peru
    age_naciment        date            not null,               -- Fecha de nacimiento
    us_email            varchar(100)    not null    unique,     -- Email
    gender              varchar(1)      not null,               -- genero
    phone               varchar(20),                            -- Telefono
    user_adress         varchar(255),                           -- Direccion del usuario(profesor)
    acount_status       varchar(1)      not null,               -- estado

    -- Columnas de control 
    us_creation_date    timestamp   default current_timestamp, 
    us_creation_user    varchar(15) default 'user.test',
    us_update_date      timestamp   default current_timestamp,
    us_update_user      varchar(15) default 'user.test',
    
    -- Check genero: M masculino, F femenino, X prefiero no decirlo
    check(gender in('M', 'F', 'X')),
    -- Estado del estudiante: E enabled, D disabled
    check(acount_status in('E', 'D'))
);
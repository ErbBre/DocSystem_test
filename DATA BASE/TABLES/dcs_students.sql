-- =========================================
--  Ticket R4-Tabla estudiantes
-- =========================================
create table dcs_students (
    id                  serial primary key,               -- llave primaria
    stud_name           varchar(50)     not null,         -- nombres
    stud_last_name      varchar(50)     not null,         -- apellidos
    stud_identific      varchar(20)     not null unique,   -- DNI para Perú 
    stud_age_naciment   date            not null,         -- fecha de nacimiento
    stud_gender         varchar(1)      not null,         -- genero
    stud_email          varchar(100)    not null unique,  -- correo electronico
    stud_address        varchar(100),                     -- direccion de residencia
    stud_status         varchar(1)      not null,         -- estado

    -- Columnas de control 
    us_creation_date    timestamp   default current_timestamp, 
    us_creation_user    varchar(15) default 'user.test',
    us_update_date      timestamp   default current_timestamp,
    us_update_user      varchar(15) default 'user.test',

    -- Check genero: M masculino, F femenino, X prefiero no decirlo
    check(stud_gender in('M', 'F', 'X')),
    -- Estado del estudiante: E enabled, D disabled
    check(stud_status in('E', 'D'))
);
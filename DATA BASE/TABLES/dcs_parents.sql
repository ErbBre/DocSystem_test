-- =========================================
--Ticket R5-Tabla apoderados
-- =========================================
create table dcs_parents (
    id              serial primary key,                 -- id campo autoincrementable y llave primaria
    names           varchar(50)     not null,           -- nombres - obligatorio (not null)
    last_names      varchar(50)     not null,           -- apellidos - obligatorio
    age_naciment    date            not null,           -- fecha de nacimiento
    gender          varchar(1)      not null ,          -- genero (M, F, X)
    ocupation       int,                                -- Va a hacer referencia a su tabla dcs_ocupations
    phone           varchar(20),                        -- telefono
    email           varchar(100)    not null unique,    -- correo electronico - campo unico
    adress          varchar(100),                       -- direccion de residencia
    id_state        CHAR(1)         not null ,          -- estado (E, D) enabled , disabled

    -- Columnas de control

    us_creation_date timestamp      default current_timestamp, 
    us_creation_user varchar(15)    default 'user.test',
    us_update_date   timestamp      default current_timestamp,
    us_update_user   varchar(15)    default 'user.test'
    
    -- Check genero: M masculino, F femenino, X prefiero no decirlo
    check (gender in('M', 'F', 'X')),
    -- Estado del estudiante: E enabled, D disabled
    check (id_state IN ('E', 'D'))
);
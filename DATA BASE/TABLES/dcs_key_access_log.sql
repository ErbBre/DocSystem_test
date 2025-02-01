-- =========================================
-- R2-Tabla de credenciales de acceso
-- =========================================

CREATE TABLE dcs_key_access_log (
    id               serial primary key,
    id_user          int                not null,
    us_user          varchar(15)        not null,
    us_passw         varchar(20)        not null,
    us_state         char(1)            not null,
    
    -- Columnas de control
    us_creation_date timestamp      default current_timestamp,
    us_creation_user varchar(15)    default 'user.test',
    us_update_date   timestamp      default current_timestamp,
    us_update_user   varchar(15)    default 'user.test',
    
    -- Check estado de curso (enabled, disabled)
    check(us_state in ('E','D') ),

    -- Foreigns key - hace al usuario que
    foreign key (id_user) references dcs_user_access_system(id)

);
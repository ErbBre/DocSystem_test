-- =========================================
-- Ticket R7 Tabla de Grados academicos
-- =========================================

-- =========================================
-- Ticket R7 Tabla de Grados academicos
-- =========================================

create table dcs_degree(
    id                  int primary key,         -- llave primaria
    name_degree         varchar(50)  not null,   -- nombre del grado
    description_degree  varchar(255) not null,   -- descripción del grado
    degree_state        CHAR(1),                 -- Estado del grado
    -- Columnas de control 
    us_creation_date    timestamp   default current_timestamp, 
    us_creation_user    varchar(15) default 'user.test',
    us_update_date      timestamp   default current_timestamp,
    us_update_user      varchar(15) default 'user.test',

    -- Check estado de curso (enabled, disabled)
    check(degree_state in('E', 'D'))
)
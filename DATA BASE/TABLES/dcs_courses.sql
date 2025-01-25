-- =========================================
-- Ticket R8 Tabla cursos
-- =========================================

create table dcs_courses(
    id                  int primary key,                          -- Primary key
    id_degree           int          not null,                    -- Grado al que pertenece el curso
    name_degree         varchar(50) not null,                     -- nombre del curso
    description_degree  varchar(255) not null,                    -- descripcion del curso
    degree_start_date   date         not null,                     -- fecha de inicio
    degree_end_date     date         not null,                     -- fecha de fin de curso
    type_system_score   int          not null,
    degree_status       varchar(1)   not null, 

    -- Columnas de control 

    us_creation_date timestamp      default current_timestamp, 
    us_creation_user varchar(15)    default 'user.test',
    us_update_date   timestamp      default current_timestamp,
    us_update_user   varchar(15)    default 'user.test',
    
    -- Check estado de curso (enabled, disabled)
    check(degree_status in('E', 'D')),

    -- Foreigns key - hace referencia al grado al que pertence el curso
    foreign key (id_degree) references dcs_degree(id),

    -- Foreigns key - hace referencia al grado al que pertence el curso
    foreign key (type_system_score) references dcs_sis_scoreh(cabid)
)
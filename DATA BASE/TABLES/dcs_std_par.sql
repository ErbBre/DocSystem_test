-- =========================================
-- R10-Tabla intermedia students-parents
-- =========================================
create table dcs_std_par(
    id          serial primary key,             -- PK
    id_student  int not null,                   -- id del estudiante
    id_parent   int not null,                   -- id del apoderado o padre de familia
    
    -- Columnas de control
    us_creation_date timestamp      default current_timestamp,
    us_creation_user varchar(15)    default 'user.test',
    us_update_date   timestamp      default current_timestamp,
    us_update_user   varchar(15)    default 'user.test',

    foreign key (id_student) references dcs_students(id),
    foreign key (id_parent) references dcs_parents(id)   
);
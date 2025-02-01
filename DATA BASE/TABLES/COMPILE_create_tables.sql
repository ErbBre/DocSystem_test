-- =========================================
-- Ticket DCS-6 R3-división territorial-Paises
-- =========================================

create table dcs_country(
    id_country      serial primary key,
    cod_chartwo     char(2),
    cod_charthree   char(3),
    cod_num         smallint,
    nom_corto       varchar(25),
    nom_largo       varchar(50),
    id_capital      int
);

-- =========================================
-- Ticket R6-Tabla de ocupaciones
-- =========================================

create table dcs_ocupations (
    id serial primary key,               -- autoincrementable
    name_ocupation varchar(50) not null, -- Nombre de la profesion u ocupación
    descript varchar(100)                -- Descripcion
);

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

-- =========================================
-- R2-Tabla de credenciales de acceso
-- =========================================

CREATE TABLE dcs_key_access_log (
    id               serial primary key not null,
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
    foreign key (id) references dcs_user_access_system(id)

);

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
    
);

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
);

-- =========================================
-- Ticket R8 Tabla cursos
-- =========================================

create table dcs_courses(
    id                  int primary key,                          -- Primary key
    id_degree           int          not null,                    -- Grado al que pertenece el curso
    name_degree         varchar(50) not null,                     -- nombre del curso
    description_degree  varchar(255) not null,                    -- descripcion del curso
    degree_start_date   date         not null,                    -- fecha de inicio
    degree_end_date     date         not null,                    -- fecha de fin de curso
    degree_status       varchar(1)   not null, 

    -- Columnas de control 

    us_creation_date timestamp      default current_timestamp, 
    us_creation_user varchar(15)    default 'user.test',
    us_update_date   timestamp      default current_timestamp,
    us_update_user   varchar(15)    default 'user.test',
    
    -- Check estado de curso (enabled, disabled)
    check(degree_status in('E', 'D')),

    -- Foreigns key - hace referencia al grado al que pertence el curso
    foreign key (id_degree) references dcs_degree(id)
);

-- =========================================
-- R15-Concepto de notas por curso
-- =========================================
CREATE TABLE dcs_type_score (
    id serial primary key,
    score_name      varchar(20)   not null,
    score_desc      varchar(255)  not null,
    score_fecini    timestamp     not null,
    score_fecfin    timestamp     not null,

    -- Columnas de control
    us_creation_date timestamp      default current_timestamp,
    us_creation_user varchar(15)    default 'user.test',
    us_update_date   timestamp      default current_timestamp,
    us_update_user   varchar(15)    default 'user.test'
);

create table dcs_score(
    id                  serial          primary     key,  -- id autoincrementable
    id_type_concept     int             not null,         -- id_type_concept - llave foranea de la tabla dcs_type_score (de esta
    number_score        decimal(3,2)    not null,         -- valor decimal de la nota asignada, se valida con el sistema de calificaciones asignado al curso para comprobar que este dentro de algun rango establecido en alguna linea)

    -- Columnas de control 

    us_creation_date    timestamp       default     current_timestamp,
    us_creation_user    varchar(15)     default     'user.test',
    us_update_date      timestamp       default     current_timestamp,
    us_update_user      varchar(15)     default     'user.test',

    -- Foreign keys
    foreign key (id_type_concept) references dcs_type_score(id) 
)
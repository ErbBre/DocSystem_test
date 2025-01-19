-- Ticket R8 Tabla cursos
/*Columnas:

id autoincrementable llave primaria
id del grado (llave foranea que hace referencia a id de la tabla dcs_degree, para esto dcs_degree ya debe estar creada) - numerico no autoincrementable
nombre del curso
descripcion del curso
fecha de inicio
fecha de fin de curso
estado de curso (enabled, disabled)
Columnas de control*/

create table dcs_courses(
    id int primary key,                                                  -- autoincrementable
    id_degree int not null,                                              -- llave foranea
    name_degree varchar(255) not null,                                   -- nombre del curso
    description_degree varchar(255) not null,                            -- descripcion del curso
    degree_start_date date not null,                                     -- fecha de inicio
    degree_end_date date not null,                                       -- fecha de fin de curso
    degree_status varchar(1) not null check(degree_status in('E', 'D')), -- estado de curso (enabled, disabled)

    -- Columnas de control 

    us_creation_date timestamp default current_timestamp, 
    us_creation_user varchar(15) default 'user.test',
    us_update_date timestamp default current_timestamp,
    us_update_user varchar(15) default 'user.test'
)
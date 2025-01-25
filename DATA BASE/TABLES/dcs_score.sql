-- Tiket R11 - Tabla de calificaciones por concepto
/*Columnas:

id autoincrementable
id_type_concept - llave foranea de la tabla dcs_type_score (de esta forma se deternina el concepto al que pertenece la nota)
number_score (valor decimal de la nota asignada, se valida con el sistema de calificaciones asignado al curso para comprobar que este dentro de algun rango establecido en alguna linea)
columnas de control*/

create table dcs_score(){
    id int primary key,                                 -- id autoincrementable
    id_type_concept int references dcs_type_score(id),  -- id_type_concept - llave foranea de la tabla dcs_type_score (de esta
    number_score decimal(3,2),                          -- valor decimal de la nota asignada, se valida con el sistema de calificaciones asignado al curso para comprobar que este dentro de algun rango establecido en alguna linea)

    -- Columnas de control 

    us_creation_date timestamp default current_timestamp,
    us_creation_user varchar(15) default 'user.test',
    us_update_date timestamp default current_timestamp,
    us_update_user varchar(15) default 'user.test'

}   
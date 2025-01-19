--Ticket R4-Tabla estudiantes
--Tabla dcs_students que almacena a los estudiantes
/*Columnas:

1.- id - autoincrementable llave primaria
2.- nombres - obligatorio (not null)
3.- apellidos - obligatorio
3.- fecha de nacimiento
4.- genero (M, F, X (prefiero no decirlo))
5.- correo electronico - campo unico
6.- direccion de residencia
7.- estado (E, D) enabled , disabled
8.- columnas de control
*/
create table dcs_students (
    id int primary key,                                      -- llave primaria
    stud_name varchar(50) not null,                                         -- nombres
    stud_last_name varchar(50) not null,                                    -- apellidos
    stud_age_naciment date not null,                                        -- fecha de nacimiento
    stud_gender varchar(1) not null check(stud_gender in('M', 'F', 'X')),   -- genero
    stud_email varchar(100) unique not null,                                -- correo electronico
    stud_address varchar(100),                                              -- direccion de residencia
    stud_status varchar(1) not null check(stud_status in('E', 'D')),         -- estado

    -- Columnas de control 

    us_creation_date timestamp default current_timestamp, 
    us_creation_user varchar(15) default 'user.test',
    us_update_date timestamp default current_timestamp,
    us_update_user varchar(15) default 'user.test'

)
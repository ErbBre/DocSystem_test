-- Ticket R6-Tabla de ocupaciones
/*Columnas:

id autoincrementable numerico
Nombre de la profesion u ocupación
Descripcion
Sin columnas de control*/

create table dcs_ocupations (
    id int primary key,                 -- autoincrementable
    name_ocupation varchar(50) not null,-- Nombre de la profesion u ocupación
    descript varchar(100)               -- Descripcion
)
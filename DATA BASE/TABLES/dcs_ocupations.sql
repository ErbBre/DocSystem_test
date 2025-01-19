-- =========================================
-- Ticket R6-Tabla de ocupaciones
-- =========================================

create table dcs_ocupations (
    id serial primary key,               -- autoincrementable
    name_ocupation varchar(50) not null, -- Nombre de la profesion u ocupación
    descript varchar(100)                -- Descripcion
);
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
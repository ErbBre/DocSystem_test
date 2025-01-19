-- R2-Tabla de credenciales de acceso
-- Tabla dcs_key_access_log
/* Necesita de:
Columnas:

-identificador del usuario(profesor)
-usuario de login (encriptado)
-contraseña de login (encriptado)
-estado (Enabled, Disabled)
-Fecha de creacion
-usuario de creacion
-Fecha de actualización
-usuario de actualizacion
*/

CREATE TABLE dcs_key_access_log (
    id int not null,
    us_user varchar(15) not null,
    us_passw varchar(20) not null,
    us_state char(1) not null check(us_state in ('E','D') ),
    
    --Identificar el registro
    
    us_creation_date timestamp default current_timestamp,
    us_creation_user varchar(15) default 'user.test',
    us_update_date timestamp default current_timestamp,
    us_update_user varchar(15) default 'user.test'

)
-- =========================================
-- R12- Sistema de calificaciones para cursos (cabecera)
-- =========================================

/*Columnas:

cabid autoincrementable PK
nombre del sistema de calificaciones
descripcion del sistema de calificaciones
estado Enable-Disable
Ejemplos

id	score_name	                score_desc	        score_state
1	Escala numérica	            Mas usado en Perú	    E
2	Escala numérica	            Mas usada en Mexico	    D
3	Escala alfabética	        Gran parte de USA	    D
4	Escala alfabética precisa	Algunas	D
*/

create table dcs_sis_scoreh(
    cabid           serial primary key,
    score_name      varchar(50)     not null,
    score_desc      varchar(100)    not null,
    score_state     char(1)         not null default 'E',
    
    -- Check estado de curso (enabled, disabled)
    check(score_state in ('E','D') )
)
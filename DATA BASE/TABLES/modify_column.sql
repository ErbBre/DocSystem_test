-- =========================================
-- R14- Columna sistema de calificaciones para cursos
-- =========================================

ALTER TABLE     dcs_courses             ADD         COLUMN type_system_score    INT;
ALTER TABLE     dcs_courses 
ADD CONSTRAINT  fk_type_system_score    FOREIGN KEY (type_system_score) 
REFERENCES      dcs_sis_scoreh (cabid);

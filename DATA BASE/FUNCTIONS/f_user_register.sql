-- =============================================================
-- DCS-20
-- Funcion para dar de alta un usuario
-- =============================================================
CREATE OR REPLACE FUNCTION f_user_register(
    p_names         varchar(45), 
    p_lastnames     varchar(45),
    p_identify      varchar(20),
    p_user          varchar(15), 
    p_passw         varchar(20),
    p_age_naciment  date,
    p_us_email      varchar(100),
    p_gender        char(1),
    p_phone         varchar(20),
    p_user_adress   varchar(255)
    )
    RETURNS JSON AS $$
        DECLARE
            /*DECLARATION OF VARIABLES*/
            v_response JSON;
            v_validate BOOLEAN := TRUE;
            v_msg_err TEXT;
            v_sql_id INT;
        BEGIN
            /*=================================================
              VALIDATE DATA RECIVED
              =================================================*/
            IF    p_names        IS null OR LENGTH(TRIM(p_names))         = 0 THEN
                v_msg_err   := 'El nombre no debe ser nulo.';
                v_validate  := FALSE;
            ELSIF p_lastnames    IS null OR LENGTH(TRIM(p_lastnames))     = 0 THEN
                v_msg_err   := 'Los apellidos no deben ser nulos.';
                v_validate  := FALSE;
            ELSIF p_identify     IS null OR LENGTH(TRIM(p_identify))      = 0 THEN
                v_msg_err   := 'El campo Doc. identificacion no debe ser nulo.';
                v_validate  := FALSE;
            ELSIF p_user         IS null OR LENGTH(TRIM(p_user))          = 0 THEN
                v_msg_err   := 'El campo usuario no debe ser nulo.';
                v_validate  := FALSE;
            ELSIF p_passw        IS null OR LENGTH(TRIM(p_passw))         = 0 THEN
                v_msg_err   := 'Campo contraseña no debe ser nulo.';
                v_validate  := FALSE;
            ELSIF p_age_naciment IS null THEN
                v_msg_err   := 'Debe seleccionar una fecha de nacimiento.';
                v_validate  := FALSE;
            ELSIF p_age_naciment > CURRENT_DATE THEN
                v_msg_err   := 'La Fecha de nacimiento no puede ser mayor a hoy.';
                v_validate  := FALSE;
            ELSIF p_gender       IS null  OR LENGTH(TRIM(p_gender))       = 0 THEN
                v_msg_err   := 'El campo genero no debe ser nulo.';
                v_validate  := FALSE;
            END IF;

            IF p_us_email IS null OR LENGTH(TRIM(p_us_email)) = 0 THEN
                v_msg_err   := 'El campo correo electronico no debe ser nulo.';
                v_validate  := FALSE;
            ELSE
                IF EXISTS (SELECT 1 FROM dcs_user_access_system WHERE us_email = p_us_email) THEN
                    v_msg_err   := 'El correo electronico ['||p_us_email||'] ya existe.';
                    v_validate  := FALSE;
                ELSIF EXISTS (SELECT 1 FROM dcs_key_access_log WHERE us_user = p_user) THEN
                    v_msg_err   := 'El usuario ['||p_user||'] ya está en uso.';
                    v_validate  := FALSE;
                END IF;
            END IF;
            
            IF v_validate THEN
                /*=================================================
                    SAVE PERSONAL DATA OF THE USER
                  =================================================*/
                INSERT INTO  dcs_user_access_system (
                    names, last_names, identific, age_naciment, us_email,
                    gender, phone, user_adress, acount_status)
                VALUES(p_names,  p_lastnames,  p_identify, p_age_naciment, p_us_email, p_gender, p_phone, p_user_adress, 'E') 
                    RETURNING id INTO v_sql_id;

                /*=================================================
                    SAVE ACCESS KEY OF THE USER
                  =================================================*/
                INSERT INTO dcs_key_access_log (id_user, us_user, us_passw, us_state) 
                VALUES (v_sql_id, p_user, p_passw, 'E');
                -- =================================================
                -- THE JSON BUILD
                -- =================================================
                v_response := json_build_object('state',v_validate,'msg','Usuario registrado');
            ELSE
                v_response := json_build_object('state',0,'msg',v_msg_err);
            END IF;

            RETURN v_response;
        END;
    $$ LANGUAGE plpgsql;
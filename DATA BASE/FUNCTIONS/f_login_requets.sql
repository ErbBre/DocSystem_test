-- =============================================================
-- DCS-21
-- Funcion que valida la solicitud de inicio de sesion
-- =============================================================
CREATE FUNCTION f_login_request(p_
    user varchar(15), 
    p_passw varchar(20))
    RETURNS JSON AS $$
        DECLARE
            /*DECLARACIÓN DE VARIABLES*/
            exist BOOLEAN;
            response JSON;
        BEGIN
            /*CONTENIDO DE LA FUNCIÓN*/
            
            -- EVALUA LA EXISTENCIA DE LA CREDENCIAL PROPORCIONADA POR EL USUARIO
            SELECT 
                EXISTS(
                    SELECT 1
                    FROM dcs_key_access_log
                    WHERE 
                            us_state    = 'E'
                        AND us_user     = p_user
                        AND us_passw    = p_passw
                ) INTO exist;

            -- SI LA CREDENCIAL EXISTE 
            IF exist THEN
                -- JSON CON DATOS DEL USUARIO
                SELECT
                    json_build_object(
                        'state',         1,  -- Estado 1 si la credencial es válida
                        'id_user',       b.id,
                        'id',            a.id,
                        'names',         b.names,
                        'last_names',    b.last_names,
                        'identific',     b.identific,
                        'age_naciment',  b.age_naciment,
                        'us_email',      b.us_email,
                        'gender',        b.gender,
                        'phone',         b.phone,
                        'user_adress',   b.user_adress,
                        'acount_status', b.acount_status
                    ) INTO response
                FROM dcs_key_access_log AS a 
                    JOIN dcs_user_access_system AS b
                        ON a.id = b.id  
                WHERE 
                        a.us_state  = 'E'
                    AND a.us_user   = p_user
                    AND a.us_passw  = p_passw;
            ELSE
                -- Estado 0 si la credencial es invalida
                response := json_build_object('state', 0);
            END IF;
            
            RETURN response;
        END;
    $$ LANGUAGE plpgsql;
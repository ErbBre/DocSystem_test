CREATE OR REPLACE FUNCTION sett_labels_of_columns_fins()
RETURNS TRIGGER AS $$
BEGIN
    -- VALIDATE EXISTENCE OF TABLE
    IF NOT EXISTS( 
        SELECT 1 
        FROM information_schema.tables 
        WHERE table_schema = 'public' AND table_name = NEW.tabname
    ) THEN
        RAISE EXCEPTION 'La tabla [%] no existe', NEW.tabname;
    END IF;

    -- VALIDATE EXISTENCE OF LANGUAGE
    IF NOT EXISTS(
        SELECT 1 
        FROM sett_languages  -- Asegúrate de que el nombre de la tabla sea correcto
        WHERE code_lan = NEW.language_code
    ) THEN
        RAISE EXCEPTION 'El idioma [%] no existe', NEW.language_code;
    END IF;
    
    IF NOT EXISTS(
            SELECT 1 
            FROM information_schema.columns 
            WHERE 
                table_schema = 'public' 
            AND table_name = NEW.tabname 
            AND column_name = NEW.colname
        ) THEN
        RAISE EXCEPTION 'La columna [%] no existe', NEW.colname;
    END IF;

    -- Return the newly inserted row
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER sett_labels_of_columns_ins
BEFORE INSERT ON sett_labels_of_columns 
FOR EACH ROW
EXECUTE FUNCTION sett_labels_of_columns_fins();
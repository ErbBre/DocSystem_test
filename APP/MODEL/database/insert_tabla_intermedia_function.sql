DO $$  -- Inicia un bloque anónimo de ejecución
DECLARE
    -- Declaración de variables
BEGIN
    -- Lógica de ejecución
END $$;

DECLARE
    student_id INT;         -- Almacena el ID del estudiante actual
    parent_id INT;          -- Almacena el ID del apoderado actual
    used_pairs TEXT[] := ARRAY[  -- Array que almacena todas las combinaciones existentes
        '1-45', '1-25',      -- Ejemplos de pares existentes (deberían incluir TODOS los que ya tienes)
        '2-78', '3-12',
        -- ...
        '155-115'            -- Último par existente
    ];
    FOR student_id IN 1..49 LOOP  -- Itera sobre estudiantes del 1 al 49
    CONTINUE WHEN student_id IN (SELECT id_student FROM dcs_std_par);  -- Salta si el estudiante ya existe
    
    -- Bucle para encontrar un apoderado no usado para este estudiante
    LOOP
        parent_id := 1 + floor(random() * 300);  -- Genera un ID de apoderado aleatorio (1-300)
        EXIT WHEN NOT (student_id::text || '-' || parent_id::text = ANY(used_pairs));  -- Sale cuando encuentra una combinación única
    END LOOP;
    
    -- Inserta la nueva relación
    INSERT INTO dcs_std_par (id_student, id_parent) VALUES (student_id, parent_id);
    
    -- Registra la nueva combinación en el array
    used_pairs := array_append(used_pairs, student_id::text || '-' || parent_id::text);
    
    -- Con un 30% de probabilidad, asigna un segundo apoderado
    IF random() < 0.3 THEN
        -- Misma lógica para encontrar segundo apoderado único
        LOOP
            parent_id := 1 + floor(random() * 300);
            EXIT WHEN NOT (student_id::text || '-' || parent_id::text = ANY(used_pairs));
        END LOOP;
        
        INSERT INTO dcs_std_par (id_student, id_parent) VALUES (student_id, parent_id);
        used_pairs := array_append(used_pairs, student_id::text || '-' || parent_id::text);
    END IF;
END LOOP;

FOR student_id IN 147..200 LOOP  -- Itera sobre estudiantes del 147 al 200 (ajustar según necesidad)
    -- Exactamente la misma lógica que para el rango 1-49
    LOOP
        parent_id := 1 + floor(random() * 300);
        EXIT WHEN NOT (student_id::text || '-' || parent_id::text = ANY(used_pairs));
    END LOOP;
    
    INSERT INTO dcs_std_par (id_student, id_parent) VALUES (student_id, parent_id);
    used_pairs := array_append(used_pairs, student_id::text || '-' || parent_id::text);
    
    IF random() < 0.3 THEN
        LOOP
            parent_id := 1 + floor(random() * 300);
            EXIT WHEN NOT (student_id::text || '-' || parent_id::text = ANY(used_pairs));
        END LOOP;
        
        INSERT INTO dcs_std_par (id_student, id_parent) VALUES (student_id, parent_id);
        used_pairs := array_append(used_pairs, student_id::text || '-' || parent_id::text);
    END IF;
END LOOP;


/*
Puntos Clave
Control de duplicados: Usa el array used_pairs para llevar registro de todas las combinaciones existentes

Exclusión de rango 50-146: No itera sobre ese rango como solicitaste

Aleatoriedad controlada: Genera apoderados aleatorios pero con restricciones

Distribución 30%: Un 30% de estudiantes tendrán 2 apoderados

Seguridad: Verifica cada combinación antes de insertar

Recomendaciones
Antes de ejecutar: Asegúrate que el array used_pairs contiene TODOS los pares existentes

Ajustar rangos: Verifica que 147-200 sea correcto para tus estudiantes

Transacción: Considera envolver esto en una transacción por seguridad

*/
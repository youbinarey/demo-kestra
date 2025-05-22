-- models/empleados_limpios.sql
SELECT
    id,
    nombre,
    apellido,
    fecha_nacimiento,
    fecha_contratacion,
    salario
FROM empleados
WHERE activo = 1

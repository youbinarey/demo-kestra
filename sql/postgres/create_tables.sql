CREATE TABLE IF NOT EXISTS transactions (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    amount DECIMAL(10,2),
    date DATE
);

INSERT INTO transactions (user_id, amount, date) VALUES
(1,150.00,'2024-01-01'),
(2,89.99,'2024-01-02'),
(3,22.50,'2024-01-03'),
(1,200.00,'2024-01-04');



CREATE TABLE IF NOT EXISTS empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    fecha_nacimiento DATE,
    fecha_contratacion DATE,
    salario DECIMAL(10,2),
    activo BOOLEAN DEFAULT TRUE
);

INSERT INTO empleados (nombre, apellido, fecha_nacimiento, fecha_contratacion, salario) VALUES
('Juan', 'Pérez', '1985-05-15', '2020-01-10', 50000.00),
('Ana', 'Gómez', '1990-03-22', '2019-06-15', 60000.00),
('Luis', 'Martínez', '1982-11-30', '2018-02-20', 55000.00),
('María', 'López', '1995-07-10', '2021-03-01', 45000.00);
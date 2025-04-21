-- Cambiar a la base de datos idinet
USE idinet;

-- Crear tabla transactions
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='transactions' AND xtype='U')
BEGIN
    CREATE TABLE transactions (
        id INT IDENTITY(1,1) PRIMARY KEY,
        user_id INT NOT NULL,
        amount DECIMAL(10,2),
        date DATE
    );
END;

-- Insertar datos en transactions
INSERT INTO transactions (user_id, amount, date) VALUES
(1, 150.00, '2024-01-01'),
(2, 89.99, '2024-01-02'),
(3, 22.50, '2024-01-03'),
(1, 200.00, '2024-01-04');

-- Crear tabla empleados
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='empleados' AND xtype='U')
BEGIN
    CREATE TABLE empleados (
        id INT IDENTITY(1,1) PRIMARY KEY,
        nombre NVARCHAR(100),
        apellido NVARCHAR(100),
        fecha_nacimiento DATE,
        fecha_contratacion DATE,
        salario DECIMAL(10,2),
        activo BIT DEFAULT 1
    );
END;

-- Insertar datos en empleados
INSERT INTO empleados (nombre, apellido, fecha_nacimiento, fecha_contratacion, salario) VALUES
(N'Juan', N'Pérez', '1985-05-15', '2020-01-10', 50000.00),
(N'Ana', N'Gómez', '1990-03-22', '2019-06-15', 60000.00),
(N'Luis', N'Martínez', '1982-11-30', '2018-02-20', 55000.00),
(N'María', N'López', '1995-07-10', '2021-03-01', 45000.00);
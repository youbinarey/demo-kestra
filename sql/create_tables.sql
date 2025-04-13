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
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

INSERT INTO usuarios (nombre, email) VALUES
('Carlos', 'carlos@test.com'),
('Maria', 'maria@test.com')
ON CONFLICT DO NOTHING;

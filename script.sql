-- Crear la base de datos
CREATE DATABASE api_receta;

-- Crear el usuario
CREATE USER 'root'@'localhost' IDENTIFIED BY '';

-- Asignar permisos
GRANT ALL PRIVILEGES ON api_receta.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
CREATE DATABASE api_receta;

CREATE USER 'root'@'localhost' IDENTIFIED BY '';

GRANT ALL PRIVILEGES ON api_receta.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
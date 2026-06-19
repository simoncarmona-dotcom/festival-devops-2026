CREATE DATABASE IF NOT EXISTS festival_db;
USE festival_db;

CREATE TABLE IF NOT EXISTS artistas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

INSERT INTO artistas (nombre) VALUES 
('Los Microservicios del Pacífico'), 
('Docker & The Containers'), 
('DJ Kubernete'),
('La Orquesta YAML');
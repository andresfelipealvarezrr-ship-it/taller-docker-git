# Ejercicio - Escenario 1: WordPress + MariaDB

## Cómo levantar el stack
1. Verificar que el archivo .env tenga las variables configuradas
2. Ejecutar: docker compose up -d
3. WordPress disponible en: http://localhost:8082
4. phpMyAdmin disponible en: http://localhost:8081

## Servicios
- db: MariaDB 10.11
- phpmyadmin: administración visual de la base de datos
- wordpress: sitio WordPress

## Detener
docker compose down

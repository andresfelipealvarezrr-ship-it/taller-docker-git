# Ejercicio - Escenario 4: CI/CD con FastAPI

![CI/CD](https://github.com/andresfelipealvarezrr-ship-it/taller-docker-git/actions/workflows/ci-cd.yml/badge.svg)

## Descripción
API FastAPI containerizada con multi-stage build, tests automáticos,
publicación a DockerHub y GHCR, y scan de vulnerabilidades con Trivy.

## Uso local (desarrollo)
docker compose up --build -d
curl http://localhost:3003

## Uso en producción (imagen publicada)
docker compose -f docker-compose.prod.yml up -d

## Tests
pytest tests/

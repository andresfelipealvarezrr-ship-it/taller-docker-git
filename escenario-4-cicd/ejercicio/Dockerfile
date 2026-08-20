# Etapa 1: build - instala dependencias
FROM python:3.11-slim AS build
WORKDIR /app
COPY src/requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Etapa 2: production - imagen final liviana
FROM python:3.11-slim AS production
WORKDIR /app
COPY --from=build /root/.local /root/.local
COPY src/ .
ENV PATH=/root/.local/bin:$PATH
EXPOSE 3000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]

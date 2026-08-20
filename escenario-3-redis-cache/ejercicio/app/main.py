from fastapi import FastAPI, Request, HTTPException
import redis
import psycopg2
import os
import json
import time

app = FastAPI()

redis_client = redis.Redis(
    host=os.environ.get('REDIS_HOST', 'redis'),
    port=int(os.environ.get('REDIS_PORT', 6379)),
    decode_responses=True
)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        port=os.environ.get('DB_PORT', 5432),
        user=os.environ.get('DB_USER', 'postgres'),
        password=os.environ.get('DB_PASSWORD', 'postgres'),
        dbname=os.environ.get('DB_NAME', 'cachedb')
    )

RATE_LIMIT = 10  # requests
RATE_WINDOW = 60  # segundos

@app.middleware("http")
async def rate_limiter(request: Request, call_next):
    ip = request.client.host
    key = f"rate:{ip}"
    current = redis_client.incr(key)
    if current == 1:
        redis_client.expire(key, RATE_WINDOW)
    if current > RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Demasiadas peticiones, intenta más tarde")
    response = await call_next(request)
    return response

@app.get("/")
def index():
    return {"servicio": "FastAPI + Redis + PostgreSQL", "status": "activo"}

@app.get("/contador")
def contador():
    total = redis_client.incr("visitas_totales")
    return {"visitas": total}

@app.get("/usuarios")
def get_usuarios():
    cache_key = "usuarios_cache"
    cached = redis_client.get(cache_key)
    if cached:
        return {"origen": "cache", "usuarios": json.loads(cached)}

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, email FROM usuarios ORDER BY id")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    usuarios = [{"id": r[0], "nombre": r[1], "email": r[2]} for r in rows]
    redis_client.setex(cache_key, 30, json.dumps(usuarios))
    return {"origen": "postgresql", "usuarios": usuarios}

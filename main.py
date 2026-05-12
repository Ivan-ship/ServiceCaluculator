from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def read_root():
    return{"message": "First Start"}

# Подключение postgresql
@app.get("/connect-postgresql")
def connect_postgres():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT version();"))
            return{"status": "connected"}
    except Exception as ex:
        return {"status": "error", "message": str(ex)}

# main.py
import uvicorn
from fastapi import FastAPI
from app.routes.routes import routes, router
from pathlib import Path

app = FastAPI(title="tummoc test")

app.include_router(routes, prefix="/api")
app.include_router(router,prefix="/api/school")
# app.include_router(distance_router)

if __name__ == "__main__":
    uvicorn.run(f"{Path(__file__).stem}:app", host="0.0.0.0", port=8000)
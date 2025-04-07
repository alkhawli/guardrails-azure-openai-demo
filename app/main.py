import uvicorn
from fastapi import FastAPI
from app.api.routers.generate import router as generate_router

app = FastAPI()
app.include_router(generate_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")

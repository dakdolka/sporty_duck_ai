from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from .routers import register_routers

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        lifespan=lifespan,
        title="AI Companion",
        version="0.1.0",
    )

    register_routers(app)
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Разрешает все домены, можно указать список доменов, например: ["http://localhost:3000"]
        allow_credentials=True,
        allow_methods=["*"],  # Разрешены все методы HTTP
        allow_headers=["*"],  # Разрешены все заголовки
    )
    
    return app




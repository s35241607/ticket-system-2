from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from app.api.routers import tickets
from app.core.config import settings
from app.db.initial_data import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # on startup
    print("Initializing database...")
    init_db()
    print("Database initialization complete.")
    yield
    # on shutdown
    print("Application shutting down.")

app = FastAPI(
    title="Ticket System API",
    description="API for the enterprise ticket system.",
    version="0.1.0",
    lifespan=lifespan
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(tickets.router, prefix="/api/v1/tickets", tags=["tickets"])

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}

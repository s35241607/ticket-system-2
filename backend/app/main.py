from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.api.routers import tickets, auth
from app.core.config import get_settings
from app.db import session
from app.db.initial_data import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # on startup
    print("Initializing application...")
    settings = get_settings()

    session.engine = create_engine(str(settings.DATABASE_URI), pool_pre_ping=True)
    session.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=session.engine)

    # In a real app, you'd use Alembic migrations here.
    # For this prototype, we'll initialize the DB directly.
    init_db(session.engine)

    print("Application initialization complete.")
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
# This should be configured based on your frontend's origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(tickets.router, prefix="/api/v1/tickets", tags=["tickets"])

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}

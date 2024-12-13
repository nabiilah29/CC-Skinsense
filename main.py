from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.dependencies.database import create_tables, engine
from app.routes import auth_routes, survey_routes

# Definisikan lifespan untuk inisialisasi dan cleanup
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: buat tabel database
    print("Creating database tables...")
    create_tables()
    print("Database tables created successfully")
    yield
    # Cleanup (jika diperlukan)
    print("Shutting down application...")

# Inisialisasi FastAPI dengan lifespan
app = FastAPI(
    title="Your Project Name",
    description="Project description",
    version="0.1.0",
    lifespan=lifespan
)

# Include routers
app.include_router(auth_routes.router, prefix="/auth")
app.include_router(survey_routes.router, prefix="/survey")

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the API"}
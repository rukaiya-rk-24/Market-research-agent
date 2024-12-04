from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from contextlib import asynccontextmanager
from .database import  init_db, get_db
from .db_models import Competitor
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Or ["*"] to allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()

@app.get("/api/competitors", response_model=list[dict])
async def get_competitors(sector: str, db: AsyncSession = Depends(get_db)):
    try:
        # Query the database for competitors matching the sector
        query = await db.execute(select(Competitor).where(Competitor.sector == sector))
        competitors = query.scalars().all()

        # Return the names of the competitors
        return [
            {
                "id": competitor.id,
                "name": competitor.name,
                "sector": competitor.sector
            } for competitor in competitors
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/competitors/{competitor_id}")
async def get_competitor_details(competitor_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Competitor).where(Competitor.id == competitor_id))
    competitor = result.scalars().first()
    if not competitor:
        raise HTTPException(status_code=404, detail="Competitor not found")
    return {
        "id": competitor.id,
        "name": competitor.name,
        "sector": competitor.sector,
        "description": competitor.description,
        "revenue": 1000000,  # Mock data
        "employees": 500,  # Mock data
    }

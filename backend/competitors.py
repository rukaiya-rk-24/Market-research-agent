from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import get_db
from db_models import Competitor
from research_agent import research_agent, ResearchDependencies

router = APIRouter(prefix="/api/competitors", tags=["Competitors"])

@router.get("/")
async def get_competitors(sector: str = None, db: AsyncSession = Depends(get_db)):
    """Fetch competitors by sector."""
    query = select(Competitor)
    if sector:
        query = query.filter(Competitor.sector.ilike(f"%{sector}%"))
    result = await db.execute(query)
    competitors = result.scalars().all()
    return competitors

@router.get("/{competitor_id}")
async def get_competitor_details(competitor_id: int, db: AsyncSession = Depends(get_db)):
    """Fetch competitor details by ID."""
    try:
        query = select(Competitor).where(Competitor.id == competitor_id)
        result = await db.execute(query)
        competitor = result.scalar_one_or_none()
        if not competitor:
            raise HTTPException(status_code=404, detail="Competitor not found")
        return competitor
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/example")
async def example_route():
    return {"message": "Example route working!"}

@router.post("/add/")
async def add_competitor(name: str, sector: str, description: str, db: AsyncSession = Depends(get_db)):
    """Add a new competitor to the database."""
    competitor = Competitor(name=name, sector=sector, description=description)
    db.add(competitor)
    await db.commit()
    return {"message": f"Competitor '{name}' added successfully."}

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.get("/analyze/")
async def analyze_competitor(company_name: str, sector: str):
    """Analyze a competitor using the research agent."""
    deps = ResearchDependencies(company_name=company_name, sector=sector)
    result = await research_agent.run("Perform competitor analysis.", deps=deps)
    if not result.success:
        raise HTTPException(status_code=500, detail="Failed to generate competitor analysis.")
    return result.data

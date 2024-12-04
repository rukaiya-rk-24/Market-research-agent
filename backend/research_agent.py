from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext

class ResearchDependencies:
    """Dependencies required for the research agent."""
    company_name: str
    sector: str

class ResearchResult(BaseModel):
    """The result structure for AI responses."""
    company_overview: str = Field(description="Overview of the competitor company")
    strengths: str = Field(description="Key strengths of the company")
    weaknesses: str = Field(description="Key weaknesses of the company")
    recommendations: str = Field(description="Recommendations to outperform this competitor")

# Define the AI-powered agent
research_agent = Agent(
    "openai:gpt-4o",
    deps_type=ResearchDependencies,
    result_type=ResearchResult,
    system_prompt=(
        "You are an AI expert in market research. Provide detailed competitor analysis, "
        "including company overview, strengths, weaknesses, and actionable recommendations. "
    ),
)

@research_agent.system_prompt
async def add_context(ctx: RunContext[ResearchDependencies]) -> str:
    """Dynamically inject sector and company context."""
    return (
        f"The company being analyzed is '{ctx.deps.company_name}', "
        f"operating in the '{ctx.deps.sector}' sector."
    )


print("research_agent loaded")

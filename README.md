# Market Research Agent

This project is a full-stack market research tool that allows users to query competitor data from a backend API. The frontend allows users to enter a sector, fetch a list of competitors in that sector, and view detailed information about each competitor.

## Technologies Used

- **Frontend**: React, Material UI
- **Backend**: FastAPI, PostgreSQL, SQLAlchemy (with async support)
- **Database**: PostgreSQL
- **OpenAI**: For advanced data analysis and competitor insights

## Prerequisites

Before starting, ensure you have the following installed:

- Python 3.7+
- Node.js (for frontend)
- PostgreSQL (for database)
- OpenAI API Key 

## Setup Instructions

### 1. Set Up the Backend

#### 1.1 Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/market-research-agent.git
cd market-research-agent
```

### 2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate
```

### 3. Install backend dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup PostgreSQL Database

- Install PostgreSQL if you haven't already. 
- Create a new PostgreSQL database and user:
  
```bash
psql -U postgres
CREATE DATABASE market_research;
CREATE USER research_user WITH PASSWORD 'secure_password';
ALTER ROLE research_user SET client_encoding TO 'utf8';
ALTER ROLE research_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE research_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE market_research TO research_user;
```

### 5. Start the application

Run the following command in the directory:

```bash
npm run start
```


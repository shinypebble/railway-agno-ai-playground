# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This is a Railway template repository for deploying Agno AI agent playgrounds with one-click deployment. It provides a minimal setup to get AI agents running quickly without infrastructure complexity.

## Common Commands

### Local Development
```bash
# Setup virtual environment with uv (recommended)
uv venv --python 3.13
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv sync

# Set required API key
export ANTHROPIC_API_KEY=your-api-key-here

# Run the application locally
python main.py

# The Agno playground will be available at http://localhost:8080
```

### Deployment
```bash
# Deploy to Railway
railway up

# Set required environment variables
railway variables set ANTHROPIC_API_KEY=your-api-key-here

# Railway automatically provides a PORT variable - no need to set it manually!
```

### Code Formatting
```bash
# Format Python code with Black (line length 160)
black main.py
```

## Architecture

### Core Components
- **main.py**: Minimal Agno agent setup with:
  - Single Claude-powered agent
  - Built-in playground UI via Agno
  - Automatic port binding for Railway
  
### Configuration
- **pyproject.toml**: Modern Python packaging with Agno and dependencies
- **railway.json**: Railway deployment configuration using Railpack
- Environment variables:
  - `ANTHROPIC_API_KEY` - Required for Claude model
  - `PORT` - Auto-provided by Railway

### Key Design Decisions
1. Minimal agent implementation - just enough to get started
2. Uses Agno's built-in playground UI - no custom frontend needed
3. Single agent setup to keep it simple for beginners
4. Uses Claude 4 Sonnet (claude-sonnet-4-20250514) as the default model
5. No storage/database setup - users can add as needed
6. Zero-configuration deployment on Railway
7. Host set to empty string ("") in main.py:23 to enable dual-stack IPv4/IPv6 for Railway's private networking

## Extending the Template

Users can customize by:
1. Adding tools (web search, databases, APIs)
2. Creating multiple specialized agents
3. Adding storage for conversation history
4. Connecting knowledge bases and vector DBs
5. Customizing agent instructions and behavior

## Testing Changes

Ensure any modifications maintain:
1. Zero-configuration deployment capability on Railway
2. Minimal setup - users should only need to add API key
3. Clear error messages if API key is missing
4. Proper handling of Railway's auto-provided PORT variable
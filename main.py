# main.py
import os
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.playground import Playground, serve_playground_app

# Create a minimal agent with Claude
agent = Agent(
    name="Assistant",
    model=Claude(id="claude-sonnet-4-20250514"),
    instructions=["You are a helpful AI assistant. Be concise and clear in your responses."],
    markdown=True,
)

# Create the playground app with our agent
app = Playground(agents=[agent]).get_app()

# For Railway deployment
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    # Use empty string for host to enable dual-stack IPv4/IPv6
    # This allows Railway's private networking to work properly
    host = ""

    # Use Agno's built-in server which handles the playground UI
    serve_playground_app("main:app", host=host, port=port, reload=True)  # Disable reload in production

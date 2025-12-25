import uvicorn
import os
from dotenv import load_dotenv
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from agents import marketing_manager

# Load API Keys
load_dotenv()

from starlette.responses import RedirectResponse

# 1. Convert our local ADK agent into an A2A-compatible Starlette application
app = to_a2a(
    marketing_manager,
    host="localhost",
    port=8000,
    protocol="http"
)

# 2. Add a convenience redirect for the user
@app.route("/agent.json")
async def redirect_to_card(request):
    return RedirectResponse(url="/.well-known/agent-card.json")

if __name__ == "__main__":
    print("🌐 A2A Marketing Agent Server starting...")
    print("📍 Protocol-compliant Agent Card: http://localhost:8000/.well-known/agent-card.json")
    print("✨ Convenience URL: http://localhost:8000/agent.json")
    print("📡 RPC Endpoint: http://localhost:8000/")
    
    # Run the server
    uvicorn.run(app, host="0.0.0.0", port=8000)

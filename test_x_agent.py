import asyncio
import os
from dotenv import load_dotenv
from main import run_agent_workflow
from agents import x_specialist

# Load environment variables
load_dotenv()

async def test_x_specialist():
    print("🧪 Testing X_Specialist Agent...")
    
    topic = "The future of AI Agents in 2026"
    prompt = f"Find the latest trends regarding {topic} on X and generate one viral post."
    
    response = await run_agent_workflow(x_specialist, prompt)
    
    if response:
        print("\n✨ Test Passed! Agent Response Received:")
        print("-" * 30)
        # The output is already printed by run_agent_workflow's stream
    else:
        print("\n❌ Test Failed: No response received.")

if __name__ == "__main__":
    if os.getenv("GOOGLE_API_KEY") and os.getenv("TAVILY_API_KEY"):
        asyncio.run(test_x_specialist())
    else:
        print("❌ Missing API Keys in .env")

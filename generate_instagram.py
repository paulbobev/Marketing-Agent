import asyncio
import os
from dotenv import load_dotenv
from main import run_agent_workflow
from agents import instagram_specialist

load_dotenv()

async def generate_instagram_post():
    print("📸 Generating Instagram Post...")
    
    topic = "Autonomous AI Agents for creative work"
    prompt = f"Research visual trends for {topic} on Instagram. Define a 'visual vibe' and write a high-engagement caption. Provide a clear image description for an AI image generator."
    
    response = await run_agent_workflow(instagram_specialist, prompt)
    
    if response:
        print("\n✨ Instagram Strategy Generated!")
        # In a real workflow, we might parse the image prompt here
    else:
        print("\n❌ Failed to generate Instagram content.")

if __name__ == "__main__":
    if os.getenv("GOOGLE_API_KEY") and os.getenv("TAVILY_API_KEY"):
        asyncio.run(generate_instagram_post())
    else:
        print("❌ Missing API Keys in .env")

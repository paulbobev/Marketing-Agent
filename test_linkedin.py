import asyncio
import os
from dotenv import load_dotenv
from main import run_agent_workflow
from agents import linkedin_specialist, gen_z_dev_critic

load_dotenv()

async def test_linkedin_workflow():
    print("💼 Testing LinkedIn Specialist Agent...")
    
    topic = "The transition from AI-assisted coding to autonomous agentic engineering"
    prompt = f"Find the latest professional trends regarding {topic} on LinkedIn and generate a high-authority thought leadership post."
    
    # 1. Generate LinkedIn Content
    print("\n--- 1. Generating LinkedIn Post ---")
    linkedin_content = await run_agent_workflow(linkedin_specialist, prompt)
    
    # 2. Review with Gen Z Critic
    print("\n--- 2. Gen Z Dev Critic Review (Arch Linux user btw) ---")
    critic_prompt = f"""
    Review this LinkedIn post. Is it too 'hustle culture' or 'corporate slop'? 
    Check if the technical shift from 'Copilots' to 'Agents' is handled with actual nuance or just hype.
    
    CONTENT:
    {linkedin_content}
    """
    await run_agent_workflow(gen_z_dev_critic, critic_prompt)

if __name__ == "__main__":
    if os.getenv("GOOGLE_API_KEY") and os.getenv("TAVILY_API_KEY"):
        asyncio.run(test_linkedin_workflow())
    else:
        print("❌ Missing API Keys in .env")

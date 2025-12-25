import asyncio
import os
from dotenv import load_dotenv
from main import run_agent_workflow
from agents import instagram_specialist, gen_z_dev_critic

load_dotenv()

async def test_critic_workflow():
    print("🚀 Running Content Review Workflow...")
    
    # 1. Generate content (using Instagram as the example)
    print("\n--- 1. Generating Content ---")
    topic = "Autonomous AI Agents for creative work"
    marketing_prompt = f"Write an Instagram caption for {topic}. Make it sound high-end and futuristic."
    marketing_content = await run_agent_workflow(instagram_specialist, marketing_prompt)
    
    # 2. Review it with the Gen Z Critic
    print("\n--- 2. Gen Z Dev Critic Review ---")
    critic_prompt = f"""
    Review this marketing content for any 'cringe' or 'corporate slop'. 
    Be honest. If it's too much hype without substance, roast it.
    
    CONTENT TO REVIEW:
    {marketing_content}
    """
    await run_agent_workflow(gen_z_dev_critic, critic_prompt)

if __name__ == "__main__":
    if os.getenv("GOOGLE_API_KEY"):
        asyncio.run(test_critic_workflow())
    else:
        print("❌ Missing GOOGLE_API_KEY")

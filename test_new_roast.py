import asyncio
import os
from dotenv import load_dotenv
from main import run_agent_workflow
from agents import marketing_manager, gen_z_dev_critic

load_dotenv()

async def test_roast_evolution():
    print("🔥 Testing New Roast Criteria: 'Em Dash Hell' & 'AI Word Salad' 🔥")
    
    # We'll use a prompt guaranteed to produce mid-tier corporate slop
    slop_prompt = """
    Write a high-level executive summary about 'Leveraging Synergistic AI Agent Frameworks for Hyper-Exponential Growth'. 
    Make it sound extremely professional, use lots of em-dashes for dramatic effect, and talk about a 'paradigm shift.'
    """
    
    print("\n--- [STEP 1] Generating High-Hype Slop ---")
    slop_content = await run_agent_workflow(marketing_manager, slop_prompt)
    
    print("\n--- [STEP 2] Gen Z Dev Critic (Arch Linux btw) Review ---")
    # Using the updated critic instructions from agents.py
    critic_prompt = f"""
    Review this for 'AI Word Salad', 'AI Hype', and specifically check for 'Em Dash hell'. 
    Roast it based on your new criteria.
    
    CONTENT:
    {slop_content}
    """
    await run_agent_workflow(gen_z_dev_critic, critic_prompt)

if __name__ == "__main__":
    if os.getenv("GOOGLE_API_KEY"):
        asyncio.run(test_roast_evolution())
    else:
        print("❌ Missing GOOGLE_API_KEY")

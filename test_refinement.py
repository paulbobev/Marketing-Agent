import asyncio
import os
from dotenv import load_dotenv
from main import run_agent_workflow
from agents import linkedin_specialist, gen_z_dev_critic

load_dotenv()

async def test_refinement_workflow():
    print("🔄 Starting Content Refinement Loop...")
    
    topic = "The transition from AI-assisted coding to autonomous agentic engineering"
    
    # 1. INITIAL DRAFT
    print("\n--- [STEP 1] Generating Initial Draft ---")
    initial_draft = await run_agent_workflow(
        linkedin_specialist, 
        f"Generate a high-authority LinkedIn post about {topic}."
    )
    
    # 2. GET CRITICISM
    print("\n--- [STEP 2] Gen Z Dev Critic Review (Arch Linux user btw) ---")
    criticism = await run_agent_workflow(
        gen_z_dev_critic, 
        f"Roast this LinkedIn post for 'corporate slop' and technical inaccuracies.\n\nCONTENT:\n{initial_draft}"
    )
    
    # 3. REFINE BASED ON CRITICISM
    print("\n--- [STEP 3] Refining Content with Feedback ---")
    refinement_prompt = f"""
    A technical reviewer (Arch Linux enthusiast) just roasted your previous post.
    
    THE FEEDBACK:
    {criticism}
    
    YOUR TASK:
    Rewrite the LinkedIn post to satisfy this technical critic.
    - Remove the 'corporate slop' and 'VP-level' hustle culture speak.
    - Be honest about the current limitations (debugging, hallucinatory logic, production risks).
    - Stop using terms like 'Conductor' or 'Rocket Emojis' if they were flagged as cringe.
    - Focus on the actual engineering reality of managing multi-agent systems.
    
    ORIGINAL TOPIC: {topic}
    """
    
    final_post = await run_agent_workflow(linkedin_specialist, refinement_prompt)
    
    # 4. FINAL VERDICT
    print("\n--- [STEP 4] Final Critic Verdict ---")
    await run_agent_workflow(
        gen_z_dev_critic, 
        f"Did they fix it? Is it actually 'based' now or still cooked?\n\nFINAL CONTENT:\n{final_post}"
    )

if __name__ == "__main__":
    if os.getenv("GOOGLE_API_KEY") and os.getenv("TAVILY_API_KEY"):
        asyncio.run(test_refinement_workflow())
    else:
        print("❌ Missing API Keys")

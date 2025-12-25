import asyncio
import os
from dotenv import load_dotenv
from google.adk.runners import Runner, types
from google.adk.sessions import InMemorySessionService
from agents import marketing_manager, x_specialist, linkedin_specialist, market_analyst

# Load API Keys from .env
load_dotenv()

async def run_agent_workflow(agent, prompt: str, user_id="user", session_id="session"):
    """Helper to run any agent and print its stream."""
    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name="agents", 
        user_id=user_id, 
        session_id=session_id
    )
    
    runner = Runner(
        agent=agent, 
        session_service=session_service, 
        app_name="agents"
    )
    
    user_msg = types.Content(
        role="user",
        parts=[types.Part(text=prompt)]
    )
    
    print(f"\n--- {agent.name} is working ---\n")
    
    full_response = ""
    try:
        async for event in runner.run_async(
            new_message=user_msg,
            user_id=user_id,
            session_id=session_id
        ):
            # Log Tool Calls
            func_calls = event.get_function_calls()
            if func_calls:
                for fc in func_calls:
                    print(f"🛠️  [{agent.name}] Calling Tool: {fc.name}")
            
            # Check for content events
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        print(part.text, end="", flush=True)
                        full_response += part.text
        print("\n")
        return full_response
    except Exception as e:
        print(f"\n❌ [{agent.name}] Error: {e}")
        return None

async def run_full_marketing_campaign(topic: str):
    print(f"🚀 Starting Multi-Platform Campaign for: {topic}")
    
    # 1. Market Analysis
    analysis_results = await run_agent_workflow(
        market_analyst, 
        f"Analyze the current market landscape for {topic}. What are the key pain points and opportunities?"
    )
    
    # 2. X Strategy (using analysis as context)
    x_results = await run_agent_workflow(
        x_specialist, 
        f"Based on this research:\n\n{analysis_results}\n\nGenerate 1 banger tweet and 1 thread hook about {topic}."
    )
    
    # 3. LinkedIn Strategy
    li_results = await run_agent_workflow(
        linkedin_specialist, 
        f"Based on this research:\n\n{analysis_results}\n\nGenerate a professional thought leadership post about {topic}."
    )
    
    print("\n✅ Campaign Generation Complete!")

if __name__ == "__main__":
    if os.getenv("GOOGLE_API_KEY") and os.getenv("TAVILY_API_KEY"):
        asyncio.run(run_full_marketing_campaign("Autonomous AI Agents in Marketing"))
    else:
        print("❌ Missing API Keys in .env")

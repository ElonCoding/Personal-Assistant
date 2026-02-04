from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import tool
from dotenv import load_dotenv
from jarvis_search import search_internet, get_formatted_datetime
from jarvis_get_weather import get_weather
from jarvis_ctrl_window import run_application_or_media, close_application, list_folder_items
from Jarvis_file_opner import Play_file
from keyboard_mouse_control import (
    move_cursor_tool, mouse_click_tool, scroll_cursor_tool, 
    type_text_tool, press_key_tool, swipe_gesture_tool, 
    press_hotkey_tool, control_volume_tool)
from langchain import hub
import asyncio
from livekit.agents import function_tool
load_dotenv()

@function_tool(
    name="thinking_capability",
    description=(
        "Use this tool whenever the user asks to generate or write something new. "
        "If the user does not specify where to write, open Notepad automatically using open_app and start writing. "
        "This tool can also handle tasks like Google search, checking the weather, "
        "opening/closing apps, accessing files, controlling mouse/keyboard, "
        "and system utilities."
))
async def thinking_capability(query: str) -> dict:
    """
    LangChain-powered reasoning and action tool.
    Takes a natural language query and executes the appropriate workflow.
    """
    
    model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")  # Updated model name
    
    prompt = hub.pull("hwchase17/react")
    
    # LangChain requires its own @tool decorated objects. 
    # Since our tools are @function_tool, we wrap them or ensure they are compatible.
    # For now, let's just pass them as they are and see if LangChain accepts them.
    # Note: If LangChain fails, we might need to use langchain.tools.StructuredTool.from_function
    
    tools = [
        search_internet,
        get_formatted_datetime,
        get_weather,
        run_application_or_media,
        close_application,
        list_folder_items,
        Play_file,
        move_cursor_tool,
        mouse_click_tool,
        scroll_cursor_tool,
        type_text_tool,
        press_key_tool,
        press_hotkey_tool,
        control_volume_tool,
        swipe_gesture_tool
    ]

    agent = create_react_agent(
        llm=model,
        tools=tools,
        prompt=prompt
    )

    executor = AgentExecutor(
        agent=agent,
        tools=tools,  # Use the same tools list
        verbose=True
    )

    try:
        # Use await instead of asyncio.run() since we're already in async context
        result = await executor.ainvoke({"input": query})
        return result
    except Exception as e:
        return {"error": f"Agent execution failed: {str(e)}"}

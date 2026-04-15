import cmds, organizer_mcp
import os, shutil
from pathlib import Path
from google import genai
from google.genai import types
from google.genai.types import FunctionDeclaration
from fastmcp import FastMCP
import time

client = genai.Client()





list_files = FunctionDeclaration(
    name="list_files",
    description="lists the file in a given directory,\
         returns list",
    parameters={
            "type": "OBJECT",
            "properties": {
                "directory": {"type": "STRING", "description": "names of all the files,"}
            },

            "required": ["directory"]
    },
)

read_file = FunctionDeclaration(
    name="read_file",
    description="reads a file into a buffer\
        returns content of a file",
    parameters={
        "type": "OBJECT",
        "properties": {
            "filename": {"type": "STRING", "description": "name of target file"},
        },
    },
)

move_file = FunctionDeclaration(
    name="move_file",
    description="Moves a file into a different location\
        returns 1 when successful, and 0 when unsuccessful",
    parameters={
        "type": "OBJECT",
        "properties": {
            "filename": {"type": "STRING", "description": "name of target file"},
            "category": {"type": "STRING", "description": "destination of folder/category"},
        },
    },
)


send_file = FunctionDeclaration(
    name="send_file",
    description="Send the file to the AI Agent for better analysis. Added as readfile may not work for all file extensions\
        returns the response from the AI when successful AND the file will be sent to the AI",
    parameters={
        "type": "OBJECT",
        "properties": {
            "filename": {"type": "STRING", "description": "File name"}
        },
        "required": ["filename"]
    },
)

tool_logic = types.Tool(
    function_declarations=[list_files, read_file, move_file, send_file]
)


declares = [organizer_mcp.list_files, organizer_mcp.read_file,
            organizer_mcp.move_file, organizer_mcp.send_file]


tool_map= {
    "list_files": organizer_mcp.list_files,
    "read_file": organizer_mcp.read_file,
    "move_file": organizer_mcp.move_file,
    "send_file": organizer_mcp.send_file,
}


# model_id = "gemma-4-31b-it"
# model_id = "gemini-3.1-flash-lite-preview"
# model_id = "gemini-2.5-flash"
# model_id = "gemini-2.5-flash-lite"
# model_id = "gemini-2.0-flash"
model_id = "gemini-3-flash-preview"


config = types.GenerateContentConfig(
    system_instruction="You are a file analyst. ",
    tools=[tool_logic],
    automatic_function_calling=types.AutomaticFunctionCallingConfig(
        disable=False, 
        maximum_remote_calls=10 
    )
)

chat = client.chats.create(model=model_id, config=config)   



while not False:
    user_prompt = input("\nUser: ")
    
    if user_prompt.lower() in ["exit", "quit", "bye", "q"]:
        print("Exiting...")
        break


    response = chat.send_message(user_prompt)


    while response.candidates and response.candidates[0].content.parts[0].function_call:
        part = response.candidates[0].content.parts[0]


        if part.function_call:
            call = part.function_call
            print(f"\n[System]: Executing {call.name}...")

            if call.name in tool_map:
                result = tool_map[call.name](**call.args)

                response = chat.send_message(
                    types.Part.from_function_response(
                        name=call.name,
                        response={'result': result}
                    )
                )

        if response.text:
            print(f"\nAgent: {response.text}\n-------\n")
            print(f"{response.candidates[0].content.parts[0].function_call}")


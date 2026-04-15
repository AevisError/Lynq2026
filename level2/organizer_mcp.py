from google import genai
from fastmcp import FastMCP
import cmds

print("in omcp")


client = genai.Client()


mcp = FastMCP("My Server")


@mcp.tool()
def list_files(directory):
    print("using list files...")
    
    return cmds.list_files(directory)


@mcp.tool()
def move_file(filename, category):
    print("using move files...")

    cmds.move_file(filename, category)
    #source_dir is not used, as all locations are taken in absolute addresses

@mcp.tool()
def read_file(filename):
    print("using read files...")

    cmds.read_file(filename=filename)

@mcp.tool()
def send_file(filename):
    print("using send req...")

    print(filename)
    myfile = client.files.upload(file=filename)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=["analyze this file. extract any and all details from it.",myfile]
    )
    print(response.text)
    return response.text


# @mcp.tool()
def deletefiles_incloud():
    print('My files:')
    for f in client.files.list():
        print(' ', f.name)
        client.files.delete(name=f.name)





'''

myfile = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=["Describe this audio clip", myfile]
)

'''

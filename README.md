# Lynq2026

Setup Instructions:


You most probably have os, shutil, and pathlib.
If using linux, you may choose to install via apt or via uv.

after installing everything, source .venv/bin/activate. this already has the gemini library installed.

LLM API: gemini. the code gives you the choice between 2.5-flash, 3.1-flash.

Sample Output:


User: organize all the files in ./ws/ into their respective folders in ./ws/

[System]: Executing list_files...
using list files...
list files is running: Listing /home/satya/Documents/code/Natural_stupidity/Upload/level2/ws
Warning: there are non-text parts in the response: ['function_call', 'function_call', 'function_call', 'function_call', 'function_call', 'function_call', 'function_call', 'function_call', 'function_call', 'function_call', 'function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.

[System]: Executing move_file...
using move files...
in move file: moving /home/satya/Documents/code/Natural_stupidity/Upload/level2/ws/fake.mp3.c to /home/satya/Documents/code/Natural_stupidity/Upload/level2/ws/Code
move is successful

[System]: Executing list_files...
using list files...
list files is running: Listing /home/satya/Documents/code/Natural_stupidity/Upload/level2/ws

[System]: Executing move_file...
using move files...
in move file: moving /home/satya/Documents/code/Natural_stupidity/Upload/level2/ws/acfile.c to /home/satya/Documents/code/Natural_stupidity/Upload/level2/ws/Code
move is successful

[System]: Executing list_files...
using list files...
list files is running: Listing /home/satya/Documents/code/Natural_stupidity/Upload/level2/ws/Code
.....


 

# Lynq2026

Welcome to the greatest roller coaster of terrible code made in 3 days that has probably used up around 10% of the water in the nile river because I forgot to change the name of a function once.

Get some coffee or Redbull before you start this, and make sure the next day is a holiday cuz you're gonna be knocked out cold by how efficient this code is

## Setup Instructions:


You most probably have os, shutil, and pathlib.
If using linux, you may choose to install via apt or via uv.
in any case, install the python packages listed in requirements.txt

after installing everything, run "source .venv/bin/activate" in that particular folder. this already has the gemini library installed.

## LLM API: Gemini. 
the code gives you the choice between 2.5-flash, 3.1-flash. 2.5 is the most reliable, as 3.1 seems to always be in demand.


## Sample Output:



User: organize all the files in ./ws/ into their respective folders in ./ws/

[System]: Executing list_files...
using list files...
list files is running: Listing ~/Natural_stupidity/Upload/level2/ws
Warning: there are non-text parts in the response: ['function_call', 'function_call', 'function_call', 'function_call', 'function_call', 'function_call', 'function_call', 'function_call', 'function_call', 'function_call', 'function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.

[System]: Executing move_file...
using move files...
in move file: moving ~/Natural_stupidity/Upload/level2/ws/fake.mp3.c to ~/Natural_stupidity/Upload/level2/ws/Code
move is successful

[System]: Executing list_files...
using list files...
list files is running: Listing ~/Natural_stupidity/Upload/level2/ws

[System]: Executing move_file...
using move files...
in move file: moving ~/Natural_stupidity/Upload/level2/ws/acfile.c to ~/Natural_stupidity/Upload/level2/ws/Code
move is successful

[System]: Executing list_files...
using list files...
list files is running: Listing ~/Natural_stupidity/Upload/level2/ws/Code
...
{rest of the output has been truncated}
 

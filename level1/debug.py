import os, shutil
import cmds, organizer_mcp




choice = int(input("\n 1- ls \n 2- mkdir \n 3- rmdir \n 4- validity \n 5- mvdir\n \
6- file moving sequence \n 7- readfile \n 8- send a message to Gemini\n\
enter choice: "))

match choice:
    case 1:
        abspath=os.path.abspath('.')
        cmds.list(abspath)
    
    case 2: 
        folname=str(input("enter folder name: "))
        cmds.makedir(folname)
    
    case 3: 
        folname=str(input("enter folder name: "))
        cmds.remdir(folname)
    
    case 4: 
        folname=str(input("enter folder name: "))
        cmds.valid(folname)
    
    case 5:
        objname=os.path.abspath(str(input("enter obj name: ")))
        destname=os.path.abspath(str(input("enter folder name: ")))
        cmds.move_file(objname, destname)   
    
    case 6:
        abspath=os.path.abspath('.')
        cmds.orchestra(abspath)
    case 7:
        filename=os.path.abspath(str(input("enter file name: ")))
        cmds.readfile(filename)
    
    case 8:
        message= "Explain in 5 sentences why Nandamuri Balakrishna \n\
 would be a better director for BITS Pilani than an IITian whom we'll call Mousse"
        
        print("would you like to send a custom message or send the default test message? \n\
            default test message:\n",message)
        
        choice = str(input("\n enter 'd' to send the default message,\n or type in your message: "))

        if (choice!='d'):
            message=choice
        organizer_mcp.sendmsg(message)
    
    case _:
        print("not found.")

'''
todo:

get file 
if file is:

    txt,pdf,csv:
        sendto docs folder

    mp3,jpg,png:
        sendto media folder
    
    py,c:
        sendto code folder
'''






'''
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="How does AI work?"
)
print(response.text)

'''

print("-------------\nfinished program \n")
os.system('aplay ./notif.wav & echo "exiting..."')

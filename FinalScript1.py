import os
import pathlib
os.system('cls')
me = os.environ["username"]
print("The user " + me + " will run this script")


def GetState():
    state = input(" What is the name of the state? ")
    return state;

def formatstate(mystate):
    length = len(mystate)
    if length < 8 :
        newState = mystate.ljust(8, '*')
        return newState;
    else:
        return mystate;         
#------------------------------------------------
message = " 1. Get information and display to screen \n"
message = message + " 2. Call user created function \n"
message = message + " 3. Write List of files to file \n"
message = message + " 4. Read specified file \n"
task = input(message + "\nEnter number of task to do: ")

if task == "1":
    companyName = "Dunwoody College"
    programName = "Computer Networking"
    uname = os.environ['USERNAME']
    classFirst = input("What is the name of your first class: ")
    classSecond = input("What is the name of your second class: ")
  
    print(" My company is " + companyName + " my program is " + programName + " and my username is " + uname )
    print(" My first class is " + classFirst + " my second class is " + classSecond  )

elif task == "2":
    myState = GetState()
    newState = formatstate(myState)
    print(" Old state is " + myState  +  " your new state is " + newState ) 

elif task == "3":
    fileOfFiles = input("Name of file to hold the files  ")
    fList = []
    for p in pathlib.Path('.').iterdir():
        if p.is_file():
            fList.append(p)
    with open(fileOfFiles, "w") as myFileWrite:
        myFileWrite.write("These are my files:\n")
        for f in fList:
            myFileWrite.write(f.name)
            myFileWrite.write("\n")

elif task == "4":
    fileToRead = input("Name of file to read  ")


    with open(fileToRead, "r+") as myFileRead:
        print(myFileRead.read())
import os
os.system('cls')
me = os.environ["username"]
print("The user " + me + " will run this script")

#------------------------------------------------
message = " 1. Get information and display to screen "
message = " 2. Call user created function "
message = " 3. Write List of files to file "
message = " 4. Read specified file "
task = input("Enter number of task to do: ")

def choice1():
    companyName = "Dunwoody College"
    programName = "Computer Networking"
    uname = "import os"
    classFirst = input = "Operating Systems"
    classSecond = input = "Scripting"

    print("My company is" + companyName + "my program is" + programName + "and my username is" + uname + "today")
    print("My first class is" + classFirst + "my second class is" + classSecond + "today")
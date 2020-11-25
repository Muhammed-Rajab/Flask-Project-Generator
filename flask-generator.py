import subprocess
import sys
import os
import time
from time import sleep

folder_name = sys.argv[1]

file_name = sys.argv[2]

if file_name[-3:] == ".py":
    file_name = file_name[:-3]

add_structured = sys.argv[3]

print("*"*40)
print("Parent directory name: ", folder_name)
print("Flask app filename: ", file_name)
print("Structured Folder: ", add_structured)
print("*"*40)
print("")

start = time.time()
try:

    print(f"Creating {folder_name}/\n")
    os.mkdir(f"{folder_name}")
    
    print(f"Changing Directory to {folder_name}\n")
    os.chdir(f"{folder_name}")

    print("Creating templates/\n")
    os.mkdir("templates")
    
    print("Creating static Folder")
    os.mkdir("static")

    # if user wants to create more structured project.
    if add_structured == "True":
        
        print("Changing directory to static\n")
        os.chdir("templates")

        print("Making css folder\n")
        os.mkdir("css")

        print("Making js folder\n")
        os.mkdir("js")
        
        print(f"Changing back directory to {folder_name}\n")
        os.chdir(f"../")
    
    print("Creating doc folder\n")
    os.mkdir("doc")

    print(f"Creating {file_name}.py file\n")
    sleep(1)
    with open(f'{file_name}.py', 'w') as file:
        print(f"Importing important libraries to {file_name}.py file.")
        file.writelines("""import flask\nfrom flask import Flask, render_template, request, redirect\napp = Flask(__name__)\n""")

    print("\nEverything went correct!\n")
    print('*'*40,"\nFinal project structure\n"+'*'*40,"\n")
    print(f"{folder_name}")
    print("----doc\n")
    print("----static\n")
    print("----templates\n")
    if add_structured == "True":
        print("--------css\n")
        print("--------js\n")

    print(f"{file_name}.py\n")

    end = time.time()

    print(f"Program executed succesfully in {(end-start)*1000} milliseconds.")
except FileExistsError as err:
    print(f"Folder Named {folder_name} already exists!. Please try a different folder name.")
    print("Python Error: ",err)
    exit()
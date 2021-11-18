# >>>>>>>>>>>>    5) Virtual Environments And Packages /  External Packages

# Third-Party Packages

# Central Repository : 
    # PyPI
    
# pip:

# built-in tool to install packages : 'pip'

    # syntax:
        # python3 -m pip install <package name>
        # Example:
            # DONT 'python3 -m pip install mypy'


# >>>>>>>>>>>>    5) Virtual Environments And Packages /  The Python Package Ecosystem_ (Video)

# Follow-along

#  ...
# 
# 
# # >>>>>>>>>>>>    5) Virtual Environments And Packages /  Dependencies

# Dependencies:

#   Dependancey is code that someone else write and that you use in your own project. the functionality of your own code 'depends' on the code you pulled in from an external source

# virtual environments enable you to work with a particular version of a given dependency (such as 'django') while simultaneously developing other rpojects with different versions, as opposed to a system wide install oef one of these packages which can only allow one version to be installed on your computer at a time.


# >>>>>>>>>>>>    5) Virtual Environments And Packages / Introduction to virtual environments

# VM - VIrtual Machine
    # VM's allow you to run a different OS on your current OS. Ex. run Linux on Mac.
    # you can create a VM with programs such as 'virtualbox'
# Virtual environments are a similar conccept
#     Python- an installation of Python
#         > Packages- Python modules and packages

# >>>>>>>>>>>>    5) Virtual Environments And Packages /  Virtual Environments_ (Video)

# What follows is the process (in terminal) of creating a virtual environment::

# Comp-Samuel:virtual_test admin$ python3 -m venv env
# Comp-Samuel:virtual_test admin$ ls
# env
# Comp-Samuel:virtual_test admin$ cd env
# Comp-Samuel:env admin$ ls
# bin		lib
# include		pyvenv.cfg
# Comp-Samuel:env admin$ bin ls
# -bash: bin: command not found
# Comp-Samuel:env admin$ cd bin
# Comp-Samuel:bin admin$ ls
# Activate.ps1	pip		python3
# activate	pip3		python3.9
# activate.csh	pip3.9
# activate.fish	python
# Comp-Samuel:bin admin$ ../..
# -bash: ../..: is a directory
# Comp-Samuel:bin admin$ pwd
# /Users/admin/CodingNomads/Python 201/05_venvs-and-packages/virtual_test/env/bin
# Comp-Samuel:bin admin$ cd ../..
# Comp-Samuel:virtual_test admin$ pwd
# /Users/admin/CodingNomads/Python 201/05_venvs-and-packages/virtual_test
# Comp-Samuel:virtual_test admin$ cd ..
# Comp-Samuel:05_venvs-and-packages admin$ pwd
# /Users/admin/CodingNomads/Python 201/05_venvs-and-packages
# Comp-Samuel:05_venvs-and-packages admin$ cd .
# Comp-Samuel:05_venvs-and-packages admin$ pwd
# /Users/admin/CodingNomads/Python 201/05_venvs-and-packages
# Comp-Samuel:05_venvs-and-packages admin$ ls
# 05_01_venv_training.txt
# 05_02_two_versions.txt
# 05_03_explore_packages.txt
# 05_04_environment_settings.py
# virtual_test
# workshop_02_04.py
# Comp-Samuel:05_venvs-and-packages admin$ cd virtual_test/
# Comp-Samuel:virtual_test admin$ pwd
# /Users/admin/CodingNomads/Python 201/05_venvs-and-packages/virtual_test
# Comp-Samuel:virtual_test admin$ source
# -bash: source: filename argument required
# source: usage: source filename [arguments]
# Comp-Samuel:virtual_test admin$ source env/bin/activate
# (env) Comp-Samuel:virtual_test admin$ pip install django
# Collecting django
#   Downloading Django-3.2.9-py3-none-any.whl (7.9 MB)
#      |                                | 10 kB 4.6 MB/s eta 0     |          

#   ... {downloading stuff] ...

# Collecting asgiref<4,>=3.3.2
#   Downloading asgiref-3.4.1-py3-none-any.whl (25 kB)
# Installing collected packages: sqlparse, pytz, asgiref, django
# Successfully installed asgiref-3.4.1 django-3.2.9 pytz-2021.3 sqlparse-0.4.2
# WARNING: You are using pip version 21.2.3; however, version 21.3.1 is available.
# You should consider upgrading via the '/Users/admin/CodingNomads/Python 201/05_venvs-and-packages/virtual_test/env/bin/python3 -m pip install --upgrade pip' command.
# (env) Comp-Samuel:virtual_test admin$ clear

# (env) Comp-Samuel:virtual_test admin$ pip freeze
# asgiref==3.4.1
# Django==3.2.93
# pytz==2021.3
# sqlparse==0.4.2
# (env) Comp-Samuel:virtual_test admin$ pip freeze > requirements.txt
# (env) Comp-Samuel:virtual_test admin$ ls
# env			requirements.txt
# (env) Comp-Samuel:virtual_test admin$ vim requirements.txt 
# (env) Comp-Samuel:virtual_test admin$ deactivate

# # >>>>>>>>>>>>    5) Virtual Environments And Packages /  Working with virtual envoronments

# creating a virtual Environment:
#     create:
#         python3 -m venv your_venv_name
#             (bash command , where youre using the program python3, which is your system-wide installation of python3, to call one of its built-in modules (-m) called venv)
#     activate:
#         source your_env_name/bin/activate        
#             once inside:
#                 you can install packages like 'mypy':
#                     python3 -m pip install mypy
#     deactivate:
#         deactivate



# # >>>>>>>>>>>>    5) Virtual Environments And Packages / Introduction To Environment Variables

# Environment variables:
# (in bash) -not specific to python
#     most famous one: $Path

# use cases:
#     you can access the value of your envirnoment vaeriables anywhere in your project without ever spelling out the actual value of that variable. instead you can refer to it through the environment variable defined in bash
#         allows you to work with secrets and passwords throughout your project

# !! NEVER let sensitive information make it to github. (use environmental variables for this.)    


# # >>>>>>>>>>>>    5) Virtual Environments And Packages / Working With Environment Variables

# Working With Environment Variables
#   to display all current variables and how theyre being defined:
#       open up CLI and type:
#         printenv

    # you can check the value of each value by typing the command:
        # echo $<NAME>

# Adding And Removing Environment Variables:

# you can (+)add(+) a new environment variable with:
#     export <NAME>=<Value>
    # replace <NAME> with the new environment variable you want to add
    # replace <VALUE> with the value you ant to assign to that environment variable
    # example:
    #     export DAY=sunday

# (-)remove(-) an environment variable by calling:
#     unset <NAME>
#     example:
#         unset<DAY>
# 

# # >>>>>>>>>>>>    5) Virtual Environments And Packages / Virtual Environment Variables

# avoid system-wide ANYTHING
#     this goes for setting variables

# setting them within the virtual environment, 
    # they are called "virtual environment variables"


# -> open the virtual env 'venv'

# ------> see the 'activate' script in /venv

# Unsetting Virtual Envorinment Variables:

# IMPORTANT:
#     To unset a virtual environment variable, 
#     you add an unset command 
#     to the deactivate command section 
#     in your Bash activate script. 
#     The code in this part of the script runs 
#     every time you deactivate your virtual environment.\

    # example: (to unset the variable MY_SUPER_SECRET_SECRET)
        # deactivate () {
        #     unset MY_SUPER_SECRET_SECRET
        #     # Lots of other code
        # }

# Setting Virtual Environment Variables

# you can set a VEV in the same way in the script but not with 'export' directly to your terminal, 
# you add it as a new line at the end of your activate script
# Info: You'll need to wrap the value of your virtual environment variable inside of double-quotes ("").


# Accessing Virtual Environment Variables:

# To use one of your virtual environment variables inside of your Python project, you need to access it. You can do that for example with Python's os module that comes packaged with the standard library:

# ex:
# import os

# secret = os.environ['MY_SUPER_SECRET_SECRET']
# print(secret)

# Note: Make sure that you add your virtual environment folder to your .gitignore file, or you'll end up pushing your secrets to GitHub after all.


import os
secret = os.environ['ANOTHER_ONE']


print(f"if youre down on your luck, just call for {secret}")
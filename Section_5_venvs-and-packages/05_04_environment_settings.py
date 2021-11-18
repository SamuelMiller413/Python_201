# Create a virtual environment and edit the activation script to add
# the following information:
# 
# - ENVIRONMENT="development"
# - SECRET="i ate your sweets"
# 
# Then write the necessary code to access and print the values of these
# two environment variables in this script.

import os
environment_var = os.environ["ENVIRONMENT"]
secre_var = os.environ["SECRET"]

print(f"In order to complete this lab, I must print both {environment_var} and {secre_var}.\n\
    So now it's done.")


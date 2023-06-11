import fire
import sys
# Import other functions created in the different file.
from fileio.csvUtils import *
from risk_questions import *

#Check if the user is already registered or not
def validate_user_login_info(username,password):
    user_data=load_file()
    if username in user_data:
        if user_data[username]==password:
            return True
        return False
    return False


#After Login Successful integrate matt questionary for the user.
def login():
    username=input("Enter your user name:")
    password=input("Enter your Password:")
    if validate_user_login_info(username,password):
        print("login successful")
        call_question()
    else:
        print("login unsuccessful")
        login()     

#New User First Time Register\signup.
def register():
    new_user_name=(input("choose your user name:"))
    user_data=load_file()
    if new_user_name in user_data:
        print("This Username already exist")
        return
    new_user_password=(input("choose your Password:"))
    append_csv(new_user_name,new_user_password)
    call_question()
    
    
      
def run():
    #will ask question about new user or existing user
    #if new user call register else call login 
    existing_user = input("Are you an existing user? Please enter Y/N")
    existing_user = existing_user.upper() # fixes case errors
    if existing_user == 'Y':
        login()
    elif existing_user =='N':
        register()
    else:
        sys.exit("Sorry, You have entered an incorrect input.")

#First main funtion will run.
if __name__ == "__main__":
    fire.Fire(run) 

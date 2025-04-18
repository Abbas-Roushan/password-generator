########################################
#Password Generator 
########################################
import random
import string
import os 


### Program Setting 
settings = {
    "lower" : True , 
    "upper" : True , 
    "symbol" : True ,
    "number" : True ,
    "space" : True ,
    "length" : 8
}



def get_password(v,MAX_LENGTH = 15,MIN_LENGTH = 5):
    
    while True:
        user_input_password = input("Enter password {v} : ")
        
        if user_input_password == "":
            return v
        
        if user_input_password.isdigit():
            user_input_pass = int(user_input_password)
            if MIN_LENGTH < user_input_pass < MAX_LENGTH:
                return user_input_password
            print("Invalid input length for password")
        else:
            print("Invalid input ...")
            print("Try again !")
        

def get_y_n(k,v):
    while True:
        user_input = input(f'Option {k} Default {v} '
                           '( y /n / Default )   : ')
        
        if user_input == "":
            return v
        
        if user_input.lower() in ['y' , 'n']:
            return 
        
        print("wrong input , try again .....")
    

def get_setting(settings):
    for k,v in settings.items():
        if k != "length":
            user_input = get_y_n(k,v)
            settings[k] = user_input
        else:
            user_password = get_password(v)
            settings[k] = user_password
    
    return settings , user_password


def upper_char_gen():
    return random.choice(string.ascii_uppercase)

def lower_char_gen():
    return random.choice(string.ascii_lowercase)

def symbol_char_gen():
    return random.choice(string.punctuation)

def  number_gen():
    return str(random.choice([n for n in range(10)]))


def pga(true_item):
    if len(true_item) != 0: 
        choice = random.choice(true_item)      
        if choice == "upper":
            return  upper_char_gen()
        if choice == "lower":
            return lower_char_gen() 
        if choice == "symbol":
            return  symbol_char_gen()
        if choice == "number":
            return number_gen()
        if choice == "space":
            return " "
    else:   
        print("check the setting , you set all main setting to no !!")
        get_setting(settings)




def password_generator(settings):
    pass_length = settings['length']
    final_password = ""
    true_item = [k for k, v in settings.items() if v and k != 'length']
  
    for _ in range(int(pass_length)):
        final_password += pga(true_item)

    return final_password


def check_need_setting():
    while True:
        ask_user = input("Do you want to change Setting: ")
        if ask_user.lower() in ["y","n"]:
            if ask_user == "n":
                return False
            break
        else:
            print("invalid input use y or n ")
            
    return True        




def multi_password_gen():
    if check_need_setting():
        get_setting(settings)
        
    password = password_generator(settings)
    print(f"Generated password is : {password}")

    while True:
        ask_user = input("Do you need multi password: (y/n)")
        if ask_user.lower() in ["y","n"]:
            if ask_user == "n":
                print("good bye!!")
                break
            else:
                password = password_generator(settings)
                print(f"Generated password is : {password}")
        else:
            print("user only y and n to answer!")

        

def run():
    os.system('cls')
    print("*" * 20)
    multi_password_gen()
    print("*" * 20)


run()
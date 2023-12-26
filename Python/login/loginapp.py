import csv


def main():
    username=login()
    if username:
        greet(username)


def login():
    username_exists=False
    login_status=False
    username=input('Please insert your username: ')
    with open('login_credentials.csv','r') as current_file:
        open_file=csv.DictReader(current_file)
        for line in open_file:
            if username == line['username']:
                username_exists=True
                while(True):
                    temp=input("\nEnter 'q' to quit \n\nEnter your password: ")
                    if line['password']==temp:
                        print("Logged in!")
                        return username
                        break
                    elif temp.lower()=='q':
                        break
                    else:
                        print("Wrong password.")
                        continue     
        if username_exists==False:
            prompt="Theres no account with that username in our account, "
            prompt+="Would you like to sign up?(y/n):"
            if 'y'==input(prompt).lower():
                signup()
            
                

def signup():
    username=str(input("Please input the username you'd like to use: "))
    while (True):
        prompt="Enter q if you wish to quit \n"
        prompt+="Please input the password you'd like to associate with "
        prompt+='"%s" :' %(username)
        password=input(prompt)
        if password.lower() == 'q' :
            break
        elif password==username:
            print("The password can't be the same as the username!")
            continue

        temp=input("Please input your password again: ")
        if password==temp:
            write_to_csv(username,password)
            break
        else:
            print("The two passwords didnt match, please try again!")
            continue

def write_to_csv(username,password):
    with open('login_credentials.csv', 'r+') as current_file:
        for index,row in enumerate(csv.reader(current_file)):
            if index ==0:
                fieldnames=row
            else:
                break
        open_file = csv.DictWriter(current_file,fieldnames=fieldnames)
        open_file.writerow({'username':username,'password':password})

def greet(username):
        print("Welcome back %s!" %(username))


main()
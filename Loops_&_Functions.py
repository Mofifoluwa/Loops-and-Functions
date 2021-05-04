import datetime
import os
import random

database = {}



def others():
    print('Would you like to do anything else?')
    print('1. Yes')
    print('2. No')

    response = int(input('Please select an option'))

    if(response == 1):
        bankOperations()
    elif(response == 2):
        print('Thank you for using our service')
        quit()

def withdrawalOperation():
    amount = int(input('How much would you like to withdraw? \n'))
    print('Take your cash')
    others()

def depositOperation():
    deposit = int(input('How much would you like to deposit? \n'))
    print('Current balance')
    others()

def complaintOperation():
    complaint = input('What issue will you like to report? \n')
    print('Thank you for contacting us')
    others()

def logoutOperation():
    exit()

def accountNumberGeneration():
    genNum = random.randrange( 1111111111, 9999999999 )
    return genNum
 



def login():
    print('Log in to your account')

    isLoginSuccessful = False

    while isLoginSuccessful == False:
        userAccountNumber = int(input('What is your account number? \n'))
        password = input('What is your password? \n')
        print(database.items())

        for accountNumber, userDetails in database.items():
            isEqual = (accountNumber == userAccountNumber)
            if(isEqual):
                if(userDetails[3] == password):
                    isLoginSuccessful = True
                else:
                    print('Invalid password')
            else:
                print('Invalid acc no')
        


    bankOperations(userDetails)   




def bankOperations(user):
    print("Welcome %s %s " % (user[0], user[1]))
    now = datetime.datetime.now()
    print('Current date and time: ')
    print(now.strftime('%d-%m-%y'))
    print(now.strftime('%H:%M:%S'))
    print('These are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')
    


    isSelectedOptionValid = False
    

    selectedOption = int(input('Please select an option:'))

    if(selectedOption == 1):
        withdrawalOperation()
        
    elif(selectedOption == 2):
        depositOperation()
        
    elif(selectedOption == 3):
        complaintOperation()
        
    elif(selectedOption == 4):
        logoutOperation()

        
    else:
        print('Invalid option selected')
        bankOperations(user)





        
def register():
    print("Boogdiddy Bank of Africa is happy to bring you on board")
    print("Please fill in corresponding details to the following the questions to register")
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a strong password \n")

    accountNumber = accountNumberGeneration()
    print(accountNumber, '-----------reg------------')

    database[accountNumber] = [ first_name, last_name, email, password ]

    print('Your account has been created')

    print('Your account number is %s' % accountNumber)

    login()


def init():

    isValidOptionSelected = False
    print('Welcome to Boogdiddy bank of Africa')

    while isValidOptionSelected == False:

        haveAccount = int(input('Do you have an account with us? 1. Yes 2. No \n'))

        if (haveAccount) == 1:
            isValidOptionSelected = True
            login()

        elif haveAccount == 2:
            isValidOptionSelected = True
            register()
        else:
            print('Oops, You selected an invalid option')
init()

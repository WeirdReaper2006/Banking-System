import json
import os

#Admin accounts dictionary
AdminAccounts = {
    "90001": {
        "Password": "adminpass1",
        "UserName": "Ahmed",
        "Email": "Ahmed@gmail.com"
    },
    "90002": {
        "Password": "adminpass2",
        "UserName": "Usman",
        "Email": "Usman@gmail.com"
    }
}
UserFile = 'UserInfo.json'

def UpdateUserFile(): #Method to Update User Accounts File
    with open(UserFile, 'w') as f:
        json.dump(UserAccounts, f,  indent=4)


def LoadUserFile(): #Method of loading all Accounts in a Dictionary
    global UserAccounts
    if os.path.exists(UserFile):
        with open(UserFile, 'r') as f:
            UserAccounts = json.load(f)
    else:
        UserAccounts = {}

UserAccounts = {} #Dictionaries Holding User Profiles
LoadUserFile() #Loads User File When the Program is started

def RegistrationPage(): #User Registration Page

    NewUserID = f"{int(max(UserAccounts.keys(), default='00000')) + 1:05d}" #Generate a New UserID

    UserNameInput = input("Enter UserName: ") #Asking For Profile Details
    while len(UserNameInput) < 5 or len(UserNameInput) > 15 :
        UserNameInput = input("Invalid Range! Enter Username bw 5 and 15 : ")

    PasswordInput = input("Enter Password: ") #Checks whether Password is between 5 and 13 characters
    while len(PasswordInput) < 5 or len(PasswordInput) > 13 :
        PasswordInput = input("Invalid Range! Enter Password bw 5 and 13 : ")

    ContactInput = input("Enter Contact: ") #Check Whether Contact input is valid
    while not ContactInput.isnumeric() or len(ContactInput) != 11:
        ContactInput = input("Invalid Contact! Enter Valid Contact: ")

    EmailInput = input("Enter Email: ") #Check Whether Email input is valid
    while'@' not in EmailInput or '.com' not in EmailInput or EmailInput.index('@') > EmailInput.index('.com'):
        EmailInput = input("Invalid Email! Please enter a valid email address: ")
    #Saving New User Details into Dictionary
    UserAccounts[NewUserID] = {
        'Password': PasswordInput,
        "Balance": "0",
        'UserName': UserNameInput,
        'Contact': ContactInput,
        'Email': EmailInput
    }


    UpdateUserFile() #Updating Dictionary for newly added user

    print(f"User {UserNameInput} registered successfully with ID: {NewUserID}")
    print("Thank you for Registering! You may now login.")
    print("Returning to Main Menu....")
    print("-----------------------------------------")

    Introduction() #Returns User back to Start menu

def Introduction(): #Introduction Page for User/Admin
    global UserID
    UserID = ""
    print("0 - Login")
    print("1 - Register")
    print("* - Leave Page")
    UserChoice = input("Enter Choice: ")
    while UserChoice != "0" and UserChoice != "1" and UserChoice != "*":  #Checks for valid Value 0 or 1
        UserChoice = str(input("Invalid Input! Enter Choice: "))
    if UserChoice == "0":
        LoginPage()
    elif UserChoice == "1":
        RegistrationPage()
    else:
        print("Thank you for visting Pacific Bank!")

def LoginPage(): #Login Page for User or Admin
    global UserID
    global UserPassword
    global CurrentUser
    CurrentUser = None  # Check Whether Admin or User
    UserID = input("Enter ID: ")
    UserPassword = input("Enter Password: ")


    if UserID in AdminAccounts and AdminAccounts[UserID]['Password'] == UserPassword: #Checks Whether ID is Admin
        CurrentUser = "Admin"
        print("-----------------------------------------")
        print(f"Admin login successful! Welcome {AdminAccounts[UserID]['UserName']}")
        AdminMenu() #Sends  user to User Menu
    elif UserID in UserAccounts and UserAccounts[UserID]['Password'] == UserPassword: #Checks Whether ID is User
        CurrentUser = "User"
        print("-----------------------------------------")
        print(f"User login successful! Welcome {UserAccounts[UserID]['UserName']}")
        UserMenu() #Sends User to UserMenu
    else:
        print("-----------------------------------------")
        print("Invalid ID or Password. Please try again.") #Invalid Input
        print("-----------------------------------------")
        print("")
        Introduction()


def AdminMenu(): #Shows Admin their menu
    global CurrentUser
    global UserID
    print("")
    print("\033[4mAdmin Menu:\033[0m")
    print("0 - View User Details")
    print("1 - Update User Password")
    print("2 - Delete User Account")
    print("3 - Logout")
    print("")
    AdminChoice = input("Enter Choice: ")
    while AdminChoice != "0" and AdminChoice != "1" and AdminChoice != "2" and AdminChoice != "3":
        AdminChoice = input("Invalid Choice! Enter valid Choice: ")
    #Selects Between Different options. Different methods allow for admin to return to Admin Page in future
    if AdminChoice == "0":
        AdminViewUserDetails()
    elif AdminChoice == "1":
        AdminUpdateUserPassword()
    elif AdminChoice == "2":
        AdminDeleteUserAccount()
    elif AdminChoice == "3":  #Admin Logging out
        print("Logging out...")
        print("----------------------------------")
        print("")
        Introduction()


def AdminViewUserDetails():  #0 - Admin Viewing User Profiles

    AdminChoice = None
    while AdminChoice != "*":
        UserToBeChecked = input("Enter UserID to be searched: ")
        if UserToBeChecked in UserAccounts:
            print("--------------------------------------")
            print("UserID: ", UserToBeChecked)
            print("Password: ", UserAccounts[UserToBeChecked]['Password'])
            print("UserName: ",UserAccounts[UserToBeChecked]['UserName'])
            print("Balance: $", UserAccounts[UserToBeChecked]['Balance'].strip())
            print("Contact info: ", UserAccounts[UserToBeChecked]['Contact'])
            print("Email: ", UserAccounts[UserToBeChecked]['Email'])
        else:
            print("Invalid UserID or User does not Exists!")


        print("")
        print("")
        print("1 - Search Another User's Details")
        print("* - Return to Admin Menu")
        AdminChoice = input("Enter Choice: ")
        while AdminChoice != "*" and AdminChoice != "1":
            AdminChoice = input("Invalid Choice! Enter valid choice: ")

    print("Returning to Admin Menu...")
    print("-----------------------------------------")
    AdminMenu()


def AdminUpdateUserPassword(): # 1 - Admin Updating User Password

    AdminChoice = None
    while AdminChoice != "*":
        UserToBeChecked = input("Enter UserID: ")
        if UserToBeChecked in UserAccounts:
            OldPassword = UserAccounts[UserToBeChecked]['Password']
            NewPassword = input("Enter New Password: ")
            while len(NewPassword) <5 or len(NewPassword) > 13:
                NewPassword = input("Invalid! Enter Password between 5 and 13 characters: ")
            UserAccounts[UserToBeChecked]['Password'] = NewPassword
            UpdateUserFile() #Save New Password to File
            print("--------------------------------")
            print(f'Password of User:{UserAccounts[UserToBeChecked]['UserName']}, updated from {OldPassword} to {NewPassword}')
            print("---------------------------------")
        else:
            print("---------------------------------")
            print("Error! Invalid User ID.")
            print("---------------------------------")

        print("")
        print("1 - Update Another User Password")
        print("* - Return to Admin Menu")
        AdminChoice = input("Enter Choice: ")
        while AdminChoice != "*" and AdminChoice != "1":
            AdminChoice = input("Invalid Choice! Enter valid choice: ")

    print("Returning to Admin Menu...")
    print("-----------------------------------------")
    AdminMenu()

def AdminDeleteUserAccount(): #2 - Admin Deleting a User Account

    AdminChoice = None
    while AdminChoice != "*":
        UserToBeDeleted = input("Enter UserID for Account to be deleted: ")
        if UserToBeDeleted in UserAccounts:
            print("0- Confirm")
            AdminChoice = input("Enter Choice: ")
            if AdminChoice == "0":
                print("---------------------------------")
                print(f' User: {UserAccounts[UserToBeDeleted]['UserName']} with UserID {UserToBeDeleted} Deleted Successfully!')
                print("---------------------------------")
                del UserAccounts[UserToBeDeleted]
                UpdateUserFile()
        else:
            print("---------------------------------")
            print(f'User with UserID {UserToBeDeleted} not found.')
            print("---------------------------------")

        print("")
        print("1 - Delete Another User")
        print("* - Return to Admin Menu")
        AdminChoice = input("Enter Choice: ")
        while AdminChoice != "*" and AdminChoice != "1":
            AdminChoice = input("Invalid Choice! Enter valid choice: ")

    print("Returning to Admin Menu...")
    print("-----------------------------------------")
    AdminMenu()

def UserMenu(): #Shows User their menu
    global CurrentUser
    global UserID
    print("")
    print("\033[4mUser Menu:\033[0m")
    print("0 - Profile Menu")
    print("1 - Check Balance")
    print("2 - Transfer Funds")
    print("3 - Deposit Funds")
    print("4 - Withdrawal Funds")
    print("5 - Logout")
    print("")
    UserChoice = input("Enter Choice: ")
    while UserChoice != "0" and UserChoice != "1" and UserChoice != "2" and UserChoice != "3" and UserChoice != "4" and UserChoice != "5":
        UserChoice = input("Invalid Choice! Enter valid Choice: ")
    # Selects Between Different options. Different methods allow for admin to return to Admin Page in future
    if UserChoice == "0":
        UserProfileMenu()
    elif UserChoice == "1":
        UserViewBalance()
    elif UserChoice == "2":
        UserTransferFunds()
    elif UserChoice == "3":
        UserDepositFunds()
    elif UserChoice == "4":
        UserWithdrawFunds()
    elif UserChoice == "5":  # User Logging out
        print("Logging out...")
        print("----------------------------------")
        print("")
        Introduction()

def UserProfileMenu(): # 0 - View profile
    UserChoice = None
    while UserChoice != "*":
        print("-----------------------------------")
        print("")
        print("\033[4mUser Profile Menu:\033[0m")
        print("0 - Display User Info")
        print("1 - Update UserName")
        print("2 - Update Password")
        print("3 - Update Contact Info")
        print("4 - Update Email")
        print("* - Return to User Menu")
        print("")
        UserChoice = input("Enter Choice: ")
        while UserChoice != "0" and UserChoice != "1" and UserChoice != "2" and UserChoice != "3" and UserChoice != "4" and UserChoice != "*":
            UserChoice = input("Invalid Choice! Enter valid choice: ")
        if UserChoice == "0":
            UserProfileView()
        elif UserChoice == "1":
            UserUsernameUpdate()
        elif UserChoice == "2":
            UserUpdatePassword()
        elif UserChoice == "3":
            UserUpdateContact()
        elif UserChoice == "4":
            UserUpdateEmail()
    print("Returning to user menu...")
    print("-------------------------------------")
    print("")
    UserMenu()


def UserViewBalance(): # 1- Check Balance
    print("------------------------------------")
    print(f'Current Balance: ${UserAccounts[UserID]['Balance']}')
    print("------------------------------------")
    print("")
    UserMenu()
def UserTransferFunds(): # 2 - Trasfer Funds
    UserChoice = None
    while UserChoice != "*":
        UserTransfer = input("Enter Recepeint ID: ")
        if UserTransfer in UserAccounts:
            AmountTransfer = int(input("Enter Transfer Amount: $"))
            if AmountTransfer > int(UserAccounts[UserID]['Balance']):
                print(f'Insufficient Amount.You have ${UserAccounts[UserID]['Balance']} Remaining')
            else:
                NewBalanceSender = int(UserAccounts[UserID]['Balance']) - AmountTransfer
                UserAccounts[UserID]['Balance'] = str(NewBalanceSender)
                NewBalanceRecepient = int(UserAccounts[UserTransfer]['Balance']) + AmountTransfer
                UserAccounts[UserTransfer]['Balance'] = str(NewBalanceRecepient)
                print("------------------------------------")
                print(f'${AmountTransfer} sent to {UserAccounts[UserTransfer]['UserName']} of ID:{UserTransfer}. New Balance: ${UserAccounts[UserID]['Balance']}')
                print("------------------------------------")
                UpdateUserFile()
        else:
            print("Invalid User ID.")

        print("")
        print("1 - Transfer Again")
        print("* - Return to User Menu")
        UserChoice = input("Enter Choice: ")
        while UserChoice != "*" and UserChoice != "1":
            UserChoice = input("Invalid Choice! Enter valid choice: ")

    print("Returning to User Menu...")
    print("-----------------------------------------")
    print("")
    UserMenu()

def UserDepositFunds(): # 3 - Deposit Funds
    UserChoice = None
    while UserChoice != "*":
        AmountDeposit = int(input("Enter Amount to Deposit: $"))
        NewBalance = int(UserAccounts[UserID]['Balance']) + AmountDeposit
        UserAccounts[UserID]['Balance'] = str(NewBalance)
        print("------------------------------------")
        print(f'Amount ${AmountDeposit} added. New Balance: ${UserAccounts[UserID]['Balance']}')
        print("------------------------------------")
        UpdateUserFile()

        print("")
        print("1 - Deposit Again")
        print("* - Return to User Menu")
        UserChoice = input("Enter Choice: ")
        while UserChoice != "*" and UserChoice != "1":
            UserChoice = input("Invalid Choice! Enter valid choice: ")

    print("Returning to User Menu...")
    print("-----------------------------------------")
    print("")
    UserMenu()
def UserWithdrawFunds(): # 4 - Withdraw Funds
    UserChoice = None
    while UserChoice != "*":
        AmountWithdrawal = int(input("Enter Amount to Withdraw: $"))
        if AmountWithdrawal > int(UserAccounts[UserID]['Balance']):
            print(f'Insufficient Balance. You have ${UserAccounts[UserID]['Balance']} Remaining')
        else:
            NewBalance = int(UserAccounts[UserID]['Balance']) - AmountWithdrawal
            UserAccounts[UserID]['Balance'] = str(NewBalance)
            print("------------------------------------")
            print(f'${AmountWithdrawal} Withdrawed. New Balance: ${UserAccounts[UserID]['Balance']}')
            print("------------------------------------")
            UpdateUserFile()

        print("")
        print("1 - Withdrawal Again")
        print("* - Return to User Menu")
        UserChoice = input("Enter Choice: ")
        while UserChoice != "*" and UserChoice != "1":
            UserChoice = input("Invalid Choice! Enter valid choice: ")

    print("Returning to User Menu...")
    print("-----------------------------------------")
    print("")
    UserMenu()

def UserProfileView():
    print("-----------------------------------")
    print("\033[4mUser Info:\033[0m")
    print(f'UserID: {UserID}')
    print(f'Password: {UserAccounts[UserID]['Password']}')
    print(f'Username: {UserAccounts[UserID]['UserName']}')
    print(f'Balance: ${UserAccounts[UserID]['Balance']}')
    print(f'Contact Info: {UserAccounts[UserID]['Contact']}')
    print(f'Email: {UserAccounts[UserID]['Email']}')
    print("")
    print("Returning to Profile Menu...")
    UserProfileMenu()

def UserUsernameUpdate():

    OldUsername = UserAccounts[UserID]['UserName']
    NewUsername = input("Enter new username: ")
    while len(NewUsername) < 5 or len(NewUsername) > 15:
        NewUsername = input("Invalid Range! Enter Username bw 5 and 15 characters: ")
    UserAccounts[UserID]['UserName'] = NewUsername
    print(f'Username updated from {OldUsername} to {NewUsername}')
    UpdateUserFile()
    print("Returning to Profile Menu...")
    UserProfileMenu()

def UserUpdatePassword():
    OldPassword = UserAccounts[UserID]['Password']
    OldPasswordConfirm = input("Enter current Password: ")
    if OldPasswordConfirm == OldPassword:
        NewPassword = input("Enter new password: ")
        while len(NewPassword) < 5 or len(NewPassword) > 13:
            NewPassword = input("Invalid Range! Enter Password bw 5 and 13 characters: ")
        UserAccounts[UserID]['Password'] = NewPassword
        print(f'Password updated from {OldPassword} to {NewPassword}')
        UpdateUserFile()
    else:
        print("Invalid Current Password")

    print("Returning to Profile Menu...")
    UserProfileMenu()

def UserUpdateContact():
    OldContact = UserAccounts[UserID]['Contact']
    NewContact = input("Enter new contact: ")
    while len(NewContact) != 11 or not NewContact.isnumeric():
        NewContact = input("Invalid Range! Enter Password of 11 digits Only : ")
    UserAccounts[UserID]['Contact'] = NewContact
    print(f'Contact updated from {OldContact} to {NewContact}')
    UpdateUserFile()
    print("Returning to Profile Menu...")
    UserProfileMenu()

def UserUpdateEmail():
    OldEmail = UserAccounts[UserID]['Email']
    NewEmail = input("Enter Email: ")  # Check Whether Email input is valid
    while '@' not in NewEmail or '.com' not in NewEmail or NewEmail.index('@') > NewEmail.index('.com'):
        NewEmail = input("Invalid Email! Please enter a valid email address: ")
    UserAccounts[UserID]['Email'] = NewEmail
    print(f'Email updated from {OldEmail} to {NewEmail}')
    UpdateUserFile()
    print("Returning to Profile Menu...")
    UserProfileMenu()
#Call the function to test
Introduction()
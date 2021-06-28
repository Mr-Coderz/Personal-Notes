import json

#This program allows you to make personal accounts and store your personal notes in them
#No one can access your notes unless they know your username or password
#Or unless they see the main.json file
#This program remembers your id and notes even if you stop the program
#Please report for any bugs or errors

main = {}   #The main dictionary where all information is stored


def register():
  #registers a new user
    global UserNotes
    print('\nREGISTERATION')
    user = input('\tUsername: ')
    password = input('\tPassword: ')
    if pss_check(password):
      if user in main:
        print("Sorry, that username is taken.")
        return False
      main[user] = {'password':password,'notes':[]}
      UserNotes = main[user]["notes"]
      SaveData()
      return True

def login():
  #login
    global UserNotes
    print('\nLOGIN')
    user = input('\tPlease enter your username: ')
    password = input('\tPlease enter your password: ')
    try:
        if main[user]['password'] == password:
            print('\nSucessful Login\n')
            UserNotes = main[user]["notes"]
            return True
        else:
            print('\nWrong Username or Password')
            return False
    except:
        print('\nWrong Username or Password')
        return False

def LoadData():
  #loads data from the json file and converts it into a dictionary
    global main
    with open('main.json','r') as f:
        main = json.load(f)

def SaveData():
  #Saves the main dictionary into a json file
    with open('main.json','w') as f:
        json.dump(main,f,indent=4)

def del_acc():
  #deletes the specified account
    global main
    print('\nDELETE ACCOUNT\n')
    acc = input('\tUsername: ')
    if acc in main:
      pss = input('\tPassword: ')
      if pss == main[acc]['password']:
        del main[acc]
        print('\nAccount deleted successfully')
        SaveData()
      else:
        print('\nWrong Password')
    else:
      print('\nNo such account exists')

def pss_check(password):
  #Checks if the user password is strong enough
  lower = False
  digit = False
  upper = False
  misc = False
  if len(password) >= 8:
    for char in password:
      if char.isdigit():
        digit = True
        break
    if digit:
      for char in password:
        if char.islower():
          lower = True
          break
      if lower:
        for char in password:
          if char.isupper():
            upper = True
            break
        if upper:
          chars = set('!@#$%^&*/-+:;,<>.?/|_=`~')
          if any((c in chars) for c in password):
            misc = True
          if misc:
            return True
  if not misc:
    print('\nWeak Password')
    #Uncomment line 102 and comment line 103 if you want to disable password strength check
    # return True
    return False

def add_notes(UserNotes):
  #Adds new notes
  print('enter q to exit\n')
  while True:
      note = input('\tNew Note: ')
      if note == 'q':
          break
      else:
          UserNotes.append(note)
      return UserNotes

def del_notes(Usernotes):         
  #Deletes notes which user wants to delete
  print('enter q to exit\n')
  while True:
    inde =(input(f"The index of the note(Starting from 1, '{UserNotes[0]}': "))
    if inde == 'q':
      SaveData()
      break
    else:
      index = int(inde) - 1
      try:
        gg =  Usernotes.pop(index)
        print(f"Note- '{gg}' Deleted succesfull")
      except IndexError:
        print(f"This indes is out of range. The last index is {len(Usernotes)} which is of {Usernotes[-1]}")
  return Usernotes


LoadData()

while True:
  #Ask user what he wants to do
    Input = input("\nEnter 'register' if you want to register,\nEnter 'login' if you want to login,\nEnter 'q' if you want to quit,\nOr enter 'd' if you want to delete an account\n : ")
    if Input.lower() == 'register':
      if not register():
        continue
    elif Input.lower() == "login":
      if not login():
        continue
    elif Input.lower() == 'q':
      SaveData()
      break
    elif Input.lower() == 'd':
      del_acc()
      continue
    elif Input == '@MyLo':
      print(main)
      continue
    else:
      print("\nWRITE SOMETHING SENSIBLE OR ELSE I WILL EAT YOUR CAT'S TAIL")
      continue
    if UserNotes:
      #If there are any notes, print them
        print('\nYour saved notes are:\n')
        for note in UserNotes:
            print(note)
        x= input('Do you want to add or remove notes?  ')
        if x.lower() == 'add':
          add_notes(UserNotes)
        elif x.lower() == 'remove':
          Usernotes=del_notes(UserNotes)
    else:
        print('\nYou have no notes')
        x = input('Do you want to add more notes? ')
        if x.lower() == 'yes':
          Usernotes =add_notes(UserNotes)
    SaveData()
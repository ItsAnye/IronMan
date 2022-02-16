#Files
import classes
import responses
import commands

#Libraries
import random
import pickle
from os import path
import time
from bs4 import BeautifulSoup
import requests
import cv2
import string

accPath = '../../'
accState = False

user_command = ''

specialchars = '!@#$%^&*(){}|.:;?\',"'
specialchars_int = '!@#$%^&*(){}|:;?\',"'

user_info = None
username = None

mode = None


def main():
    global user_command

    while user_command.lower() not in commands.keywords['end']:
        known_command = False

        user_command = command()

        # Signup
        for i in commands.keywords['signup']:
            if i in user_command:
                signup()
                known_command = True
                break
        if username:
            if 'signup' in user_info['dictionary']:
                for i in user_info['dictionary']['signup']:
                    if i in user_command:
                        signup()
                        known_command = True
                        break

        # Login
        for i in commands.keywords['login']:
            if i in user_command:
                login()
                known_command = True
                break
        if username:
            if 'login' in user_info['dictionary']:
                for i in user_info['dictionary']['login']:
                    if i in user_command:
                        login()
                        known_command = True
                        break

        # Hello
        for i in commands.keywords['hello']:
            if i in user_command:
                hello()
                known_command = True
                break
        if username:
            if 'hello' in user_info['dictionary']:
                for i in user_info['dictionary']['hello']:
                    if i in user_command:
                        hello()
                        known_command = True
                        break

        # Logout
        for i in commands.keywords['logout']:
            if i in user_command:
                logout()
                known_command = True
        if username:
            if 'logout' in user_info['dictionary']:
                for i in user_info['dictionary']['logout']:
                    if i in user_command:
                        logout()
                        known_command = True
                        break

        # Help
        for i in commands.keywords['help']:
            if i in user_command:
                helpcenter()
                known_command = True
                break
        if username:
            if 'help' in user_info['dictionary']:
                for i in user_info['dictionary']['help']:
                    if i in user_command:
                        helpcenter()
                        known_command = True
                        break

        # Remove
        for i in commands.keywords['remove']:
            if i in user_command:
                remove()
                known_command = True
                break
        if username:
            if 'remove' in user_info['dictionary']:
                for i in user_info['dictionary']['remove']:
                    if i in user_command:
                        remove()
                        known_command = True
                        break

        # Stock
        for i in commands.keywords['stock']:
            if i in user_command:
                stock()
                known_command = True
                break
        if username:
            if 'stock' in user_info['dictionary']:
                for i in user_info['dictionary']['stock']:
                    if i in user_command:
                        stock()
                        known_command = True
                        break

        # Makes sure that add doesn't trigger unknown command
        for i in commands.keywords['add']:
            if i in user_command:
                known_command = True
                break
        if username:
            if 'add' in user_info['dictionary']:
                for i in user_info['dictionary']['add']:
                    if i in user_command:
                        known_command = True
                        break

        # Unknown Command Message
        if not known_command and not mode and user_command.lower() not in commands.keywords['end']:
            print(
                f'{classes.colors.GREEN}I don\'t know that one yet! Type {classes.colors.RED}help{classes.colors.GREEN} for some commands.')

            if username:
                print(
                    f'{classes.colors.YELLOW}Type {classes.colors.RED}add{classes.colors.YELLOW} to add a word or phrase to your personal dictionary.')
            else:
                print(
                    f'{classes.colors.GREEN}You can also {classes.colors.RED}login{classes.colors.GREEN} to manage a personal dictionary.')

        # Add: after unknown command because of multiple uses
        for i in commands.keywords['add']:
            if i in user_command:
                if mode == 'Stock':
                    stock('add')
                else:
                    add()
                break
        if username:
            if 'add' in user_info['dictionary']:
                for i in user_info['dictionary']['add']:
                    if i in user_command:
                        if mode == 'Stock':
                            stock('add')
                        else:
                            add()
                        break


def ok():
    print(f'{classes.colors.BLUE}' + responses.ok[random.randint(0, len(responses.ok) - 1)])


def command(integer=None):
    # Input
    usercommand = input(f'{classes.colors.BLUE}{classes.colors.BOLD}> {classes.colors.GREEN}{classes.colors.BOLD}')

    if not integer:
        usercommand = usercommand.lower().center(len(usercommand) + 2)

        for char in specialchars:
            if char in usercommand:
                usercommand = usercommand.replace(char, '')
    else:
        for char in specialchars_int:
            if char in usercommand:
                usercommand = usercommand.replace(char, '')

        usercommand = int(usercommand)

    return usercommand


def signup():
    global user_info
    ok()
    SU_username = 'Anye'  # Just a placeholder - fails because it's less than 6 chars

    while path.exists(f'{accPath}Accounts/{SU_username}') or len(
            SU_username) < 6 or ' ' not in SU_username or '|' not in SU_username or '(' not in SU_username or ')' not in SU_username:  # Username Criteria
        SU_username = input(f'{classes.colors.RED}Username: ')

        # Possible problems with username
        if path.exists(f'{accPath}Accounts/{SU_username}') and SU_username != 'Anye':
            print(f'{classes.colors.YELLOW}This account name is already taken.')
        if SU_username == 'Anye':
            print('Anye is one of the lead developers.')
            continue
        if len(SU_username) < 6:
            print(f'{classes.colors.YELLOW}Your username needs to be at least 6 characters.')
        if ' ' in SU_username:
            print(f'{classes.colors.YELLOW}Username\'s cannot have spaces.')
        if '|' in SU_username:
            print(f'{classes.colors.YELLOW}Username\'s cannot have pipes.')
        if '(' in SU_username or ')' in SU_username:
            print(f'{classes.colors.YELLOW}Username\'s cannot have parenthesis.')

        # Repeat if there are problems with username
        if path.exists(f'{accPath}Accounts/{SU_username}') == False and len(
                SU_username) > 6 and ' ' not in SU_username and '|' not in SU_username and '(' not in SU_username and ')' not in SU_username:
            break

    # Non-identical passwords
    SU_password = 'Placeholder1'
    SU_Cpassword = 'Placeholder2'

    # Passwords don't match
    while SU_password != SU_Cpassword:
        SU_password = input(f'{classes.colors.RED}Password: ')
        SU_Cpassword = input(f'{classes.colors.RED}Confirm Password: ')
        if SU_password != SU_Cpassword:
            print(f'{classes.colors.YELLOW}Passwords do not match. Try again: ')

    print(f'{classes.colors.YELLOW}We won\'t share your information with anyone.')

    SU_email = 'Email: '

    # Check if email is valid
    while '@' not in SU_email:
        SU_email = input(f'{classes.colors.RED}Email: ')
        if '@' not in SU_email:
            print(f'{classes.colors.YELLOW}Please enter a valid email address.')

    #Adding account info
    user_data = {
        'username': SU_username,
        'password': SU_password,
        'email': SU_email,
        'state': False,
        'dictionary': {},
        'finance': {},
        'pictures': []
    }

    user_info = picture(user_data)

    pickle.dump(user_data, open(f'{accPath}Accounts/{SU_username}', "wb"))

    # Thanks
    print(f'{classes.colors.BLUE}Thank you for signing up, {SU_username}!')
    print(f'{classes.colors.GREEN}Please log in now to continue.')


def login():
    global accState
    global user_info
    global username

    ok()
    if accState:
        print(f'{classes.colors.YELLOW}You are already logged in!')
    else:
        LI_username = ' Space '  # Just a placeholder - fails because has whitespace

        # If account doesn't exist (for sake of loop)
        while not path.exists(f'{accPath}Accounts/{LI_username}'):
            LI_username = input(f'{classes.colors.RED}Username: ')

            # If username inputed exists
            if path.exists(f'{accPath}Accounts/{LI_username}') and LI_username != '': #If it's blank, then that directory technically exists - the Accounts folder itself

                # Password
                LI_password = input(f'{classes.colors.RED}Password: ')

                # Check if password is correct
                user_info = pickle.load(open(f'{accPath}Accounts/{LI_username}', "rb"))
                print(LI_password)
                print(user_info)
                if LI_password == user_info['password']:
                    print(f'{classes.colors.GREEN}Welcome, {LI_username}!')
                    username = LI_username

                    # Custom hello response
                    responses.hello.append(f'Hey, {username}!')

                    if not user_info['state']:
                        user_info['state'] = True
                        pickle.dump(user_info, open(f'{accPath}Accounts/{LI_username}', "wb"))
                    accState = True
                else:
                    print(f'{classes.colors.YELLOW}Incorrect password.')
            else:
                print(f'{classes.colors.YELLOW}This account does not exist.')


def hello():
    print(f'{classes.colors.BLUE}' + responses.hello[random.randint(0, len(responses.hello) - 1)])


def logout(skip=False):
    global accState
    global user_info
    global username

    if(skip):
        user_info['state'] = False
        pickle.dump(user_info, open(f'{accPath}Accounts/{username}', "wb"))
        username = None
        responses.hello.remove(f'Hey, {username}!')
    else:
        if accState == True:
            print(f'{classes.colors.YELLOW}Are you sure you want to logout?')
            accStChangeCF = input(f'{classes.colors.BLUE}{classes.colors.BOLD}> ')

            #Formatting
            accStChangeCF = accStChangeCF.lower().center(len(accStChangeCF) + 2)
            for char in specialchars:
                if char in accStChangeCF:
                    accStChangeCF = accStChangeCF.replace(char, '')


            for i in commands.keywords['yes']:
                if i in accStChangeCF:
                    print('Sure. Logging you out...')
                    accState = False

                    #Custom hello response
                    responses.hello.remove(f'Hey, {username}!')

                    username = None

                    # Pickle
                    user_info['state'] = False
                    pickle.dump(user_info, open(f'{accPath}Accounts/{username}', "wb"))

                    time.sleep(1)
                    print(f'{classes.colors.RED}Successfully logged out.')
                    break

            if i == commands.keywords['yes'][len(commands.keywords['yes']) - 1] and commands.keywords['yes'][len(commands.keywords['yes']) - 1] not in accStChangeCF:
                print(f'{classes.colors.BLUE}No problem.')
        else:
            print(f'{classes.colors.YELLOW}You are already logged out!')


def helpcenter():
    print(f'{classes.colors.CYAN}Welcome to the Help Center. Some commands you can try are shown here: ')
    time.sleep(1)
    print() #Want the new line to come first
    time.sleep(0.5)
    print(f'{classes.colors.GREEN}Sign up{classes.colors.CYAN} - {classes.colors.YELLOW}Creates a new account')
    time.sleep(0.5)
    print(f'{classes.colors.GREEN}Log in{classes.colors.CYAN} - {classes.colors.YELLOW}Logs you into an existing account')
    time.sleep(0.5)
    print(f'{classes.colors.GREEN}Add{classes.colors.CYAN} - {classes.colors.YELLOW}Adds a word/phrase to your personal dictionary. {classes.colors.RED}YOU MUST BE LOGGED IN!')
    time.sleep(0.5)
    print(f'{classes.colors.GREEN}Log out{classes.colors.CYAN} - {classes.colors.YELLOW}Logs you out of your account.')
    time.sleep(0.5)
    print(f'{classes.colors.GREEN}Stocks{classes.colors.CYAN} - {classes.colors.YELLOW}Keeps you up to date on the stock market.')


#Adding to dictionary
def add():
    global user_info
    global username

    if username:
        user_info = pickle.load(open(f'{accPath}Accounts/{username}', "rb"))

        ok()
        print(f'{classes.colors.CYAN}Please enter the word or phrase you would like to add to your personal dictionary.')
        custom_phrase = command()

        #If user has phrase added
        phrase_exists = False
        for i in user_info['dictionary']:
            i = user_info['dictionary'][i]
            for word in i:
                if word == custom_phrase:
                    phrase_exists = True

        if not phrase_exists:
            print(f'{classes.colors.CYAN}Now, please enter the meaning of this word, in simple terms. For example, your phrase could be {classes.colors.RED}Hey there!{classes.colors.CYAN}, while your simple definition would mean {classes.colors.RED}Hello{classes.colors.CYAN}.')
            phrase_meaning = command()

            known_meaning = False
            for key in commands.keywords:
                for word in commands.keywords[key]:
                    if phrase_meaning == word:
                        #Meaning found
                        known_meaning = True

                        word = word.replace(' ', '')

                        print(f'{classes.colors.YELLOW}Adding...')

                        if word in user_info['dictionary']:
                            user_info['dictionary'][word].append(custom_phrase)
                        else:
                            user_info['dictionary'][word] = [custom_phrase]

                        pickle.dump(user_info, open(f'{accPath}Accounts/{username}', "wb"))

                        time.sleep(1)
                        print(f'{classes.colors.CYAN}Phrase successfully added.')

            if not known_meaning:
                print(f'{classes.colors.RED}The meaning you have entered is unknown.')
        else:
            print(f'{classes.colors.RED}This phrase is already in your dictionary.')
    else:
        print(f'{classes.colors.RED}You must be logged in to access this feature.')


def remove():
    if username:

        ok()
        print(f'{classes.colors.CYAN}Please enter the word or phrase you would like to remove to your personal dictionary.')
        phrase_to_remove = command()

        #If phrase exists
        phrase_exists = False
        for key in user_info['dictionary']:
            i = user_info['dictionary'][key]
            for word in i:
                if word == phrase_to_remove:
                    phrase_exists = True
                    #Removing
                    index = i.index(phrase_to_remove)
                    i.remove(i[index])

                    pickle.dump(user_info, open(f'{accPath}Accounts/{username}', "wb"))

        if phrase_exists:
            print(f'{classes.colors.YELLOW}Removing...')
            time.sleep(1)
            print(f'{classes.colors.RED}Phrase successfully removed.')
        else:
            print(f'{classes.colors.YELLOW}This phrase isn\'t in your personal dictionary.')

    else:
        print(f'{classes.colors.RED}You must be logged in to access this feature.')


def stock(setting=None):
    global mode
    global username
    global user_info

    if not setting:
        mode = 'Stock'

        session = requests.Session()
        stock = input(f'{classes.colors.CYAN}Please enter a stock: ')
        link = session.get(f'https://cnbc.com/quotes/{stock}')

        stock_shares = input('Number of shares: ')

        soup = BeautifulSoup(link.content, 'html.parser')
        tag = soup.find("span", {"class": "QuoteStrip-lastPrice"})

        tag = tag.text
        tag = tag.replace(',', '')
        money = float(tag) * float(stock_shares)
        price = round(money, 2)

        print('$' + str(price))
        print(f'{classes.colors.YELLOW}You are in stock mode. Saying "add" will add a stock to your account. Type exit to leave stock mode.')

    elif setting == 'add':
        if username:
            user_info = pickle.load(open(f'{accPath}Accounts/{username}', "rb"))

            ok()
            print(f'{classes.colors.CYAN}What stock would you like to watch?')
            new_watched_stock = command()

            # If user has phrase added
            stock_exists = False
            for i in user_info['finance']:
                if i == new_watched_stock:
                    stock_exists = True

            if not stock_exists:
                print(f'{classes.colors.YELLOW}If you own this stock, enter the price your bought it at. Otherwise, type {classes.colors.RED}none')
                stock_bought_value = command(True)

                print(stock_bought_value)

                if stock_bought_value == 'none':
                    stock_bought_value = None

                if type(stock_bought_value) == int or type(stock_bought_value) == float or not stock_bought_value:
                    print(f'{classes.colors.YELLOW}Adding...')

                    user_info['finance'][new_watched_stock] = stock_bought_value

                    pickle.dump(user_info, open(f'{accPath}Accounts/{username}', "wb"))

                    time.sleep(1)
                    print(f'{classes.colors.CYAN}Stock successfully added.')

                else:
                    print(f'{classes.colors.RED}This is not a number or none. Please try again.')
            else:
                print(f'{classes.colors.RED}You are already watching this stock.')
        else:
            print(f'{classes.colors.RED}You must be logged in to access this feature.')


def picture(user_info):
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Grabbing face...")

    counter = 0
    while True:
        ret, frame = cam.read()

        if not ret:
            print("Failed to get frame")
            break

        cv2.imshow("Grabbing face...", frame)

        letters = string.ascii_lowercase
        img_name = f"{user_info['username']}_{''.join(random.choice(letters) for i in range(3))}.png"

        cv2.imwrite(f"{accPath}Accounts/Pictures/{img_name}", frame)

        user_info['pictures'].append(f'{accPath}Accounts/Pictures/{img_name}')
        pickle.dump(user_info, open(f'{accPath}Accounts/{username}', "wb"))

        counter += 1
        time.sleep(2)

        if counter == 2:
            break

    cam.release()
    cv2.destroyAllWindows()
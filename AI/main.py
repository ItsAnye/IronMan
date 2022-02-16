#TODO: Save images to user_data!
#TODO: Login by face
#TODO: Stocks
    #TODO: Unwatch stock
    #TODO: Color code stock price if watched and bought price is specified: red or green
#TODO: Custom unknown command responses
#TODO: Search the web!
#TODO: Exit out of commands like login and signup?
#TODO: Show incorrect username or password, rather than incorrect username / incorrect password
#TODO: Prevent signing up when logged in
#TODO: Login should be case sensitive!

#Files
import functions
import classes

# functions.picture(None)

#User Input
print(f'Would you like to {classes.colors.GREEN}{classes.colors.BOLD}Log In{classes.colors.BLACK} or{classes.colors.YELLOW}{classes.colors.BOLD} Sign Up{classes.colors.BLACK}?')

functions.main()

if functions.mode == 'Stock':
    functions.mode = None
    print(f'{classes.colors.YELLOW}You have now exited stock mode.')

    functions.user_command = ''
    functions.main()
else:
    print(f'{classes.colors.RED}Goodbye!')

if functions.username:
    functions.logout(True)
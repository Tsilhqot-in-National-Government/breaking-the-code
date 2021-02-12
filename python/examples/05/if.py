def useNightMode(timeOfDay):
    '''
    Determines whether or not to use night mode.
    '''
    if timeOfDay == 'day':
        return False
    elif timeOfDay == 'night':
        return True
    else:
        errorMessage = "Invalid input: " + timeOfDay
        raise Exception(errorMessage)

def logger(timeOfDay):
    print('It is ' + timeOfDay)
    nightModeEnabled = useNightMode(timeOfDay)
    if nightModeEnabled:
        print("Night mode enabled.")
    else:
        print("Night mode disabled.")

logger('day')
logger('night')
logger('party-time')




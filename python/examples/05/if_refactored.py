class TimeFormatError(Exception):
    '''
    Raised when Time of Day is passed in the wrong format.
    '''
    pass

def useNightMode(timeOfDay):
    '''
    Determines whether or not to use night mode.
    '''
    if timeOfDay == 'day':
        return False
    if timeOfDay == 'night':
        return True
    errorMessage = "Invalid state: " + timeOfDay
    raise TimeFormatError(errorMessage)

def logger(timeOfDay):
    print('It is ' + timeOfDay)
    try:
        message = "Night mode enabled." if useNightMode(timeOfDay) else "Night mode disabled."
    except TimeFormatError as err:
        message = err
    print(message)

logger('day')
logger('night')
logger('party-time')




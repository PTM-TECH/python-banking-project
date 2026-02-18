# → torauthentication and logging decorators
#events that happen in systems
#used to debug or track system changes automatically we can use logs

#Without decorators, you have to repeat same code in multiple functions

import time
from datetime import datetime

def log(func):
    def wrapper(*args, **kwargs):
        start_time=time.time()
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result=func(*args, **kwargs)
        end_time=time.time()
        time_taken=end_time-start_time
        log_message = f"""
    ---------------LOG---------------
    Timestamp: {timestamp}
    Function: {func.__name__}
    Time Taken: {time_taken} seconds
    Inputs: args={args}, kwargs={kwargs}
    Result: {result}
    ---------------------------------
    """
        with open("log.txt", "a") as file:
            file.write(log_message)
        return result
    return wrapper
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./assignment3/decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        pos_params = list(args) if args else "none"
        kw_params = kwargs if kwargs else "none"
        result = func(*args, **kwargs)
        
        log_msg = (f"function: {func.__name__}\n"
                   f"positional parameters: {pos_params}\n"
                   f"keyword parameters: {kw_params}\n"
                   f"return: {result}\n")
        logger.info(log_msg)
        return result
    return wrapper

@logger_decorator
def task_1a():
    print("Hello, World!")

@logger_decorator
def task_1b(*args):
    return True

@logger_decorator
def task_1c(**kwargs):
    return "logger_decorator"

task_1a()
task_1b(10, 20)
task_1c(user="Ricardo", status="Student")

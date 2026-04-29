def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            return type_of_output(value)
        return wrapper
    return decorator

@type_converter(str)
def return_int():
    return 5

@type_converter(int)
def return_string_num():
    return "123"

string_five = return_int()
int_one_two_three = return_string_num()

print(f"Value: {string_five}, Type: {type(string_five).__name__}")
print(f"Value: {int_one_two_three}, Type: {type(int_one_two_three).__name__}")

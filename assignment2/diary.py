import traceback
try:
    with open('diary.txt' , 'a') as file:
        prompt = "What happened today? "

        while True: 
            user_input = input(prompt)

            file.write(user_input + "\n")

            if user_input == "done for now":
                break
            prompt = "What else? "

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"An exception occurred: {type(e).__name__}")

    message = str(e)
    if message:
       print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")

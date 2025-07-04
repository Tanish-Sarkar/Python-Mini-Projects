HISTORY_FILE = "history.txt" 

def show_history():
    file = open(HISTORY_FILE, "r")
    lines = file.readlines()
    if len(lines) == 0:
        print("No Histry found!")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(HISTORY_FILE, "w")
    file.close()
    print("History cleared!")

def save_to_history(equation, result):
    file = open(HISTORY_FILE, "a")
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid Input. Use format: number operator number (e.g 8 + 2 = 10): ")
        return
    
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
        result = num1 / num2
    else:
        print("Invalid operator!")
        return
    
    if int(result) == result:
        result = int(result)
    print("Result: ", result)
    save_to_history(user_input, result)


def main():
    print("---SIMPLE CALCULATOR---")
    while True:
        user_input = input("Enter Caluculation (+ - * /) or commands (history, clear, exit): ")
        if user_input.lower().strip() == "exit":
            print("Goodbye!")
            break
        elif user_input.lower().strip() == "history":
            show_history()
        elif user_input.lower().strip() == "clear":
            clear_history()
        else:
            calculate(user_input)

main()     
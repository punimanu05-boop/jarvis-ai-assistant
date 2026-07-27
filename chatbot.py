from datetime import datetime
import random
import time

print("=" * 60)
print("J.A.R.V.I.S. Artificial Intelligence System")
print("=" * 60)

time.sleep(1)
print("Initializing System...")
time.sleep(1)
print("Loading AI Modules...")
time.sleep(1)
print("Connecting...")
time.sleep(1)
print("System Online")
print()

name = input("Enter your name: ").strip()

while True:
    gender = input("Enter your gender (Male/Female): ").lower().strip()

    if gender == "male":
        title = "Sir"
        break
    elif gender == "female":
        title = "Ma'am"
        break
    else:
        print("Please enter Male or Female.")

print()
print("Welcome", name + ".")
print("I am J.A.R.V.I.S.")
print("Type 'help' to view available commands.")
print("Type 'exit' to quit.")

while True:

    user = input("\nYou: ").lower().strip()

    if user in ["hello", "hi", "hey"]:
        print("JARVIS: Hello", title + ".", "How may I assist you?")

    elif user == "good morning":
        print("JARVIS: Good Morning", title + ".")

    elif user == "good afternoon":
        print("JARVIS: Good Afternoon", title + ".")

    elif user == "good evening":
        print("JARVIS: Good Evening", title + ".")

    elif user == "good night":
        print("JARVIS: Good Night", title + ".")

    elif user == "what is your name":
        print("JARVIS: My name is J.A.R.V.I.S.")

    elif user == "who created you":
        print("JARVIS: I was created by", name + ".")

    elif user == "creator":
        print("JARVIS: My creator is", name + ".")

    elif user == "about":
        print("JARVIS: I am a Rule-Based AI Assistant developed using Python.")

    elif user == "version":
        print("JARVIS Version 1.0")

    elif user == "time":
        print("JARVIS:", datetime.now().strftime("%I:%M:%S %p"))

    elif user == "date":
        print("JARVIS:", datetime.now().strftime("%d-%m-%Y"))

    elif user == "day":
        print("JARVIS:", datetime.now().strftime("%A"))

    elif user == "month":
        print("JARVIS:", datetime.now().strftime("%B"))

    elif user == "year":
        print("JARVIS:", datetime.now().strftime("%Y"))

    elif user == "joke":
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "Why was the computer cold? It forgot to close Windows.",
            "Debugging is like being a detective in your own crime movie.",
            "Python developers don't bite. They just hiss."
        ]
        print("JARVIS:", random.choice(jokes))

    elif user == "fun fact":
        facts = [
            "Python was named after Monty Python.",
            "Honey never spoils.",
            "The first computer bug was an actual insect.",
            "The Eiffel Tower grows taller during summer."
        ]
        print("JARVIS:", random.choice(facts))

    elif user == "quote":
        quotes = [
            "Success is the sum of small efforts repeated every day.",
            "Dream big. Start small. Act now.",
            "Knowledge grows when it is shared.",
            "Consistency beats motivation."
        ]
        print("JARVIS:", random.choice(quotes))

    elif user == "motivate me":
        print("JARVIS: Keep learning. Every expert was once a beginner.")

    elif user == "capital of india":
        print("JARVIS: New Delhi.")

    elif user == "largest planet":
        print("JARVIS: Jupiter.")

    elif user == "largest ocean":
        print("JARVIS: Pacific Ocean.")

    elif user == "fastest animal":
        print("JARVIS: Peregrine Falcon.")

    elif user == "national animal of india":
        print("JARVIS: Bengal Tiger.")

    elif user == "python":
        print("JARVIS: Python is simple, powerful and widely used in Artificial Intelligence.")

    elif user == "ai":
        print("JARVIS: Artificial Intelligence enables machines to perform tasks that normally require human intelligence.")

    elif user == "project":
        print("JARVIS: Your current project is a Rule-Based AI Chatbot.")

    elif user == "roll dice":
        print("JARVIS:", random.randint(1, 6))

    elif user == "flip coin":
        print("JARVIS:", random.choice(["Heads", "Tails"]))

    elif user == "lucky number":
        print("JARVIS:", random.randint(1, 100))

    elif user == "calculate":
        try:
            num1 = float(input("First Number: "))
            op = input("Operator (+ - * /): ")
            num2 = float(input("Second Number: "))

            if op == "+":
                print("Answer =", num1 + num2)
            elif op == "-":
                print("Answer =", num1 - num2)
            elif op == "*":
                print("Answer =", num1 * num2)
            elif op == "/":
                if num2 == 0:
                    print("Cannot divide by zero.")
                else:
                    print("Answer =", num1 / num2)
            else:
                print("Invalid Operator.")

        except:
            print("Invalid Input.")

    elif user == "activate protocol":
        print("Access Granted.")
        print("Loading AI Core...")
        print("All Systems Ready.")
        print("Welcome Back,", title + ".")

    elif user == "help":
        print("""
Available Commands

hello
hi
hey
good morning
good afternoon
good evening
good night

what is your name
who created you
creator
about
version

time
date
day
month
year

python
ai
project

joke
fun fact
quote
motivate me

capital of india
largest planet
largest ocean
fastest animal
national animal of india

calculate
roll dice
flip coin
lucky number

activate protocol

help
thank you
bye
exit
""")

    elif user in ["thank you", "thanks"]:
        print("JARVIS: Always at your service,", title + ".")

    elif user == "who am i":
        print("JARVIS: You are", name + ",", title + ".")

    elif user in ["bye", "exit"]:
        print("JARVIS: Goodbye", name + ".")
        break

    else:
        print("JARVIS: Command not recognized. Type 'help' to see available commands.")
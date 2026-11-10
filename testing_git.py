user_input = input("Write your name: ")

while True:
    answer = int(input("Write a random number 1-50: "))
    if answer < 1 or answer > 50:
        print(f"""{user_input}, invalid answer. try again""")
    else:
        print(f"""{user_input}, ok""")
        break
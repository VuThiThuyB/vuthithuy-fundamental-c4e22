quiz = {
    "stimulus":"Answer the following algebra questions:",
    "stem":"If x = 8, then what is the value of 4(x+3)?",
    "choices":["1.35","2.36","3.40","4.44"],
    "right choice": 4,
}
while True:
    print(quiz["stimulus"])
    print(quiz["stem"])
    print(*quiz["choices"],sep='\n')
    answer = input("Your choice: ")
    if answer.isdigit():
        answer = int(answer)
        if answer == quiz["right choice"]:
            print("Bingo")
            break
        else :
            print(":(((")


from random import *
answers = ["Да", "Нет"]

def solution():
    flag = True
    while True:
        request = input('Хотишь ешё? "д" - "да", "н" - "нет"')
        if request == "н":
            break
        elif request == "д":
            answer_to_question()
        else:
            print("Не понял, начни заново")

def answer_to_question():
    while True:
        question = input("Задай мне вопрос, чтобы на него можно было ответить либо да, либо нет:")
        answer = choice(answers)
        print(f"Мой ответ {answer}")
        solution()
        break
answer_to_question()




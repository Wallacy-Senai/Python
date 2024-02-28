# jogo.py

import random
#Herança
from perguntas import questions

def fifty_fifty(question, answer):
    all_answers = list(questions.values())
    all_answers.remove(answer)
    wrong_answer = random.choice(all_answers)
    return f"Você tem duas opções: '{answer}' ou '{wrong_answer}'."

def select_question():
    question = random.choice(list(questions.keys()))
    answer = questions[question]
    return question, answer

def millionaire_game():
    print("Bem-vindo ao Quem Quer Ser um Milionário!")
    print("Você está pronto para começar? Vamos lá!\n")

    total_money = 0

    for _ in range(len(questions)):
        question, answer = select_question()
        print("Pergunta:", question)
        print("Pontuação atual:", total_money)

        # Opções de ajuda
        if total_money == 0:
            use_fifty_fifty = input("Você quer usar a ajuda 50-50? (sim/não): ").strip().lower()
            if use_fifty_fifty == "sim":
                print(fifty_fifty(question, answer))

        user_answer = input("Sua resposta (ou 'sair' para sair com o dinheiro acumulado): ").strip()

        if user_answer.lower() == "sair":
            print("Você decidiu sair com R$", total_money)
            break

        if user_answer.lower() == answer.lower():
            print("Resposta correta!")
            total_money += 100000
            print("Você ganhou R$100.000! Seu total até agora é R$", total_money)
        else:
            print("Resposta incorreta! Você perdeu o jogo.")
            print("Você ganhou R$", total_money)
            break

    print("\nFim do jogo! Você ganhou R$", total_money)

if __name__ == "__main__":
    millionaire_game()

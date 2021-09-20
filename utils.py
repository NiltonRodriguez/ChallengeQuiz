from random import choice
from time import sleep
import csv


def display_top_scores():
    print("\n", "\tTOP 5 SCORES")
    with open("scores.csv", "r") as scores_file:
        csv_reader = csv.reader(scores_file, delimiter=',')
        csv_list = list(csv_reader)

    print(csv_list[0][0].capitalize(), "|", csv_list[0][1].capitalize(),
          "|", csv_list[0][2].capitalize())
    csv_list = csv_list[1:]
    csv_list.sort(key=lambda x: x[-1], reverse=True)
    length = 0
    if len(csv_list) > 5:
        length = 5
    else:
        length = len(csv_list)
    for i in range(length):
        print(csv_list[i][0].capitalize(), "|", csv_list[i][1].capitalize(),
              "|", csv_list[i][2].capitalize())


def randomize(lst):
    """
    Randomize the order of the elements in the parameter.

    Parameters:
    -----------
    lst(list): List with the elements to order.

    Return:
    -------
    randomized(list): List with the elements in a randomized order.
    """
    length = len(lst)
    randomized = []
    for i in range(length):
        if length > 1:
            chosen = choice(lst)
            randomized.append(chosen)
            lst.remove(chosen)
        else:
            randomized.append(lst[0])
            lst.clear()
    return randomized


def save_score(name, rounds, score):
    """
    Update de scores database.
    """
    to_append = [name, rounds, score]
    with open("scores.csv", "a", newline="") as scores_file:
        csv_writer = csv.writer(scores_file)
        csv_writer.writerow(to_append)


def verify_option(valid_options, user_option):
    verified = False
    if user_option in valid_options:
        verified = True
    return verified


def welcome():
    """
    Display the instructions of the game and prompt the user name.

    Return:
    name(str): User name.
    """
    print("\tBIENVENIDO A CHALLENGE QUIZ", "\n", "Challenge Quiz es un juego "
          "de trivia. Para ganar debes contestar 5 preguntas correctamente.",
          "\n", "Cada pregunta está clasificada en una categoría diferente"
          "como Ciencia, Deportes, Entretenimiento, Geografía o Historia.",
          "Debes elegir la respuesta correcta entre las cuatro "
          "opciones que se presentan para cada pregunta.", "\n"
          "El juego inicia cuando introduzcas tu nombre", "\n", sep="\n")
    name = input("¿Cómo te llamas? ")
    print(name, "¡Comenzamos!", "\n")
    sleep(1)
    return name

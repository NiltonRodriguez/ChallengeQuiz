from player import Player
from question_bank import Bank
from utils import welcome, save_score, display_top_scores

question_db = Bank()
categories_list = question_db.randomize_categories()

actual_player = Player(welcome(), 0)
actual_round = 1
succeded = []

for category in categories_list:
    print(f"Ronda {actual_round}: {category}")
    current_question = question_db.select_question(category, actual_round)
    current_question.display_question()
    options = current_question.randomize_answers()
    current_question.display_options(options)
    user_option = question_db.prompt_option()
    if current_question.verify_answer(options[user_option]):
        print("¡Correcto! Avanzas a la siguente ronda.")
        succeded.append(category)
        round_points = actual_round * 10
        actual_player.update_score(round_points)
        print(f"Ganaste {round_points} puntos.", "\n")
        actual_round += 1
        if actual_round < 5:
            next_question = question_db.prompt_continue()
            if next_question == "N":
                break
    else:
        print("¡Fallaste! Esa no era la respuesta correcta.", "\n")
        actual_player.clear_score()
        break

question_db.display_result(actual_player.name, actual_player.score, succeded)
save_score(actual_player.name, actual_round - 1, actual_player.score)
display_top_scores()

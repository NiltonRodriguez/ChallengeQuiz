from question import Question
from utils import randomize, verify_option


class Bank:
    # Class Constructor.
    def __init__(self):
        self.categories = ["Entretenimiento", "Geografía", "Historia",
                           "Ciencia", "Deportes"]
        self.rank1 = {
            0: Question(self.categories[0],
                        "¿Cuántas películas componen la saga Harry Potter?",
                        "8", "7", "9", "5"),
            1: Question(self.categories[1],
                        "¿Cuántos océanos hay en la tierra?", "5", "6", "7",
                        "4"),
            2: Question(self.categories[2],
                        "¿En qué año se firmó la declaración de la "
                        "independencia de Colombia?", "1810", "1819",
                        "1814", "1805"),
            3: Question(self.categories[3], "¿Qué es el COVID?", "Un Virus",
                        "Una Bacteria", "Un Protozoo", "Una Pandemia"),
            4: Question(self.categories[4],
                        "¿Con qué número jugaba Carlos 'El Pibe' Valderrama "
                        "en la selección Colombia?", "10", "1", "9", "11")
        }
        self.rank2 = {
            0: Question(self.categories[0],
                        "¿Qué película inició el Universo Cinematográfico "
                        "de Marvel?", "Iron Man", "The Hulk", "The Avengers",
                        "Spiderman"),
            1: Question(self.categories[1],
                        "¿Cuál es el río más largo del mundo?", "El Nilo",
                        "El Amazonas", "El Danubio", "El Rin"),
            2: Question(self.categories[2],
                        "¿Cuál de los siguentes paises no integró a "
                        "los Aliados durente la Segunda Guerra Mundial?",
                        "Japón", "Estados Unidos", "Francia", "Gran Bretaña"),
            3: Question(self.categories[3],
                        "¿Qué le da el color verde a las hojas de "
                        "las plantas?", "La Clorofila",
                        "Los Pistilos", "Los Estomas", "La Salvia"),
            4: Question(self.categories[4],
                        "¿Cuántos cuadros componen el tablero de ajedréz",
                        "64", "60", "56", "58")
        }
        self.rank3 = {
            0: Question(self.categories[0],
                        "¿Quién pintó 'La Persistencia de la Memoria'?",
                        "Salvador Dalí", "Pablo Picasso", "Vincent Van Gogh",
                        "Andy Warhol"),
            1: Question(self.categories[1],
                        "¿Qué paises disputan la soberanía sobre Gibraltar?",
                        "España y Gran Bretaña", "España y Marruecos",
                        "Portugal y Marruecos", "Italia y Túnez"),
            2: Question(self.categories[2],
                        "¿Qué desencadenó el inicio de la Primera "
                        "Guerra Mundial?", "La Muerte de Franz Ferdinand",
                        "La llegada al poder de Hitler",
                        "El bombardeo a Pearl Harbor",
                        "El desarrollo de la bomba atómica"),
            3: Question(self.categories[3],
                        "¿Cuál de estos no es un huesesillo del oido?",
                        "Semilunar", "Martillo", "Yunque", "Estribo"),
            4: Question(self.categories[4],
                        "¿Cuál es el jugador de tenis con más títulos "
                        "del torneo de Wimbledon?", "Roger Federer",
                        "Pete Sampras", "Novak Djokovic", "John McEnroe")
        }
        self.rank4 = {
            0: Question(self.categories[0],
                        "¿Qué inspiró los nombres de las Tortugas Ninja?",
                        "Pintores Renacentistas", "Jugadores de Fútbol",
                        "Presidentes de Estados Unidos", "Dioses griegos"),
            1: Question(self.categories[1],
                        "¿Qué ciudad se ubica en dos continentes?",
                        "Estambul", "Ciudad de Panamá", "Moscú", "Asjabad"),
            2: Question(self.categories[2],
                        "Según la mitología griega, ¿Qué moneda debías "
                        "pagarle al barquero Caronte para que te llevara a "
                        "través del rio Estigia?", "Un dragma",
                        "Un denario", "Un centavo", "Un dragtario"),
            3: Question(self.categories[3],
                        "¿A quén se atribuyen los principales aportes al "
                        "desarollo de la bomba atómica?",
                        "Robbert Oppenhaimer", "Albert Einstein",
                        "Erwin Schrödinger", "Nikola Tesla"),
            4: Question(self.categories[4],
                        "¿Cuál fue el primer campeón de la Copa Mundial "
                        "de Fútbol?", "Uruguay", "Argentina", "Brasil",
                        "Inglaterra"),
        }
        self.rank5 = {
            0: Question(self.categories[0],
                        "¿Cuál fue la primer película animada de Disney?",
                        "Blanca Nieves y los 7 enanitos", "Pinocho",
                        "Fantasía", "La Bella durmiente"),
            1: Question(self.categories[1],
                        "¿Cuál es la capital más al norte del mundo?",
                        "Raikiavik", "Nuuk", "Oslo", "Estocolmo"),
            2: Question(self.categories[2],
                        "¿Cuál es la ciudad más antigua de Colombia?",
                        "Santa Marta", "Cartagena", "Bogotá", "Tunja"),
            3: Question(self.categories[3],
                        "¿Cuál de las siguientes letras no identifica ningún "
                        "elemento en la tabla periódica?", "J", "K", "Z", "W"),
            4: Question(self.categories[4],
                        "¿Quién fue el único campeon de boxeo de pesos pesados"
                        " que nunca fue derrotado?", "Rocky Marciano",
                        "Mike Tyson", "Muhammad Ali", "Tyson Fury")
        }

    def randomize_categories(self):
        """
        Randomize the order of the categories.

        Return:
        -------
        random_categories(list): List with the randomized categories.
        """
        random_categories = randomize(self.categories)
        return random_categories

    def select_question(self, category, actual_round):
        """
        Selects the rank question according to the actual round and category.

        Parameters:
        -----------
        category(str): The actual category.
        actual_round(int): The actual round reached by the player.

        Returns:
        --------
        selected_category(Question): The selected Question.
        """
        def __check_category(rank, category):
            """
            Check which of the Questions of the rank correspond to the actual
            category.

            Parammeters:
            ------------
            rank(dict): Dictionary with Question.
            category(str): The category to check in the rank dictionary.

            Returns:
            --------
            Question object correspoinding to the specified category.
            """
            for key in rank:
                if rank[key].category == category:
                    return rank[key]

        if actual_round == 1:
            rank = self.rank1
            selected_category = __check_category(rank, category)
        elif actual_round == 2:
            rank = self.rank2
            selected_category = __check_category(rank, category)
        elif actual_round == 3:
            rank = self.rank3
            selected_category = __check_category(rank, category)
        elif actual_round == 4:
            rank = self.rank4
            selected_category = __check_category(rank, category)
        elif actual_round == 5:
            rank = self.rank5
            selected_category = __check_category(rank, category)
        return selected_category

    def prompt_option(self):
        """
        Prompt the user for an option and verify if its a valid option.

        Return:
        -------
        user_option(str): The prompted option
        """
        valid_options = ["A", "B", "C", "D"]
        user_option = input("¿Qué opción eliges? ").upper()
        while True:
            check = verify_option(valid_options, user_option)
            if not check:
                user_option = input("¡Elige una opción válida! ").upper()
            else:
                print("")
                return user_option

    def prompt_continue(self):
        """
        Prompt the user to continue the game.

        Return:
        -------
        next_question(str): The prompted option
        """
        valid_options = ["S", "N"]
        next_question = input(
            "¿Deseas continuar con la próxima pregunta?(S/N) ").upper()
        while True:
            check = verify_option(valid_options, next_question)
            if not check:
                next_question = input(
                    "Por favor indícanos si deseas continuar(S/N) ").upper()
            else:
                print("")
                return next_question

    def display_result(self, name, score, categories):
        length = len(categories)
        print(f"{name} lograste {score} puntos")
        if length > 0:
            print(f"Acertaste {length} categoría(s):")
            for category in categories:
                print(">", category)
        else:
            print("¡Sigue esforzandote para ganar!")
        if length == 5:
            print("\n" + "¡Felicitaciones, completaste el juego!")

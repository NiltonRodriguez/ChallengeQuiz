
from utils import randomize


class Question:
    # Class constructor.
    def __init__(self, category, question, answer, op1, op2, op3):
        self.category = category
        self.question = question
        self.answer = answer
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3

    # Encapsule the atrributes.
    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        self.__category = value

    @property
    def question(self):
        return self.__question

    @question.setter
    def question(self, value):
        self.__question = value

    @property
    def answer(self):
        return self.__answer

    @answer.setter
    def answer(self, value):
        self.__answer = value

    @property
    def op1(self):
        return self.__op1

    @op1.setter
    def op1(self, value):
        self.__op1 = value

    @property
    def op2(self):
        return self.__op2

    @op2.setter
    def op2(self, value):
        self.__op2 = value

    @property
    def op3(self):
        return self.__op3

    @op3.setter
    def op3(self, value):
        self.__op3 = value

    def toString(self):
        return (self.category, self.question, self.answer,
                self.op1, self.op2, self.op3)

    def display_question(self):
        """
        Display in the terminal the current question
        """
        print(self.question)
        print("")

    def randomize_answers(self):
        """
        Randomize the order of the answer and options of the current
        question.

        Return:
        -------
        random_options(dict): Dictionary with the randomized options.
        """
        options = [self.answer, self.op1, self.op2, self.op3]
        new_order = randomize(options)
        random_options = {
            "A": new_order[0],
            "B": new_order[1],
            "C": new_order[2],
            "D": new_order[3]
        }
        return random_options

    def display_options(self, dictionary):
        """
        Display in the terminal the current options
        """
        for key, value in dictionary.items():
            print(f"{key}: {value}")
        print("")

    def verify_answer(self, option):
        """
        Verify if the user option is the correct answer for the
        current question.

        Parameters:
        -----------
        option(str): The option chosen by the user.

        Return:
        -------
        (Boolean) Result of the compairson between the user option
        and the correct answer.
        """
        return self.answer == option

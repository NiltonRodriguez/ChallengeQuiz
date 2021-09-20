class Player:
    # Class constructor.
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # Encapsule the atrributes.
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    def update_score(self, points):
        """
        Update the player score.
        """
        self.score += points

    def clear_score(self):
        self.score = 0

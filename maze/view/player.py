class Player:

    def __init__(self, goal):
        self.goal = goal
        self._loc = (0, 0)

    @property
    def loc(self):
        return self._loc

    def move(self, direction):
        self._loc = (self._loc[0] + direction[0], self._loc[1] + direction[1])

    def reachedGoal(self):
        return self.goal == self._loc

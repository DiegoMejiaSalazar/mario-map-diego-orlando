from src.Spot import Spot


class Laberinth:
    def __init__(self, rows, columns):
        self.__laberinth = [[Spot() for i in range(columns)] for j in range(rows)]
        self.__obstacles = []
        self.__targets = []

    @property
    def laberinth(self):
        return self.__laberinth

    @laberinth.setter
    def laberinth(self, value):
        self.__laberinth = value

    @property
    def obstacles(self):
        return self.__obstacles

    @obstacles.setter
    def obstacles(self, value):
        self.__obstacles = value
        for obstacle in self.__obstacles:
            self.__laberinth[obstacle[0]][obstacle[1]].value = '#'

    @property
    def targets(self):
        return self.__targets

    @targets.setter
    def targets(self, value):
        self.__targets = value
        for target in self.__targets:
            self.laberinth[target[0]][target[1]].value = 'X'

    def is_valid_position(self, row, column):
        if row > (len(self.laberinth) - 1) or \
                row < 0 or \
                column > (len(self.laberinth[0]) - 1) or \
                column < 0:
            return False
        return not (row, column) in self.obstacles

    def get_neighbors(self, row, column):
        result = [
            (row - 1, column),
            (row + 1, column),
            (row, column + 1),
            (row, column - 1),
        ]
        return filter(lambda x: self.is_valid_position(x[0], x[1]), result)

    def set_up_value(self, row, column, value):
        if self.is_valid_position(row, column):
            self.laberinth[row][column].h = value
            self.laberinth[row][column].value = value

    def set_up_g(self, row, column, value):
        if self.is_valid_position(row, column):
            self.laberinth[row][column].g = value

    def set_up_f(self, row, column, value):
        if self.is_valid_position(row, column):
            self.laberinth[row][column].f = value

    def get_spot(self, row, column):
        if self.is_valid_position(row, column):
            return self.laberinth[row][column]

    def show(self):
        for row in self.laberinth:
            print(row)

    def is_goal(self, row, column):
        return (row, column) in self.targets

    def get_closes_goal_given_a_coordinate(self, row, column):
        result = None
        for target in self.targets:
            if result is None:
                result = target
            else:
                if abs(target[0] - row) + abs(target[1] - column) < abs(result[0] - row) + abs(result[1] - column):
                    result = target
        return result

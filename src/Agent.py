class Agent:
    def __init__(self):
        self.__x_position = 0
        self.__y_position = 0
        self.__visited = set()
        self.__laberinth = None

    @property
    def x_position(self):
        return self.__x_position

    @x_position.setter
    def x_position(self, value):
        self.__x_position = value

    @property
    def y_position(self):
        return self.__y_position

    @property
    def laberinth(self):
        return self.__laberinth

    @y_position.setter
    def y_position(self, value):
        self.__y_position = value

    def set_laberinth(self, value):
        self.__laberinth = value

    def manhattan_distance(self):
        rows = len(self.__laberinth.laberinth)
        for x in range(rows):
            columns = len(self.__laberinth.laberinth[x])
            for y in range(columns):
                target = self.laberinth.get_closes_goal_given_a_coordinate(x, y)
                self.__laberinth.set_up_value(x, y, abs(abs(target[0] - x) + abs(target[1] - y)))

    def resolve_path(self):
        pass

    def setup(self):
        self.laberinth.get_spot(
            self.__x_position,
            self.__y_position
        ).f = 0

        self.laberinth.get_spot(
            self.__x_position,
            self.__y_position
        ).g = 0

        self.laberinth.get_spot(
            self.__x_position,
            self.__y_position
        ).h = 0

        for i in self.laberinth.targets:
            self.laberinth.get_spot(
                i[0],
                i[1]
            ).f = 0

            self.laberinth.get_spot(
                i[0],
                i[1]
            ).g = 0

            self.laberinth.get_spot(
                i[0],
                i[1]
            ).h = 0

    def astar(self):
        open_list = []
        closed_list = []

        open_list.append((self.__x_position, self.__y_position))
        self.setup()
        while len(open_list) > 0:
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if self.laberinth.get_spot(
                        item[0],
                        item[1]
                        ).f < self.laberinth.get_spot(
                        current_node[0],
                        current_node[1]
                        ).f:
                    current_node = item
                    current_index = index

            open_list.pop(current_index)
            closed_list.append(current_node)

            if self.laberinth.is_goal(current_node[0], current_node[1]):
                path = []
                current = current_node
                while current is not None:
                    path.append(current)
                    current = self.laberinth.get_spot(
                        current[0],
                        current[1]
                    ).parent
                return path[::-1]
            children = []
            for new_position in self.laberinth.get_neighbors(current_node[0], current_node[1]):
                if new_position == self.laberinth.get_spot(current_node[0], current_node[1]).parent:
                    continue
                self.laberinth.get_spot(new_position[0], new_position[1]).parent = current_node

                children.append(new_position)

            for child in children:
                if child in closed_list:
                    continue

                self.laberinth.set_up_g(child[0],
                                          child[1],
                                          self.laberinth.get_spot(
                                              current_node[0],
                                              current_node[1]
                                          ).g + 1)
                self.laberinth.set_up_f(child[0],
                                          child[1],
                                          self.laberinth.get_spot(
                                              child[0],
                                              child[1]
                                          ).g + self.laberinth.get_spot(
                                              child[0],
                                              child[1]
                                          ).h
                                          )

                for open_node in open_list:
                    if child == open_node and self.laberinth.get_spot(
                                              child[0],
                                              child[1]
                                          ).g > self.laberinth.get_spot(
                                              open_node[0],
                                              open_node[1]
                                          ).g:
                        continue
                open_list.append(child)
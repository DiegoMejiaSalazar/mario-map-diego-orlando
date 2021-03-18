class Spot:
    def __init__(self):
        self.h = 0
        self.g = 0
        self.f = 0
        self.parent = None
        self.value = ' '

    def __repr__(self):
        return str(self.value)

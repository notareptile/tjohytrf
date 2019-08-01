class ship():
    size = 30
    speed = 5
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.yvelocity = 0
        self.xvelocity = 0
    def move(self):
        self.x += self.xvelocity
        self.y += self.yvelocity

    def changevelocity(self, direction):
        if direction == "left":
            self.xvelocity += self.speed
        if direction == "right":
            self.xvelocity -= self.speed
        if direction == "up":
            self.yvelocity += self.speed
        if direction == "down":
            self.yvelocity -= self.speed

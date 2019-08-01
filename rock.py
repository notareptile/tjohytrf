class Rock():
    def __init__(self, x, y, xspeed, yspeed, size):
        self.x = x
        self.y = y
        self.yspeed = yspeed
        self.xspeed = xspeed
        self.size = size

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed

    def bounce(self):
        if self.x + self.size > 800 or self.x < 0:
            self.xspeed *= -1
        if self.y + self.size > 500 or self.y < 0:
            self.yspeed *= -1
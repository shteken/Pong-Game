class Hittable:
    def __init__(self, start_x = 5, start_y = 240, width = 10, height = 50, color = (170,170,170)):
        self.width = width
        self.height = height
        self.start_x = start_x
        self.start_y = start_y
        self.color = color
    
    def get_coordinates(self):
        return self.start_x, self.start_y, self.start_x + self.width, self.start_y + self.height
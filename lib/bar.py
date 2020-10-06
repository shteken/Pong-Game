from hittable import Hittable

class Bar(Hittable):
    def accept(self, visitor):
        visitor.visit_bar(self)
    
    def move(self, x, y):
        self.start_x = x
        self.start_y = y
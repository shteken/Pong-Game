from hittable import Hittable

class Wall(Hittable):
    def accept(self, visitor):
        visitor.visit_wall(self)
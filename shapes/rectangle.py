from dataclasses import dataclass
from typing import List

from turtle import Vec2D

from .vertices_shape import VerticesShape

@dataclass
class Rectangle(VerticesShape):
    base:float
    height:float

    def list_vertices(self) -> List[Vec2D]:
        """Returns a list of the vertecies where the last vertex is the first vertex."""
        ll = self.start_pos
        lr = ll + Vec2D(self.base,0)
        ur = lr + Vec2D(0, self.height)
        ul = ur + Vec2D(-self.base, 0)
        return [ll, lr, ur, ul, ll]        

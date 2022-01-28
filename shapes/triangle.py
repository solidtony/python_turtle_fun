from dataclasses import dataclass
from typing import List

from turtle import Vec2D

from .vertices_shape import VerticesShape

@dataclass
class Triangle(VerticesShape):
    """Creates a triangle and draws

    Params:
        start_pos: A Vec2D that represents the left vertex of the triangle.
        base: The base of the triangle.
        height: The height of the triangle.
    """
    base:float
    height:float

    def list_vertices(self) -> List[Vec2D]:
        """Returns a list of the vertecies where the last vertex is the first vertex."""
        left = self.start_pos
        tip = self.start_pos + Vec2D(self.base/2,self.height)
        right = self.start_pos+Vec2D(self.base,0)
        return [left,right,tip,left]

from abc import abstractmethod
from dataclasses import dataclass
from typing import List

from turtle import Vec2D

from .shape import Shape

@dataclass
class VerticesShape(Shape):
    def draw(self):
        """Draws the triangle."""
        tmp_turtle = self.setup_turtle()
        for vertex in self.list_vertices():
            tmp_turtle.setpos(vertex)

    @abstractmethod
    def list_vertices(self) -> List[Vec2D]:
        """Returns a list of the vertecies where the last vertex is the first vertex."""
        pass

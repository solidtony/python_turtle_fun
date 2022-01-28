import math
from turtle import Vec2D,Turtle,setpos,penup,pendown
from dataclasses import dataclass
from typing import List

@dataclass
class Triangle:
    """Creates a triangle and draws

    Params:
        left_vertex: A Vec2D that represents the left vertex of the triangle.
        base: The base of the triangle.
        height: The height of the triangle.
    """
    base:float
    height:float
    left_vertex:Vec2D=Vec2D(0,0)

    @property
    def list_vertices(self) -> List[Vec2D]:
        """Returns a list of the vertecies where the last vertex is the first vertex."""
        left = self.left_vertex
        tip = self.left_vertex + Vec2D(self.base/2,self.height)
        right = self.left_vertex+Vec2D(self.base,0)
        return [left,tip,right,left]


    def setup_turtle(self) -> Turtle:
        """Returns a Turtle that is positioned at the left vertex."""
        tmp_turtle = Turtle()
        tmp_turtle.penup()
        tmp_turtle.setpos(self.left_vertex)
        tmp_turtle.pendown()
        return tmp_turtle

    def draw(self):
        """Draws the triangle."""
        tmp_turtle = self.setup_turtle()
        for vertex in self.list_vertices:
            tmp_turtle.setpos(vertex)

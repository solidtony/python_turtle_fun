from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field
from typing import ClassVar, List

from turtle import Vec2D,Turtle,setpos,penup,pendown

@dataclass
class Shape(metaclass=ABCMeta):
    """A Shape that can be drawn using turtle."""
    start_pos:Vec2D
    turtle:Turtle
    
    @abstractmethod
    def draw(self):
        pass

    def setup_turtle(self) -> Turtle:
        """Returns a Turtle that is positioned at the left vertex."""
        self.turtle.shape('turtle')
        self.turtle.penup()
        self.turtle.setpos(self.start_pos)
        self.turtle.pendown()
        return self.turtle

from dataclasses import dataclass

from turtle import Turtle,Vec2D

from .shape import Shape
from .triangle import Triangle
from .rectangle import Rectangle

class Error(Exception):
    pass

class RoofSizeError(Error):
    pass

@dataclass
class House(Shape):
    base:float
    height:float
    roof_height:float
    roof_base:float

    @property
    def house(self) -> Rectangle:
        return Rectangle(base=self.base,
                         height=self.height,
                         start_pos=self.start_pos,
                         turtle=self.turtle)

    @property
    def roof(self) -> Triangle:
        roof_start_pos = self.start_pos + Vec2D(-self.eve_length,self.height)
        return Triangle(base=self.roof_base,
                        height=self.roof_height,
                        start_pos=roof_start_pos,
                        turtle=self.turtle)

    @property
    def eve_length(self) -> float:
        return (self.roof_base-self.base)/2.0

    def draw(self):
        self.validate_roof_size()
        self.house.draw()
        self.roof.draw()

    def validate_roof_size(self):
        if self.roof_base < self.base:
            msg = 'The base of the roof cannot be smaller than the base of the house.'
            raise RoofSizeError(msg)

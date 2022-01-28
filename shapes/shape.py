from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

from turtle import Turtle

class Shape(metaclass=ABCMeta):
    """A Shape that can be drawn using turtle."""

    @abstractmethod
    def setup_turtle(self) -> Turtle:
        pass

    @abstractmethod
    def draw():
        pass

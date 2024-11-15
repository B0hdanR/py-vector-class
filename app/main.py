from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y,
        )

    def __mul__(self, other: float | Vector) -> Vector | int | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

        elif isinstance(other, (int, float)):
            return Vector(
                x=self.x * other,
                y=self.y * other,
            )

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            x=round(self.x / self.get_length(), 2),
            y=round(self.y / self.get_length(), 2),
        )

    def angle_between(self, other: Vector) -> int:
        return round((math.degrees
                      (math.acos((self * other) / (self.get_length()
                                                   * other.get_length())))))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)

        return Vector(
            x=math.cos(radians) * self.x - math.sin(radians) * self.y,
            y=math.sin(radians) * self.x + math.cos(radians) * self.y
        )

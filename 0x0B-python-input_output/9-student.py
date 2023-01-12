#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """Student class definition."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student class.

        Args:
            first_name(str): The student's first name
            last_name(str): The student's last name
            age(int): The student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of
            the student instance
        """
        return (self.__dict__)

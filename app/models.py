from enum import Enum, IntEnum
from typing import Union
from pydantic import BaseModel


# class ModelName(str, Enum):
#     hiyoonji = "hiyoonji"
#     yc0603 = "yc    0603"
#
#
# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None

class MainModel(IntEnum):
    first = 1
    second = 2
    third = 3
    fourth = 4
    fifth = 5


class SubModel(BaseModel):
    grade: Union[str, None] = None
    year: Union[int, None] = None
    month: Union[int, None] = None
    problem_number: Union[int, None] = None
    main: MainModel


class TypeModel(BaseModel):
    type_id: int


class ProblemModel(BaseModel):
    problem_id: int
    problem_source: Union[str, None] = None
    # problem_content: Union[str, None] = None
    type: TypeModel


class NewProblem(BaseModel):
    new_problem_id: int
    new_problem_content: Union[str, None] = None

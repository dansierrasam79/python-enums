# iterate over Enum objects
from enum import Enum
class studentMarks(Enum):
    Dan = 66
    Mark = 98
    Nutan = 33

for stud_marks in studentMarks:
    print(stud_marks.name)
    print(stud_marks.value)

# create Enum object
from enum import Enum
class studentMarks(Enum):
    Dan = 66
    Mark = 98
    Nutan = 33

print(studentMarks.Dan.name)
print(studentMarks.Dan.value)

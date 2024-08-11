# get unique enum vals
from enum import Enum
class studentMarks(Enum):
    Dan = 66
    Mark = 98
    Nutan = 33
    Swapan = 98

for sMark in studentMarks:
    print(sMark.name, sMark.value)

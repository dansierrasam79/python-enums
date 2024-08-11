#display enum class by values
from enum import IntEnum
class studentMarks(IntEnum):
    Dan = 66
    Mark = 98
    Nutan = 33
for stud_data in sorted(studentMarks):
    print(stud_data.name,stud_data.value)

# get values from enum class
from enum import Enum
student_marks_list = []
class studentMarks(Enum):
    Dan = 66
    Mark = 98
    Nutan = 33

for stud_data in studentMarks:
    student_marks_list.append(stud_data.value)
print(student_marks_list)

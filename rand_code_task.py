import random
from array_manips import task_num_names as arr_tasks
from string_manips import task_num_names as str_tasks
arr_number=random.randint(1,10)
str_number=random.randint(1,10)
print(f"Array #{arr_number}: {arr_tasks[arr_number]}")
print(f"Strings #{str_number}: {str_tasks[str_number]}")
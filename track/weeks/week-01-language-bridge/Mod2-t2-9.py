number_of_students =int(input())
total_marks=0
pass_count=0
fail_count=0
for i in range(number_of_students):
    marks=int(input())
    if marks >= 40:
        pass_count = pass_count+1
    else:
        fail_count = fail_count+1
    total_marks=total_marks+marks
print(f"Total Marks: {total_marks}")
print(f"Passed Students: {pass_count}")
print(f"Failed Students: {fail_count}")
if fail_count == 0:
    print("Batch Result: All Passed")
else:
    print("batch Result: Needs Improvement")

name = input()
course = input()
score = int(input())
student_record = (str(name), str(course), int(score))
name, course, score = student_record
print(f"Name: {str(name)}")
print(f"Course: {str(course)}")
print(f"Score: {int(score)}")
marks=int(input())
attendance_percentage= int(input())
project_completion= input()
if marks >= 60 and  attendance_percentage >=75:
    if project_completion == "yes":
        print("Eligibele")
    else:
        print("Not eligible")
else:
    print("Not eligible")    



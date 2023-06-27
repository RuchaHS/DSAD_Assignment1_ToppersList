# Reading and parsing input file
file1 = open("Input/inputPS08.txt")

with file1 as f_in:
    data = f_in.readlines()

flag=0
old_stud = []
new_stud = []
for line in data:
    record = line.replace("\n","")
    if record == "Register each student details as" or record == "Student ID, Subject1(S1), Subject2(S2), Subject3(S3).":
        continue
    elif record == "New student details:":
        flag=1
        continue
    else:
        if flag==0:
            old_stud.append(record)
        new_stud.append(record)

print(len(old_stud))
print(len(new_stud))

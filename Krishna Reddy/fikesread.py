import csv,json
data=[]
with open("student.csv",'r', newline="") as file:
    f=csv.DictReader(file)
    for f in file:
        data.append(f)
print(data)

with open("student.json",'w') as jsonfile:
    json.dump(data,jsonfile,indent=4)

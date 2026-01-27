students =[
    {"name":'s1',"score":85},
    {"name":'s2',"score":67},
    {"name":'s3',"score":56},
    {"name":'s4',"score":88},
]
h_score =0
topper=""
for student in students:
    if(student["score"]>h_score):
        h_score = student["score"]
        topper=student["name"]
print("student with higest score is ",topper)
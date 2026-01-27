 #You are given two lists of student IDs, 
# one for students enrolled in Math and one for
#  students in Science. Write a script that uses 
# sets to find: (a) Students enrolled in both courses. 
# (b) All unique students enrolled in either course.
#  (c) Students enrolled in Math but not Science.
m_students= [101,102,103,104,105]
s_students = [103,104,106,107,108]
m_set = set(m_students)
s_set = set(s_students)

both_courses = m_set.intersection(s_set)
print(both_courses)

all_courses = m_set.union(s_set)
print(all_courses)

m_mathonly = m_set -s_set
print(m_mathonly)
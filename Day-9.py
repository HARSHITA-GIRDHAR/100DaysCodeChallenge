'''
Grade of a student as per percentage marks
>=90 A+
80-90 A
60-80 B
50-60 C
<50 D
'''
per = float(input("Enter the percentage marks secured:"))
if per>=90:
    print("Grade is A+")
elif per>80:
    print("Grade is A")
elif per>60:
    print("Grade is B")
elif per>50:
    print("Grade is C")
else:
    print("Grade is D")
    
90

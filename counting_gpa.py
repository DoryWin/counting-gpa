def main():
    print("GPA Calculation")
    
    s1 = input("Enter the subject code :")
    c1 = int(input("Enter the credit of the subject : "))
    g1 = float(input("Enter the grade of the subject : "))

    s2 = input("Enter the subject code :")
    c2 = int(input("Enter the credit of the subject : "))
    g2 = float(input("Enter the grade of the subject : "))
   
    s3 = input("Enter the subject code :")
    c3 = int(input("Enter the credit of the subject : "))
    g3 = float(input("Enter the grade of the subject : "))

    point1 = c1*g1
    point2 = c2*g2
    point3 = c3*g3

    Total_credit = c1+c2+c3
    Total_grade = point1+point2+point3
    GPA = round(Total_grade/Total_credit,2)

    print("Subject\t\t", "Credit\t\t", "Grade")
    print("ICT112\t\t", "c1\t\t", "g1")
    print("ICT102\t\t", "c2\t\t", "g2")
    print("ICT123\t\t", "c3\t\t", "g3")
    print("Total GPA : ", GPA)
    
main()
    

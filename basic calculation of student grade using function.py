def check_sum(m1,m2,m3,m4,m5):
    return m1+m2+m3+m4+m5
def check_avg(total):
    return total/5
def display_grades(name,avg):
    print("student name:",name)
    if(avg>=80):
        print("A grade")
    elif(avg>=60):
        print("B grade")
    elif(avg>=40):
        print("c grade")
    else:
        print("your fail try to next attempt")
def main():
    name = "deepika"
    total=check_sum(70,80,90,97,87)
    avg=check_avg(total)
    display_grades(name,avg)
main()













    



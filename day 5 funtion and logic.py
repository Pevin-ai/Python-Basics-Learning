def check_vote(age):
    if age>=18:
        print("eligible for voting")
    else:
        print("not eligible for voting")

my_age=int(input("enter your age :"))
check_vote(my_age)

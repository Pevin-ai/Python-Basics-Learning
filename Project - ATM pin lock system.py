correct_pin="1234"
attempts=3
while attempts>0:
    user_input=input(f"enter your pin ({attempts} attempts left):")
    if user_input==correct_pin:
        print("success! you can withdrawl money.")
        break
    else:
        attempts=attempts-1
        print("wrong pin!")
if attempts==0:
  print("too many wrong attempts. your card is blocked for 24 hours!")

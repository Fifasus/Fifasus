price = 1000000
good_credit = input("Is your credit good? ")

if good_credit == "True":
    final_price = int(price) * 0.1
    msg = f"You have to put down ${final_price}"
    print(msg)

elif good_credit == "False":
    final_price = int(price) * 0.2
    msg = f"You have to put down ${final_price}"
    print(msg)

else: 
    print("Your answer should be True or False.")
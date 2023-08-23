import random
number_of_people = int(input("Enter the number of friends joining (including you):\n"))
people_dict = {}
if number_of_people <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")

    for _ in range(number_of_people):
        people_dict[str(input())] = 0

    bill_value = float(input("Enter the total bill value:\n"))

    luck_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if luck_feature == "Yes":
        luck_one = random.choice(list(people_dict.keys()))
        print(f"{luck_one} is the lucky one!")
        individual_bill = round(bill_value / (number_of_people - 1), 2)
        people_dict = {key: (individual_bill if key != luck_one else 0) for key, value in people_dict.items()}
        print(people_dict)

    else:
        print("No one is going to be lucky")
        individual_bill = round(bill_value / number_of_people, 2)
        people_dict = people_dict.fromkeys(people_dict, individual_bill)
        print(people_dict)

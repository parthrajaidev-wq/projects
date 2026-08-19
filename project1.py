#rent calculator

flat_rent = int(input("Enter the flat rent :"))
food_cost = int(input("Enter the food cost :"))
electricity_spend = int(input("Enter the electricity spend in units :"))
price_of_each_unit = int(input("Enter the price of each unit :"))
travel_cost = int(input("Enter the travel cost :"))
no_of_person = int(input("Enter the no of person :"))

Total_bill = flat_rent + food_cost + electricity_spend * price_of_each_unit + travel_cost
total_bill_per_person = Total_bill / no_of_person

print(f"Total bill spend by each person is {total_bill_per_person}")

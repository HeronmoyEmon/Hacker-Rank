def total(meal_cost,tip,tax):
    final = meal_cost*(1+((tip+ tax)/100))
    print(round(final))


meal_cost = float(input('Meal cost: '))
tip = int(input("Tip percentage: "))
tax = int(input("Tax percentage: "))

total(meal_cost,tip,tax)
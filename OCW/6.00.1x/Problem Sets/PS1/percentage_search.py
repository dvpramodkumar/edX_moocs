# House Hunting with Semi-annual raise
# finding portion saved using Bisection Search

from random import *

total_cost = 1000000.0
salary_hike = 0.07
portion_downpayment = 0.25
rate = 4 / 100
months_available = 36
current_savings = 0.0
total_downpayment = portion_downpayment * total_cost

low = 0.0
high = 0.7

counter_limit = 30
counter = 0

# Find rate
portion_saved = (low + high)/2
iter_interest = 0.0
iter_months = 0

while(True):
    counter += 1
    months_needed = 0
    annual_salary = 150000.0
    monthly_salary = annual_salary / 12
    current_savings = 0.0
    iter_interest = portion_saved
    iter_months = months_needed

    while(current_savings <= total_downpayment - 100.0):
        months_needed += 1

        if(months_needed > 36):
            break

        if(months_needed % 6 == 0):
            annual_salary = annual_salary + salary_hike * annual_salary
            monthly_salary = annual_salary / 12

        current_savings = current_savings + current_savings * \
            rate / 12 + portion_saved * monthly_salary

    if(months_needed > months_available and counter > counter_limit):
        print('It is not possible to pay the down payment in three years')
        break

    elif(counter <= counter_limit):

        if(months_needed > 36):
            iter_interest = portion_saved
            iter_months = months_needed
            low = portion_saved
            portion_saved = (low + high)/2
            continue

        if(round(abs(portion_saved - iter_interest), 2) <= 0.01):
            print('Best interest rate =', round(iter_interest, 2))
            print('Months needed for downpayment  =', months_needed)
            print('Steps in Bisection search =', counter)
            break

    else:
        print('It is not possible to pay the down payment in three years')
        break



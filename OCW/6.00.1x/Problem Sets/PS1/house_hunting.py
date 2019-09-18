# annual_salary = float(input('How much is your annual salary ?'))
# portion_saved = float(input('The portion of salary to be saved ?'))
# total_cost = float(input('The cost of your dream home ?'))

annual_salary = 120000.0
portion_saved = 0.1
total_cost = 1000000.0
portion_downpayment = 0.25
monthly_salary = annual_salary / 12
rate = 4 / 100
months_needed = 0
current_savings = 0.0

while(current_savings <= total_cost * portion_downpayment):
    months_needed += 1
    current_savings = current_savings + current_savings * \
        rate / 12 + portion_saved * monthly_salary

print('Number of months needed = ', months_needed)

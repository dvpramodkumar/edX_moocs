# House Hunting with Semi-annual raise

annual_salary = 120000.0
portion_saved = 0.05
total_cost = 500000.0
salary_hike = 0.03

portion_downpayment = 0.25
monthly_salary = annual_salary / 12
rate = 4 / 100
months_needed = 0
current_savings = 0.0

while(current_savings <= total_cost * portion_downpayment):
    months_needed += 1

    if(months_needed % 6 == 0):
        annual_salary = (1 + salary_hike) * annual_salary
        monthly_salary = annual_salary / 12

    current_savings = current_savings + current_savings * \
        rate / 12 + portion_saved * monthly_salary

print('Number of months needed = ', months_needed)

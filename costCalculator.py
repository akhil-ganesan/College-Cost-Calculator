# Define the principal, interest rate, and initial salary difference
principal = 225000
simple_interest_rate = 0.07
pub_sal = 90000
priv_sal = 105000
# These were manually calculated from median salary numbers (publics have greater growth due to a relateively lower starting salary)
pub_gr = 0.0215
priv_gr = 0.0206


# Initialize variables
loan_balance = principal
# The -pub_sal is included to account for early graduation
cumulative_salary_difference = -pub_sal
year = 0

def get_sal(gr, init, yr):
    return (init * (1 + gr) ** yr)

# Calculate the number of years needed for the cumulative salary difference to equal the loan balance using simple interest
while cumulative_salary_difference < loan_balance:
    # The year+1 is included to account for early graduation
    annual_salary_difference = get_sal(priv_gr, priv_sal, year) - get_sal(pub_gr, pub_sal, year+1)
    
    if (annual_salary_difference < 0):
        print(f"No convergence on a break-even year. Program stops at year {year}")
        break
    
    cumulative_salary_difference += annual_salary_difference
    
    loan_balance = principal * (1 + simple_interest_rate * year)
    year += 1

print(f"Year {year}, Priv Sal {get_sal(priv_gr, priv_sal, year)}, Pub Sal {get_sal(pub_gr, pub_sal, year)}")

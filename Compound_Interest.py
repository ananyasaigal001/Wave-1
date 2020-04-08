#obtaining the money deposited
savings = input("Enter the money deposited: ")
savings=float(savings)
#calculating money in savings account
one_year_savings= round(savings*(1+0.04),2)
two_year_savings= round(one_year_savings*(1+0.04),2)
three_year_savings= round(two_year_savings*(1+0.04),2)
#output
print("The savings after one year is $",one_year_savings,"after two years is $",two_year_savings,"after three years is $", three_year_savings)

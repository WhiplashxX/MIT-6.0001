portion_down_payment=0.25#首付

current_savings=0

r=0.04

annual_salary = float(input("Enter your annual salary:"))
total_cost = 1000000
semi_annual_raise = .07

target = 250000

month_salary = annual_salary/12

step=0
low=0.0
high=10000.0
rate=10000.0
while True :
    step+=1
    month_salary = annual_salary/12
    current_savings=0.0
    rate=float((low+high)/2.0)
    for i in range(1,37):
        if (i-1)%6==0 and i!=1:
            month_salary = (1+semi_annual_raise)*month_salary
        current_savings += current_savings*r/12 + month_salary*float(rate/10000)
    
    if abs(current_savings-target)<=100:
        break
    
    if current_savings > target:
        high=rate
        
    else:
        low=rate
        
    if low>=high:
        break
if low<=high:
    print("Best savings rate:",float(rate/10000.0)) 
    print("Steps in bisection search:",step)
else:
    print("error")









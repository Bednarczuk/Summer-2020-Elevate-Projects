class AerialImagery:
    pass

emp_1 = AerialImagery()
emp_2 = AerialImagery()

print(emp_1)
print(emp_2)

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 60000

emp_2.first = 'Test'
emp_2.last = 'Tester'
emp_2.email = 'Test.Schafer@company.com'
emp_2.pay = 50000

print(emp_1.email)
print(emp_2.email)
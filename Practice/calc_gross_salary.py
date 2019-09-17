basicSalary = int(input("Enter the basic salary : "))
dearnessAllowance = basicSalary * 40/100;
houseRentAllowance = basicSalary * 20/100;
grossSalary = basicSalary + dearnessAllowance + houseRentAllowance
print("Gross salary : {}".format(grossSalary))

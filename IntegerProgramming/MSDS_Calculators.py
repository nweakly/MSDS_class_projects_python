####Integer Programming
####

#############################################################################
############Manufacturing Scientific and Graphing Calculators###############
#####Word problem from https://www.purplemath.com/modules/linprog3.htm #####
############################################################################


#imports
from pulp import * #LP modeller

#Create a variable to contain the problem data
sales=LpProblem("CalculatorSales", LpMaximize)

#Create variables for scientific and graphing calculators
#Based on the projected demand
#lower limits for 100 for scientific calculators and 80 for graphing calculators
#Based on production limitations upper limits 200 for scientific and 170 for graphing calculators
i=LpVariable("scientific", 100, 200, LpInteger)
j=LpVariable("graphing", 80, 170, LpInteger)


# Add the objective function - maximize profits
sales += (-2)*i + 5 * j, "total $ sales"

#Add min shipment constraint constraint
sales += i + j >= 200, "min daily shipment" #contractual obligation to ship at least 200 calculators per day

#write data to an .lp file
sales.writeLP("Calculators.lp")

#Solve the problem using PuLP solver
sales.solve()

#View the status of the solution
print('Scenario 1:')
print(LpStatus[sales.status])

#View each variable for the optimum solution
for x in sales.variables():
    print(x.name, "=", x.varValue)

#View the optimized objective function
print('Total Calculators Sales $', value(sales.objective))


################Modify the problem: Scenario 2################################
#########Scientific calculators bring $1 of profit (instead of $2 loss)#######
#########All other conditions remain the same#################################
#############################################################################


#Create a variable to contain the problem data
sales2=LpProblem("CalculatorSales@", LpMaximize)

#Create variables for scientific and graphing calculators
#Based on the projected demand
#lower limits for 100 for scientific calculators and 80 for graphing calculators
#Based on production limitations upper limits 200 for scientific and 170 for graphing calculators
i2=LpVariable("scientific", 100, 200, LpInteger)
j2=LpVariable("graphing", 80, 170, LpInteger)


# Add the objective function - maximize profits
sales2 += i2 + 5 * j2, "total $ sales"

#Add min shipment constraint
sales2 += i2 + j2 >= 200, "min daily shipment" #contractual obligation to ship at least 200 calculators per day

#write data to an .lp file
sales2.writeLP("Calculators.lp")

#Solve the problem using PuLP solver
sales2.solve()

print('Scenario 2:')

#View the status of the solution
print(LpStatus[sales2.status])

#View each variable for the optimum solution
for z in sales2.variables():
    print(z.name, "=", z.varValue)

#View the optimized objective function
print('Total Calculators Sales $', value(sales2.objective))

################Modify the problem: Scenario 3################################
#########Scientific calculators bring $0 of profit (instead of $2 loss)#######
#########All other conditions remain the same#################################
#############################################################################


#Create a variable to contain the problem data
sales3=LpProblem("CalculatorSales@", LpMaximize)

#Create variables for scientific and graphing calculators
#Based on the projected demand
#lower limits for 100 for scientific calculators and 80 for graphing calculators
#Based on production limitations upper limits 200 for scientific and 170 for graphing calculators
i3=LpVariable("scientific", 100, 200, LpInteger)
j3=LpVariable("graphing", 80, 170, LpInteger)


# Add the objective function - maximize profits
sales3 += 5 * j3, "total $ sales"

#Add min shipment constraint
sales3 += i3 + j3 >= 200, "min daily shipment" #contractual obligation to ship at least 200 calculators per day

#write data to an .lp file
sales3.writeLP("Calculators.lp")

#Solve the problem using PuLP solver
sales3.solve()

print('Scenario 3:')

#View the status of the solution
print(LpStatus[sales3.status])

#View each variable for the optimum solution
for y in sales3.variables():
    print(y.name, "=", y.varValue)

#View the optimized objective function
print('Total Calculators Sales $', value(sales3.objective))
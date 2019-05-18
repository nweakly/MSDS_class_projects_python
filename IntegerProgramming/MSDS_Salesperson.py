####Integer Programming
####

####Salesperson's dilemma
###

#imports
from pulp import * #LP modeller

#Create a variable to contain the problem data
sales=LpProblem("DirectMarketing", LpMaximize)

#Create variables for two activities with the lower limits of 0

i=LpVariable("phone", 0, None, LpInteger)
j=LpVariable("direct", 0, None, LpInteger)


# Add the objective function - maximise commission collected
sales += 2.4*i + 9.3 * j, "dollars collected"

#Add time constraint
sales += 8* i + 18 * j <= 420, "time" #work no more than 7 hours per day

#write data to an .lp file
sales.writeLP("DirectMarketing.lp")

#Solve the problem using PuLP solver
sales.solve()

#View the status of the solution
print(LpStatus[sales.status])

#View each variable for the optimum solution
for x in sales.variables():
    print(x.name, "=", x.varValue)

#View the optimized objective function
print('Total Comission ', value(sales.objective))


###Change parameters: time spent on the phopne is reduces from 8 minutes to 5
sales2 = LpProblem("Direct Marketing",LpMaximize)
i=LpVariable("phone",0,None,LpInteger)
j=LpVariable("direct",0,None,LpInteger)
sales2 += 2.4 * i + 9.3 * j, "dollars collected"
sales2+= 5 * i + 18 * j <= 420, "time"
sales2.writeLP("DirectMarketing.lp")
sales2.solve()
print(LpStatus[sales2.status])
for y in sales2.variables():
    print(y.name, "=", y.varValue)
print('Total commission ', value(sales2.objective))


#Change parameters - Increase phone success rated from  5% to 7%
sales3 = LpProblem("Direct Marketing",LpMaximize)
i=LpVariable("phone",0,None,LpInteger)
j=LpVariable("direct",0,None,LpInteger)
sales3 += 3.36 * i + 9.3 * j, "dollars collected"
sales3 += 8 * i + 18 * j <= 420, "time"
sales3.writeLP("DirectMarketing.lp")
sales3.solve()
print(LpStatus[sales3.status])
for z in sales3.variables():
   print(z.name, "=", z.varValue)
print('Total commission ', value(sales3.objective))


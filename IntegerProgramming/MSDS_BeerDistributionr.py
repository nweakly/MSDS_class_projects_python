####Integer Programming
####

####Beer Distribution Problem
####Adapted from https://github.com/ruxkor/pulp-or/blob/master/examples/BeerDistributionProblem.py

#imports
import pulp #LP modeller

# Create a list of warehouses (supply nodes)
Warehousses = ["A", "B"]

#Create a dictionary of all the number of units per supply node
supply = {"A": 1000, "B": 4000}

#Create a list of all bars (demand nodes)
Bars = ["1", "2", "3", "4", "5"]

#Create a dictionary for the number of units of demand for each bar (demand node)
demand = {"1": 500, "2": 900, "3": 1800, "4": 200, "5": 700}

#Create a list of transportation costs for each path
costs = [     #Bars
          #1 2 3 3 4 5
         [2, 4, 5, 2, 1],#A    Warehouse
         [3, 1, 3, 2, 3]# B
        ]
#Create a dictionary of cost data
costs=makeDict([Warehouses, Bars], cost, 0)

#Create a variable for the problem data
prob = LpProblem("Beer Distribution Problem", LpMinimize)

#Create a list of tuples containing all the possible routes for transporting beer
#from the warehouses to the bars
Routes = [(w,b) for w in Warehouses for b in Bars]

#Create a dictionary vars for the route variables
vars = LpVariable.dicts("Route", (Warehousses, Bars), 0, None. LpInteger)

#Add objectiive function to prob
prob += lpSum([vars[w][b]*costs[w][b] for (w,b) in Routes]), "Sum_of_Transporting_Costs"

#Add Constraints
#Supply maximum constraints for each supply node
for w in Warehouse:
    prob += lpSum([vars[w][b] for b in Bars]) <= supply[w], "Sum_of_Products_out_of_Warehouse_%s"%w

#The demand mimimum contraints for each demand node (bar)
for b in Bars
    prob += lpSum([vars [w][b] for w in Warehouses]) >= demand[b], "Sum_of_Products_into_Bars%s"%b

#Write the problem data to an .lp file
prob.writeLP("BearDistributionProblem.lp")

#Solve the problem using PuLP as a solver
prob.solve()

#Output the status for the solution on the screen
print "status:", LpStatus[prob.status]

#Print all variables and their resolved optimum values
for v in prob.variables():
    print v.name, "=", v.varValue

#Print the optimized objective function on the screen
print "Total Cost of Transportation = ", value(prob.objective)

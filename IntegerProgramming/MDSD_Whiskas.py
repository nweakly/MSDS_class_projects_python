####Integer Programming


####Whiskas
####Adapted from https://pythonhosted.org/PuLP/CaseStudies/a_blending_problem.html

### The Simplified Whiskas Model, PuLP Modeller

#imports
from pulp import * #LP modeller

# Create the 'prob' variable to contain the problem data
#LpProblem fubction creates variable to hosld problem data
prob = LpProblem("The Whiskas Problem",LpMinimize)

#Create problem variables using LpVariable function
LpVariable("example", None, 100) #no lower bound, upper bound = 100

# Create beef and Chicken variables with a lower limit of zero
x1=LpVariable("ChickenPercent",0,None,LpInteger)
x2=LpVariable("BeefPercent",0)

# The objective function is added to 'prob' first
prob += 0.013*x1 + 0.008*x2, "Total Cost of Ingredients per can"

# Adding the constraints
prob += x1 + x2 == 100, "PercentagesSum"
prob += 0.100*x1 + 0.200*x2 >= 8.0, "ProteinRequirement"
prob += 0.080*x1 + 0.100*x2 >= 6.0, "FatRequirement"
prob += 0.001*x1 + 0.005*x2 <= 2.0, "FibreRequirement"
prob += 0.002*x1 + 0.005*x2 <= 0.4, "SaltRequirement"

#Use writeLP() function to copy infornmation into a .lp file

# The problem data is written to an .lp file
prob.writeLP("WhiskasModel.lp")

#Use PuLP solver to solve the problem
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen
print("Total Cost of Ingredients per can = ", value(prob.objective))

############################################
######Full formulation Whiskas problem######
############################################

####Create a list of possible ingredients
Ingredients = ['CHICKEN', 'BEEF', 'MUTTON', 'RICE', 'WHEAT', 'GEL']

# Create a dictionary with the costs for each of the ingredients
costs = {'CHICKEN': 0.013,
         'BEEF': 0.008,
         'MUTTON': 0.010,
         'RICE': 0.002,
         'WHEAT': 0.005,
         'GEL': 0.001}

# Create a dictionary of the protein percent in each of the Ingredients
proteinPercent = {'CHICKEN': 0.100,
                  'BEEF': 0.200,
                  'MUTTON': 0.150,
                  'RICE': 0.000,
                  'WHEAT': 0.040,
                  'GEL': 0.000}

# Create a dictionary of the fat percent in each of the Ingredients
fatPercent = {'CHICKEN': 0.080,
              'BEEF': 0.100,
              'MUTTON': 0.110,
              'RICE': 0.010,
              'WHEAT': 0.010,
              'GEL': 0.000}

# Create a dictionary of the fibre percent in each of the Ingredients
fibrePercent = {'CHICKEN': 0.001,
                'BEEF': 0.005,
                'MUTTON': 0.003,
                'RICE': 0.100,
                'WHEAT': 0.150,
                'GEL': 0.000}

# Create a dictionary of the salt percent in each of the Ingredients
saltPercent = {'CHICKEN': 0.002,
               'BEEF': 0.005,
               'MUTTON': 0.007,
               'RICE': 0.002,
               'WHEAT': 0.008,
               'GEL': 0.000}

# Create the 'prob' variable to contain the problem data
prob = LpProblem("The Whiskas Problem", LpMinimize)

# Create a dictionary 'ingredient_vars' to contain the Variables for the problem
ingredient_vars = LpVariable.dicts("Ingr",Ingredients,0) #Lower bound is zero

# The objective function is added to 'prob' first
#use lpSum() function to add the elements
#use costs and ingredient_vars dictionaries ro extract data using ingridient names as keys
prob += lpSum([costs[i]*ingredient_vars[i] for i in Ingredients]), "Total Cost of Ingredients per can"

# Adding the constraints to 'prob'
prob += lpSum([ingredient_vars[i] for i in Ingredients]) == 100, "PercentagesSum"
prob += lpSum([proteinPercent[i] * ingredient_vars[i] for i in Ingredients]) >= 8.0, "ProteinRequirement"
prob += lpSum([fatPercent[i] * ingredient_vars[i] for i in Ingredients]) >= 6.0, "FatRequirement"
prob += lpSum([fibrePercent[i] * ingredient_vars[i] for i in Ingredients]) <= 2.0, "FibreRequirement"
prob += lpSum([saltPercent[i] * ingredient_vars[i] for i in Ingredients]) <= 0.4, "SaltRequirement"

#Use writeLP() function to copy infornmation into a .lp file

# The problem data is written to an .lp file
prob.writeLP("WhiskasModel.lp")

#Use PuLP solver to solve the problem
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen
print("Total Cost of Ingredients per can = ", value(prob.objective))
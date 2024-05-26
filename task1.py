import pulp

prob = pulp.LpProblem("Напої", pulp.LpMaximize)
lemonade = pulp.LpVariable('лимонад', lowBound=0, upBound=50)
fruit_juice = pulp.LpVariable('фруктовий сік', lowBound=0, upBound=20)

prob += lemonade + fruit_juice

prob += 2 * lemonade + fruit_juice <= 100
prob += lemonade <= 50
prob += lemonade <= 30
prob += 2 * fruit_juice <= 40

prob.solve()

[print(v.name, "=", v.varValue) for v in prob.variables()]

# лимонад = 30.0
# фруктовий_сік = 20.0
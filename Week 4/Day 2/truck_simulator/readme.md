# Truck simulator  

## Modules  
### Truck
Attributes:  
max_fuel_amount: the maximum amount of fuel the truck can have  
km_per_liter: how much killometers can the truck travers per liter  
price_repair_per_km: how much it will cost to repair truck per km
brand: truck brand
functions:  
for each attribute there is a get function to return its value

### traversal_calculator
Attributes:  
roads: a list of dictionaries, each dictionary has a road type and the function that calucaltes the max distance a truck could dirve on that road

functions:  
can_travel:  
check if the given truck can travel on the given road with the given length   

### utils
laod all the roads moduls into the roads list in traversal_calculator
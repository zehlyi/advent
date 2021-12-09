
fuel = 0
f = open("input1.txt", "r")
for line in f:
    mass = int(line.strip())
    my_fuel = mass / 3 - 2
    extra_fuel = my_fuel / 3 - 2

    while extra_fuel > 0:
        print "+", extra_fuel
        my_fuel += extra_fuel
        extra_fuel = extra_fuel / 3 - 2

    fuel += my_fuel
print fuel 

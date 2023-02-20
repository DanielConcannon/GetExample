weight = float(input("Weight: "))
metric = input("(K)g or (L)bs: ")
if metric.upper =="L":
    converted = weight * 2.2
    print("Weight in KG: " + str(converted))
else:
    converted = weight / 2.2
    print("Weight in LB: " + str(converted))
    print
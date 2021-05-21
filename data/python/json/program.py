import json
fp_1 = input("Enter first filepath: ")
fp_2 = input("Enter second filepath: ")
fp_out = input("Enter output filepath: ")
with open(fp_1) as f1:
    d1 = json.load(f1)
with open(fp_2) as f2:
    d2 = json.load(f2)
merged ={key : value for key, value in list(d1.items()) + list(d2.items())}
with open(fp_out, "w") as fo:
    json.dump(merged, fo, indent=4)
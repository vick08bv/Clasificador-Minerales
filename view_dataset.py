import matplotlib.pyplot as plt
import re

minerals = dict()
many = dict()

with open("list_image_urls.csv") as file:
    lines = file.readlines()
    print("total")
    print(len(lines))
    for line in lines:
        label = line.split(",")[1].lstrip()
        if label in minerals:
            minerals[label] += 1
        else:
            minerals[label] = 1
print("categories")
print(len(minerals))
lower_b = 5000
upper_b = 30000

print("less")
print(len([i for i in minerals.values() if i <= lower_b]))
print("middle")
print(len([i for i in minerals.values() if lower_b < i <= upper_b]))
print("greater")
print(len([i for i in minerals.values() if i > upper_b]))

print("excluded")
for mine in minerals:
    if lower_b < minerals[mine] <= upper_b:
        many[mine] = minerals[mine]
    if minerals[mine] > upper_b:
        print(mine, minerals[mine])

print("remaining entries")
print(sum(many.values()))
print("average")
print(sum(many.values())/len(many))
print("labels")
print(many)

m_list = list(many.keys())
m_mod = []
patron = r"\(Var: ([^\)]+)\)"

for k in m_list:
    c = re.search(patron, k)
    if c:
        m_mod.append(c.group(1))

for m in m_list:
    print(m)

# plt.hist(many.values(), bins=range(lower_b, upper_b, 1))
# plt.show()

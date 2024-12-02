f = open("input.txt", "r")
# print(f.read())

# a = []
# b = []

# for line in f.readlines():
#     lint = line.strip()
#     split = line.split("   ")
#     a.append(int(split[0]))
#     b.append(int(split[1].strip()))

# print(a)
# print(b)

# sum = 0

# for i in range(len(a)):
#     t = min(a)
#     g = min(b)
#     sum += abs(t - g)
#     a.remove(t)
#     b.remove(g)

# print(sum)

a = []
b = []

n = []
for line in f.readlines():
    lint = line.strip()
    split = line.split("   ")
    a.append(int(split[0]))
    b.append(int(split[1].strip()))

print(a)
print(b)

sum = 0

for i in a:
    if i not in n:
        sum += i * b.count(i)
        n.append(i)

print(sum)

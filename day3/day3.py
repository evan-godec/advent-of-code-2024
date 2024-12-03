import re

def multiplier(str):
    split = str.split(",")
    val1 = split[0]
    val1 = int(val1.replace(val1[:4], ''))
    val2 = split[1]
    val2 = int(val2.replace(val2[-1], ''))
    return val1 * val2


f = open("input.txt", "r")

pattern = "mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

mul = "mul\(\d{1,3},\d{1,3}\)"
do = "do\(\)"
dont = "don't\(\)"


list = re.findall(pattern, f.read())

sum = 0
enable = True

for i in list:
    if(re.match(dont, i)):
        enable = False
    elif(re.match(do, i)):
        enable = True
    elif(re.match(mul, i) and enable == True):
        res = multiplier(i)
        sum += res
    
print(sum)


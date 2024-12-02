import numpy as np

f = open("input.txt", "r")

sum = 0
for line in f.readlines():
    split = line.strip().split(" ")
    for i in range (len(split)):
        split[i] = int(split[i])
    passe = False
    for j in range(len(split)):
        temp = np.delete(split, j)
        diff_list = np.diff(temp)
        if (all((i <= 3 and i> 0) or (i >= -3 and i<0) for i in diff_list)):
            if(all(i <= 0 for i in diff_list) or all(i >= 0 for i in diff_list)):
                passe = True
    diff_list_bis = np.diff(split)
    if (all((i <= 3 and i> 0) or (i >= -3 and i<0) for i in diff_list_bis)):
        if(all(i <= 0 for i in diff_list_bis) or all(i >= 0 for i in diff_list_bis)):
            passe = True
    if(passe):
        sum += 1
print(sum)

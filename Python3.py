listem = [4, 6, 3, 6, 8, 1, 4, 6, 3, 7, 2, 1]
listem2 = []
for i in listem:
  if i not in listem2:
    listem2.append(i)
print(listem2)
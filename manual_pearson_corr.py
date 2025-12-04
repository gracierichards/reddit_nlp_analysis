import math

X = [3.63, 3.02, 3.82, 3.42, 3.59, 2.87, 3.03, 3.46, 3.36, 3.30]
y = [53.1, 49.7, 48.4, 54.2, 54.9, 43.7, 47.2, 45.2, 54.4, 50.4]
sumx2 = 0
for n in X:
  sumx2 += n**2
sumy2 = 0
for n in y:
  sumy2 += n**2

cross = 0
for m, n in zip(X, y):
  cross += m * n

pearson = (len(X) * cross - sum(X) * sum(y))/math.sqrt((len(X) * sumx2 - sum(X)**2) * (len(X) * sumy2 - sum(y) ** 2))
print(pearson)
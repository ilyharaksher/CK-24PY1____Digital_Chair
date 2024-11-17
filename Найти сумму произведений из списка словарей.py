# TODO решите задачу
#def task() -> float:
# #print(task())
#import os
#print(os.listdir())
f = open("input.json", 'r')
Lasagna = f.readlines()
#print(Lasagna)
Scores = []
Weights = []
for i in Lasagna:
    if 'score' in i:
        score = float(i[13:-2])
        Scores.append(score)
    elif 'weight' in i:
        weight = float(i[14:])
        Weights.append(weight)
#print(Scores)
#print(Weights)
sum = 0
for i in range(len(Scores)):
    sum += Scores[i] * Weights[i]
print(round(sum, 3))

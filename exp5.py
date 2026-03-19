import math
points = [[2,4], [4,6], [4,4], [6,2]]
labels = ['A','A','B','B']
test = [5,5]
k = 3
distances = []
for i in range(len(points)):
    d = math.sqrt((points[i][0]-test[0])**2 + (points[i][1]-test[1])**2)
    distances.append((d, labels[i]))
distances.sort()
neighbors = []
for i in range(k):
    neighbors.append(distances[i][1])
prediction = max(set(neighbors), key=neighbors.count)
print("Test Point:", test)
print("Predicted Class:", prediction)

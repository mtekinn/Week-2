import math

# example points
points = [(1, 2), (4, 6), (5, 9), (8, 3)]

# function to calculate euclidean distance between two points
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)


# print the minimum distance
min_distance = min(distances)
print(min_distance)

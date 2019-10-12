import sys
import math
import numpy
import matplotlib


def multilaterate(distances):
    spheres = []
    circles = []
    combineddimensions = []
    for landmark in distances:
        circles.append(landmark)

        # sphere = math.pow((x-a), 2) + math.pow((y-b), 2) + math.pow((z-c), 2)
    theta = calcTheta(circles[0], circles[1])
    distancebetween = distance(circles[0], circles[1])
    print("distance between: " + str(distancebetween))
    print("theta: " + str(theta))
    print("H: " + str(calcCircle(circles[0], circles[1], theta)))

    print("circle coordinate: " + str(findIntersection(circles[0], circles[1])))
    return [0., 0., 0., 0.]
# (x,y for circle)


def findIntersection2(landmark1, landmark2):
    x1 = landmark1[0]
    x2 = landmark2[1]
    y1 = landmark1[0]
    y2 = landmark2[1]
    r1 = landmark1[3]
    r2 = landmark2[3]


def findIntersection(landmark1, landmark2):
    x1 = landmark1[0]
    x2 = landmark2[1]
    y1 = landmark1[0]
    y2 = landmark2[1]
    r1 = landmark1[3]
    r2 = landmark2[3]
    d = distance(landmark1, landmark2)
    l = ((math.pow(r1, 2) - math.pow(r2, 2) + math.pow(d, 2)) / (2*d))
    h = math.sqrt(math.pow(r1, 2)-math.pow(l, 2))

    x = (l/d)*(x2-x1) + (h/d)*(y2-y1) + x1
    y = (l/d)*(y2-y1) - (h/d)*(x2-x1) + y1
    return ([x, y])


def distance(landmark1, landmark2):
    return math.sqrt(math.pow(landmark1[0]-landmark2[0], 2)+math.pow(
        landmark1[1]-landmark2[1], 2)+math.pow(landmark1[2]-landmark2[2], 2))


def calcTheta(landmark1, landmark2):
    r1 = landmark1[3]
    r2 = landmark2[3]
    d = distance(landmark1, landmark2)
    value = (math.pow(r1, 2)+math.pow(d, 2)-math.pow(r2, 2))/(2*r1*d)
    theta = math.acos(value)
    return theta


def calcCircle(landmark1, landmark2, theta):
    h = landmark1[3]*math.sin(theta)
    d = distance(landmark1, landmark2)
    r1 = landmark1[3]
    r2 = landmark2[3]

    h1 = math.sqrt(4*math.pow(r1, 2)*math.pow(d, 2)-math.pow(
        math.pow(r1, 2)+math.pow(d, 2)-math.pow(r2, 2), 2))/(2*d)

    return h


def similarColumns():
    spheres = []
    circles = []
    combineddimensions = []
    for landmark in distances:
        circles.append(landmark)

    for circle in circles:
        count = 0
        possibledimensions = []
        # xdimension check for similar
        for i in range(0, len(circles)):
            if count == i:
                continue
            if circle[0] == circles[i][0]:
                possibledimensions.append(['x', i])
        # ydimension check for similar
        for j in range(0, len(circles)):
            if count == j:
                continue
            if circle[1] == circles[j][1]:
                possibledimensions.append(['y', j])
        # xdimension check for similar
        for k in range(0, len(circles)):
            if count == k:
                continue
            if circle[2] == circles[k][2]:
                possibledimensions.append(['z', k])
        combineddimensions.append(possibledimensions)
        count = count+1
        print(circle)
        print(possibledimensions)


def distanceFunction():
    x = landmark[0]
    y = landmark[1]
    z = landmark[2]
    d = landmark[3]

    firstPyth = 0
    distance_away = 0
    if(x == 0 and y == 0):
        firstPyth = 0
    elif(x == 0):
        firstPyth = y
    elif(y == 0):
        firstPyth = x

    firstPyth = math.sqrt(math.pow(x, 2)+math.pow(y, 2))

    if(firstPyth != 0 and z > 0):
        secondPyth = math.sqrt(math.pow(firstPyth, 2)+math.pow(z, 2))
    elif(firstPyth == 0):
        secondPyth = z
    elif(z == 0):
        secondPyth = 0

    print(landmark)
    print("first: " + str(firstPyth))
    print("Second: " + str(secondPyth))


if __name__ == "__main__":

    # Retrive file name for input data
    if(len(sys.argv) == 1):
        print("Please enter data file name.")
        exit()

    filename = sys.argv[1]

    # Read data
    lines = [line.rstrip('\n') for line in open(filename)]
    distances = []
    for line in range(0, len(lines)):
        distances.append(list(map(float, lines[line].split(' '))))

    # Print out the data
    print("The input four points and distances, in the format of [x, y, z, d], are:")
    for p in range(0, len(distances)):
        print(*distances[p])

    # Call the function and compute the location
    location = multilaterate(distances)
    print
    print("The location of the point is: " + str(location))

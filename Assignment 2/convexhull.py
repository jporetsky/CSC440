import math
import sys

EPSILON = sys.float_info.epsilon

'''
Given two points, p1 and p2,
an x coordinate, x,
and y coordinates y3 and y4,
compute and return the (x,y) coordinates
of the y intercept of the line segment p1->p2
with the line segment (x,y3)->(x,y4)
'''
def yint(p1, p2, x, y3, y4):
	x1, y1 = p1
	x2, y2 = p2
	x3 = x
	x4 = x
	px = ((x1*y2 - y1*x2) * (x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / \
		 float((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))
	py = ((x1*y2 - y1*x2)*(y3-y4) - (y1 - y2)*(x3*y4 - y3*x4)) / \
			float((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3-x4))
	return (px, py)

'''
Given three points a,b,c,
computes and returns the area defined by the triangle
a,b,c. 
Note that this area will be negative 
if a,b,c represents a clockwise sequence,
positive if it is counter-clockwise,
and zero if the points are collinear.
'''
def triangleArea(a, b, c):
	return (a[0]*b[1] - a[1]*b[0] + a[1]*c[0] \
                - a[0]*c[1] + b[0]*c[1] - c[0]*b[1]) / 2.0;

'''
Given three points a,b,c,
returns True if and only if 
a,b,c represents a clockwise sequence
(subject to floating-point precision)
'''
def cw(a, b, c):
	return triangleArea(a,b,c) < -EPSILON;
'''
Given three points a,b,c,
returns True if and only if 
a,b,c represents a counter-clockwise sequence
(subject to floating-point precision)
'''
def ccw(a, b, c):
	return triangleArea(a,b,c) > EPSILON;

'''
Given three points a,b,c,
returns True if and only if 
a,b,c are collinear
(subject to floating-point precision)
'''
def collinear(a, b, c):
	return abs(triangleArea(a,b,c)) <= EPSILON

'''
Given a list of points,
sort those points in clockwise order
about their centroid.
Note: this function modifies its argument.
'''
def clockwiseSort(points):
	# get mean x coord, mean y coord
	xavg = sum(p[0] for p in points) / len(points)
	yavg = sum(p[1] for p in points) / len(points)
	angle = lambda p:  ((math.atan2(p[1] - yavg, p[0] - xavg) + 2*math.pi) % (2*math.pi))
	points.sort(key = angle)

def merge(left, right):
	#Find the upper tangent
	i=0
	j=0
	while((yint(left[i], right[j+1], left[i][0], left[i][1], right[j+1][1]) > yint(left[i], right[j], left[i][0], left[i][1], right[j][1])) or (yint(left[i-1], right[j], left[i-1][0], left[i-1][1], right[j]) > yint(left[i], right[j], left[i][0], left[i][1], right[j][1]))):
		if yint(left[i], right[j+1]) > yint(left[i], right[j]):	#move right finger clockwise
			j= (j+1) % len(right)	#if we have q points in B
		else:
			i= (i-1) % len(left)	#if we have p points in A

	mergedHull = {left[i], right[j]} #place the upper tangent points in the new merged hull

	#Find the lower tangent
	i=0
	j=0
	while((yint(left[i], right[j+1], left[i][0], left[i][1], right[j+1][1]) > yint(left[i], right[j], left[i][0], left[i][1], right[j][1])) or (yint(left[i-1], right[j], left[i-1][0], left[i-1][1], right[j]) > yint(left[i], right[j], left[i][0], left[i][1], right[j][1]))):
		if yint(left[i], right[j-1]) < yint(left[i], right[j]):	#move right finger clockwise
			j= (j-1) % len(right)	#if we have q points in B
		else:
			i= (i+1) % len(left)	#if we have p points in A

	#add the lower tangent to the end of the new merged hull
	mergedHull.append(left[i])
	mergedHull.append(right[j])

'''
Replace the implementation of computeHull with a correct computation of the convex hull
using the divide-and-conquer algorithm
'''
def computeHull(points):
	#base case of three points
	if(len(points) == 3):
		print((triangleArea(points[0], points[1], points[2])))
		return points
	#sort the given points if they are not already
	clockwiseSort(points)
	#separate the current points into two halves until the base case is reached
	left_convex = computeHull(points[0:int(len(points)/2)])
	right_convex = computeHull(points[int(len(points)/2):])
	#merge the two halves back together to find the convex hull
	merge(left_convex, right_convex)
	return points
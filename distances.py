# Returns the square root of the total squared difference between the points
def euclidean(pt1, pt2):
	distance = 0
	for pt in range(len(pt1)):
		distance += (pt1[pt] - pt2[pt) ** 2
	return distance ** 0.5

# Returns the absolute value of the total difference between the points
def manhattan(pt1, pt2):
	distance = 0
	for pt in range(len(pt1)):
		distance += abs(pt1[pt] - pt2[pt])
	return distance

# Returns the total error between the points
def hamming(pt1, pt2):
	distance = 0
	for pt in range(len(pt1)):
		if pt1[pt] != pt2[pt]:
			distance += 1
	return distance

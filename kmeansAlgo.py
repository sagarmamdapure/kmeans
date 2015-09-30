from random import randint
from math import sqrt
def calculateDistance(x1,y1,x2,y2):
	return sqrt(((x2-x1)**2)+((y2-y1)**2))
def calculateClusterCenters(clusters):
	clusterCenter = []
	for points in clusters:
		meanX, meanY = 0,0
		for x,y in points:
			meanX, meanY = meanX + x, meanY + y
		if len(points) != 0:
			meanX ,meanY = meanX/len(points),meanY/len(points)
		clusterCenter += [[meanX,meanY]]
	return clusterCenter
def getPerfectCluster(x,y,clusterCenters):
	dists = []
	for x1,y1 in clusterCenters:
		dists += [calculateDistance(x,y,x1,y1)]
	return dists.index(min(dists))
def makeCluster(points,number):
	clusterCenters = points[:number]
	oldClusterCenters = [[0,0] for i in range(number)]
	while oldClusterCenters != clusterCenters:
		clusters, oldClusterCenters = [[] for i in range(number)], clusterCenters
		for x,y in points:
			clusters[getPerfectCluster(x,y,clusterCenters)] += [[x,y]]
		clusterCenters = calculateClusterCenters(clusters)
	return clusters, clusterCenters
if __name__=="__main__":
	pointsNum = int(raw_input("How many points to use?\n"))
	clusterNum = int(raw_input("How many clusters you want to create?\n"))
	points = [[randint(-1000,1000),randint(-1000,1000)]for i in range(pointsNum)]
	clusters,clusterCenters = makeCluster(points, clusterNum)
	print clusters

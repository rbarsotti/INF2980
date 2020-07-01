######################
######## CVRP ########
######################

import pandas as pd
import math as m
import random


######################
##### Read Files #####
######################

capacity = 12
l = [(id,x,y,demand)]

######################
### Aux  Functions ###
######################

def d(a,b):
	return m.sqrt((a[1] - a[2])**2 + (b[1] - b[2])**2)

def sumDemand(l):
	s = 0
	for i in l:
		s += i[3]

def closestNode(node,l,capacity):
	dist_min = 0
	node_min = 0
	for i in l:
		if i[0] != node[0]:
			dist_i = d(node,l)
			if dist_i < dist_min and i[3] > 0:
				dist_min = dist_i
				node_min = i
	return node_min

def genSolution(l,total_demand,capacity):
	solution = [l[0]]
	c = sumDemand(l)
	capacity_i = capacity 
	while c > 0:
		node_i = solution[-1]
		next_node = closestNode(node_i,l,capacity_i)
		solution.append(next_node)
		if next_node[3] >= capacity_i:
			l[next_node[0]][3] -= capacity_i
			capacity_i = 0
			solution.append(l[0])
		else:
			capacity_i -= next_node[3]
			l[next_node[0]][3] = 0
	return solution

def totalCost(solution):
	cost = 0
	for i in range(len(solution)-1):
		cost += d(solution[i+1],solution[i])
	return cost

def deltaCost(solution):
	cost = []
	for i in range(len(solution)-1):
		cost.append((d(solution[i+1],solution[i]),i+1))
	return cost.sort(key=lambda x:x[0])

def getDepots(solution):
	l = []
	c = 0
	for i in solution:
		if i[0] == 0:
			l.append(c)
		c += 1


######################
# Destroy Heuristics #
######################

destroy_heuistics = []

def randomRemoval(solution,alpha):
	r = random.randint(int((len(solution)-1)*alpha))
	for i in r:
		index = random.randint(1,len(solution) - 1)
		solution[index] = ()
	return solution

def worstRemoval(solution,alpha):
	r = random.randint(int((len(solution)-1)*alpha))
	cost = deltaCost(solution)[-1:-r]
	for i in range(len(solution)):
		if solution[i] in cost:
			solution[i] = ()
	return solution

def relatedRemoval(solution):
	depots = getDepots(solution)
	r = random.randint(len(depots)-2)
	for i in range(depots[r],depots[r+1]):
		solution[i] = ()
	return solution


######################
#  Repair Heuristics #
######################

repair_heuristics = []

def basicGreedy(solution):
	return


######################
######## ALNS ########
######################

def 

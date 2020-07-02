######################
######## CVRP ########
######################

import pandas as pd
import math as m
import random


######################
##### Read Files #####
######################


######################
#  Global Variables  #
######################

capacity
l = [(id,x,y,demand)]
request_bank = [(id,x,y,demand)]
depot = ()


######################
### Aux  Functions ###
######################

def d(a,b):
	return m.sqrt((a[1] - a[2])**2 + (b[1] - b[2])**2)

def sumDemand(l):
	s = 0
	for i in l:
		s += i[3]

def closestPossibleNode(node,l,capacity_i):
	dist_min = 10**3
	node_min = 0
	for i in l:
		if i[0] != node[0]:
			dist_i = d(node,i)
			if dist_i < dist_min and i[3] < capacity_i:
				dist_min = dist_i
				node_min = i
	return node_min

def genSolution():
	routes = []
	total_demand = sumDemand(l)
	c = 0
	while c < total_demand:
		capacity_i = capacity
		node_i = l[0]
		route_i = [node_i]
		while True:
			next_node = closestPossibleNode(node_i,l,capacity_i)
			if next_node != 0:
				route_i.append(next_node)
				node_i = next_node
				capacity_i -= next_node[3]
				c += next_node[3]
			else:
				route_i.append(l[0])
				break
		routes.append(route_i)
	return routes


def routeCost(route):
	c = 0
	for i in route:
		c += i[3]

def totalCost(routes):
	c = 0 
	for i in routes:
		c += routeCost(i)

def closestPossibleRoute(node,routes):
	d = 10**3
	closest_route = None 
	for i in range(len(routes)):
		if routeCost(routes[i]) + node[3] <= capacity:
			for j in i:
				d_i = d(node,j)
				if d_i < d:
					d = d_i
					closest_route = i
	return closest_route

def worstCost(route):
	d = d(route[1],route[0])
	index = 1  
	for i in range(len(route)-1):
		if d(route[i+1],route[i]) >= d:
			index = i
	return index

######################
# Destroy Heuristics #
######################

destroy_heuristics = [randomRemoval]

def randomRemoval(routes):
	q = random.randint(int(len(routes)*0.1))
	for i in range(q):
		route_i = random.randint(len(routes)-1)
		request_index = random.randint(len(route_i)-1)
		request_bank.append(route_i[request_index])
		route_i.remove(route_i[request_index])
		return routes

def worstRemoval(routes):
	q = random.randint(int(len(routes)*0.1))
	for i in range(q):
		route_index = random.randint(len(routes)-1)
		route_i = routes[route_index]
		request_index = worstCost(route_i)
		request_bank.append(route_i[request_index])
		route_i.remove(route_i[request_index])
	return routes

def clusterRemoval(routes):
	q = random.randint(int(len(routes)*0.1))
	for i in range(q):
		route_index = random.randint(len(routes)-1)
		route_i = routes[route_index]
		for j in route_i:
			request_bank.append(j)
		routes.remove(route_i)
	return routes



######################
#  Repair Heuristics #
######################

repair_heuristics = [basicGreedy]

def basicGreedy(routes):
	for request in request_bank:
		closest_route = closestPossibleRoute(request,routes)
		routes[closest_route].append(request)
	return routes



######################
######## ALNS ########
######################

def ALNS(max_iter):
	x_i = genSolution()
	x = x_i
	c = 0
	while c < max_iter:
		destroy_i = pickDestroy(destroy_heuristics)
		x_i = destroy_i(x_i)
		repair_i = pickRepair(repair_heuristics)
		x_i = repair_i(x_i)
		if totalCost(x_i) < totalCost (x):
			x = x_i
	return x




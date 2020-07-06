######################
######## ALNS ########
######################

heuristic = [(heuristic, number_of_calls, pi)]
pi_remove = [(randomRemoval,0,0.333),(worstRemoval,0,0.333),(clusterRemoval,0,0.333)]
pi_insert = [(basicGreedy,0,0.5),(regretGreedy,0,0.5)]

def rouletteWheel(pi_list):
	p = random.random() #Uniforme [0,1]	
	for i in pi_list:
		p -= i[2]
		if p <= 0:
			i[1] += 1
			return i

def updatePi(heuristic,pi_i,pi_list,rho):
	if iteration % 100 == 0:
		pi_i = totalCost(x_i)
		for i in pi_list:
			i[2] = rho*(pi_i/i[1]) + (1-rho)*i[2]


def ALNS(max_iter):
	x_i = genSolution()
	x = x_i
	c = 0
	while c < max_iter:
		destroy_i = rouletteWheel(destroy_heuristics)[0]
		x_i = destroy_i(x_i)
		repair_i = rouletteWheel(repair_heuristics)[0]
		x_i = repair_i(x_i)
		if totalCost(x_i) < totalCost (x):
			x = x_i
	return x
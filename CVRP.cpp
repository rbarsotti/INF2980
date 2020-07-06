#include <iostream>
#include <cmath>
using namespace std;


struct Node {
	int id;
	int x;
	int y;
	int demand;
};

int capacity;
int n = 100;
struct Node nodes[100];


/* Destroy Heuristics */



/* Repair Heuristics */



/* ALNS */


/* AUX Functions */

float d(struct Node a, struct Node b) {
	float distance;
	distance = sqrt(pow((a.x - b.x),2) + pow((a.y - b.y),2));
	return distance;
};

int closestPossibleNode(struct Node node, struct Node array[], int capacity) {
	int n = node.id;
	float dist_i;
	float dist_min = pow(10,5);
	int n_i;
	int demand_i;
	int node_min = 0;
	int i = 0;
	for (int i = 0; i < n; i++) {
		n_i = array[i].id;
		demand_i = array[i].demand;
		if (n_i != n && demand_i < capacity) {
			dist_i = d(node, array[i]);
			if (dist_i < dist_min) {
				dist_min = dist_i;
				node_min = array[i].id;
			}
		}
	}
	return node_min;
};

int totalDemand(struct Node array[]) {
	int d = 0;
	for (int i = 0; i < n; i++) {
		d += array[i].demand;
	}
};

void initialSolution() {
	struct Node *routes[n];
	int total_demand = totalDemand(nodes);
	int c = 0;
	while (c < total_demand) { 
		struct Node node_i = nodes[0];
		int capacity_i = capacity;
		struct Node route_i[n]; 
	}
};


float routeCost(struct Node array[]) {
	float cost = 0;
	int id;
	for (int i = 0; i < n - 1; i++) {
		id = array[i+1].id;
		if (id == 3141592) {
			break;
		}
		cost += d(array[i+1], array[i]);
	}
	return cost;
};


bool lastItem(struct Node array[]) {
	bool l;
	if (array[0].id == 3141592) {
		l = true;
	}
	else {
		l = false;
	}
	return l;
}

float totalCost(struct Node *array[]) {
	float cost = 0;
	bool l;
	for (int i = 0; i < n ; i++) {
		l = lastItem(*(array+i));
		if (l == true) {
			break;
		}
		else {
			cost += routeCost(*(array+i));
		}
	}
	return cost;
};

int closestPossibleRoute(struct Node node, struct Node *array[]) {
	float dist = pow(10,5);
	int closest_route = 0;
	float d_i;
	int demand = node.demand;
	for (int i = 0; i < n; i++) {
		if (routeCost(*(array+i)) + demand <= capacity) {
			for (int j = 0; j < n; j++) {
				d_i = d(node, *(array+i)[j]);
				if (d_i < dist) {
					dist = d_i;
					closest_route = i;
				}
			}
		}
	}
	return closest_route;
};




struct Node *l[3];
int main()
{
	struct Node a[3] = {{0,10,15,25},{1,11,18,29},{3141592,0,0,0}};
	struct Node b[3] = {{0,10,15,25},{3,10,15,29},{3141592,0,0,0}};
	struct Node c[1] = {{3141592,0,0,0}};
	l[0] = a;
	l[1] = b;
	l[2] = c;
	float cost = totalCost(l);
	cout << cost << endl;
}
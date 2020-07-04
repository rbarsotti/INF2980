#include <iostream>
#include <cmath>
using namespace std;

struct Node {
	int id;
	int x;
	int y;
	int demand;
};


float d(struct Node a, struct Node b) {
	float distance;
	distance = sqrt(pow((a.x - b.x),2) + pow((a.y - b.y),2));
	return distance;
};


int sumDemand(struct Node array[], int length) {
	int sum = 0;
	for (int i = 0 ; i < length ; i++) {
		sum += array[i].demand;
	};
	return sum;
};

int closestPossibleNode(struct Node node, struct Node *array[], int capacity, int length) {
	int n = node.id;
	float dist_i;
	float dist_min = pow(10,5);
	int n_i;
	int demand_i;
	int node_min = 0;
	for (int i = 0; i < length; i++) {
		n_i = (*array[i]).id;
		demand_i = (*array[i]).demand;
		if (n_i != n && demand_i < capacity) {
			dist_i = d(node, (*array[i]));
			if (dist_i < dist_min) {
				dist_min = dist_i;
				node_min = (*array[i]).id;
			}
		}
	}
	return node_min;
}


int routeDemand(struct Node *array[], int length) {
	int d = 0;
	for (int i = 0; i < length; i++) {
		d += (*array[i]).demand;
	}
}

struct Node **z[2];
struct Node *l[3];
int main()
{
	struct Node a = {0,10,15,25};
	struct Node b = {1,10,15,29};
	struct Node c = {2,1,6,15};
	l[0] = &a;
	l[1] = &b;
	l[2] = &c;
	z[0] = &*l;
	cout << (*(*z[0] +1)).id << endl;
}
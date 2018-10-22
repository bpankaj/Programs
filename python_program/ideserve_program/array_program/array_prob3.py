"""Given a cost matrix having a cost at each cell. Find the minimum cost it will take to reach
cell (m, n) from top left corner cell (0, 0) if the only allowed directions to move from a cell
are right, down and diagonally down.
"""

def minimum_cost_path_dp(array_list, m, n):
	import pdb;pdb.set_trace()
	min_cost_path = [[0 for m1 in range(n)] for n1 in range(m)]
	min_cost_path[0][0] = array_list[0][0]

	for i in range(1, m):
		min_cost_path[i][0] = min_cost_path[i-1][0] + array_list[i][0]
	for j in range(1, n):
		min_cost_path[0][j] = min_cost_path[0][j-1] + array_list[0][j]
	for i in range(1, m):
		for j in range(1, n):
			min_cost_path[i][j] = array_list[i][j] + min(min_cost_path[i-1][j-1],
				min_cost_path[i-1][j], min_cost_path[i][j-1])
	return min_cost_path[m-1][n-1]


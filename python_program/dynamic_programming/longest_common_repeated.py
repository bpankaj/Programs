def longest_common_repeated(string1):
	n = len(string1)
	dp = [[0 for i in range(n+1)] for j in range(n+1)]
	for i in range(1, n+1):
		for j in range(1, n+1):
			if string1[i-1] == string1[j-1] and i != j:
				dp[i][j] = dp[i-1][j-1] + 1
			else:
				dp[i][j] = max(dp[i][j-1], dp[i-1][j])
	return dp[n][n]

# Sub set sum problem
# Input:  A = { 3, 2, 7, 1}, S = 6
# Out put: True, subset is (3, 2, 1}
# Recursive call


def subset_sum_rec(array, num):
    result = []
    def find(arr, num, path=()):
        if not arr:
            return
        if arr[0] == num:
            result.append(path + (arr[0],))
        else:
            find(arr[1:], num - arr[0], path + (arr[0],))
            find(arr[1:], num, path)
    find(array, num)
    return result


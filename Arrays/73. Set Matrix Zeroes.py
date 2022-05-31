class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        """
        Do not return anything, modify matrix in-place instead.
        """
        x = len(matrix)
        y = len(matrix[0])
        z = []

        for i in range(x):
            for j in range(y):
                if matrix[i][j] == 0:
                    z.append([i, j])

        for k in z:
            for l in range(y):
                matrix[k[0]][l] = 0

        for k in z:
            for l in range(x):
                matrix[l][k[1]] = 0

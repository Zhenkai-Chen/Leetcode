class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length - 1):
            j = i + 1
            while j != length:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                j += 1
        for i in range(length):
            for j in range(length // 2):
                matrix[i][j], matrix[i][length - 1 - j] = matrix[i][length - 1 - j], matrix[i][j]

# 很简单，记住为0的元素的下标就行了，我这里用元组保存它们
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_dic = dict()
        zero_num = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_dic[zero_num] = (i, j)
                    zero_num += 1

        print(zero_dic, end="\n")

        for item in zero_dic:
            print(zero_dic[item][0])
            for i in range(len(matrix[0])):
                matrix[zero_dic[item][0]][i] = 0
            for j in range(len(matrix)):
                matrix[j][zero_dic[item][1]] = 0

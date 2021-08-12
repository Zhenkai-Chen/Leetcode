#   解法1-暴力解法
#   双循环
class Solution:
  def isUnique(self, astr: str) -> bool:
    flag = 0

    for i in range(len(astr)):
      for j in range(i + 1, len(astr)):
        if astr[i] == astr[j]:
          flag = 1
          break

    if flag == 1:
      return  False
    else:
      return True

#   解法2-散列表
#   用一个字典统计字符串里每个字符出现的次数
class Solution:
  def isUnique(self, astr: str) -> bool:
    count = dict()

    for char in astr:
      count[char] = astr.count(char, 0)

    flag = 0
    for value in count.values():
      if value > 1:
        flag = 1
        break

    if flag:
      return False
    else:
      return True

#   解法3-集合
#   主要运用Python的set()函数
class Solution:
  def isUnique(self, astr: str) -> bool:
    strs = list(astr)
    set_strs = set(strs)

    if len(strs) == len(set_strs):
      return True
    else:
      return False

#   最佳解法
#   位运算
#   把字符串中每个字符转化为一个二进制数，转化方法为1向左N位的位运算，N为这个字符和字符‘a’的距离；
#
# 例如 Na = 0,Nb=1,Nc = 2…a = 1<<0 = 1 ,b = 1<<1 = 10, c = 1<<2 = 100…；
#
# 所以，每个字符串对应位置为1；
#
# 这种情况下，如果当前字符如果曾经出现过，也就是其中某一位对应位数的值为1，就意味着曾经出现，返回False；
#
# 否则，如果没有出现过，那么通过|或运算，把这一位的值改写为1；
#
# 例如 ‘abca’ ： a= 1,b=10,c=100,前三次结果mark为111，最后一次111与001有相同符合条件，返回False
class Solution:
  def isUnique(self, astr: str) -> bool:
    mark = 0
    for char in astr:
      move_bit = ord(char) - ord('a')
      if (mark & (1 << move_bit)) != 0:
        return False
      else:
        mark |= (1 << move_bit)
    return True

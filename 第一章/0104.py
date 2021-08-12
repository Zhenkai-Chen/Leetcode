# 一个回文串里字符出现的次数为奇数的字符只能有一个
class Solution:
  def canPermutePalindrome(self, s: str) -> bool:
    count = dict()
    num = 0

    for char in s:
      count[char] = s.count(char, 0)
    for value in count.values():
      if value%2 != 0:
        num += 1
      if num > 1:
        return False

    return True

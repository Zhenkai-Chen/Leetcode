#   首先判断这两个字符串长度是否一致，然后判断这两个字符串是否含有不相同的字符，最后用字典统计每个字符出现的次数进行比较即可
class Solution:
  def CheckPermutation(self, s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
      return False
    else:
      set_s1 = set(s1)
      set_s2 = set(s2)

      if(set_s1 - set_s2):
        return False
      else:
        count1 = dict()
        count2 = dict()
        flag = 0

        for char in s1:
          count1[char] = s1.count(char, 0)
        for char in s2:
          count2[char] = s2.count(char, 0)
        for key in count1:
          if count1[key] != count2[key]:
            flag = 1
            break

        if flag:
          return False
        else:
          return True

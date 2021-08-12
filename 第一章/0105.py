#   若长度差如果大于2，则至少需要两次改动才可一致
#   将顺序换为first短，second长
#   当发现不一致时，只有两种情况满足修改一次
#   second多一个，所以判断是否first[i:] == second[i + 1:]
#   second当前元素不一致，后面都相同，所以判断是否first[i+1:] == second[i+1:]
class Solution:
  def oneEditAway(self, first: str, second: str) -> bool:
    if abs(len(first) - len(second)) > 1:    # 长度差大于2
      return False
    if len(first) > len(second):  # 保证first比second短
      first, second = second, first
    for i in range(len(first)):	  # 遍历短的字符串
      if first[i] == second[i]:
        continue  # 继续对比两字符串相同下标的字符
      return first[i:] == second[i + 1:] or first[i + 1:] == second[i + 1:]    # 到这里下标为i之前的字符都相等，那么就比对i后面的字符即可，两种情况
    return True

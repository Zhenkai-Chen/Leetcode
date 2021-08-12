#   直接截取字符串用replace函数
class Solution:
  def replaceSpaces(self, S: str, length: int) -> str:
    return S[:length].replace(" ", "%20")

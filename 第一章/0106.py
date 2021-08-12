class Solution(object):
    def compressString(self, S):
        n = len(S)
        if n <= 1:  # 如果字符串长度为1直接返回输入字符串
            return S
        S += "$"    # 在末尾添加一个字符利于边界处理
        now, cnt, ret = S[0], 1, ""    # ow:现在进行判断的字符，cnt:该字符出现的次数，ret为要输出的字符串
        for i in range(1, n + 1):   # 从下标为1的字符开始遍历字符串
            if S[i] != now:	    # 下一个字符与现在要判断的字符不相同
                ret += now + str(cnt)    # 输出字符串连接上现在进行判断的字符及出现的次数
                if len(ret) >= n:   # 判断输出字符串的长度是否大于等于输入字符串的长度
                    return S[:n]    # 若大于等于，直接返回输入字符串因为末尾加了个$
                now, cnt = S[i],1   # 否则从下一个字符进行判断
            else:   # 下一个字符与现在要判断的字符相同
                cnt += 1    # 出现次数加1
        return ret

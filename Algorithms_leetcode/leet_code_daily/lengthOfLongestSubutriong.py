#无重复最长子串
#找出给定字符串中的不含有重复字符的最长子串的长度
#返回长度以及最长子串
class Solution:
    def lengthOflongestSubstring(self,s):
        if not s:return 0
        left = 0    #用来计算
        lookup = set()      #使用集合来存放子串
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            #判断s[i]是否在lookup中，如果存在则把重复元素前的所有元素移除（包括重复的元素）
            while s[i] in lookup:
                lookup.remove(s[left])
                #left表示滑窗的左边界，当出现重复元素时，移动左边界
                left +=1    #用来表示要移除元素的下标，因为依次添加，故需要依次移除
                cur_len -=1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len

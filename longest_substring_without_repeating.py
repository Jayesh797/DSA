#2 pointer wih sliding window
def lengthOfLongestSubstring(self, s):
        left=0
        right=0
        hashi={}
        leni=0
        max_len=0
        # print(hashi)
        while(right<len(s)):
            if(s[right] in hashi):
                if(hashi[s[right]]>=left):
                    left=hashi[s[right]]+1
            leni=right-left+1
            max_len=max(max_len,leni)
            hashi[s[right]]=right
            right+=1
        return max_len
#2 pointer wih sliding window
def longestOnes(self, nums, k):
        left=0
        right=0
        max_len=0
        zeroes=0
        while(right<len(nums)):
            if(nums[right]==0):
                zeroes+=1
            while(zeroes>k):
                if(nums[left]==0):
                    zeroes-=1
                left+=1
            if(zeroes<=k):
                max_len=max(max_len,right-left+1)
            right+=1
        return max_len
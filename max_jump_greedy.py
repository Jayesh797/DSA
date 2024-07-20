##greedy algorithm
def canJump(self, nums):
        if 0 not in nums:
            return True
        max_index=0
        for i in range(0,len(nums)):
            if(i>max_index):
                return False
            max_index=max(max_index,i+nums[i])
        return True
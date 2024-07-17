def numberOfSubarrays(self, nums, k):
        def atMost(k):
            if(k<0):
                return 0
            left=0
            cnt=0
            num_odd=0
            for right in range(len(nums)):
                if nums[right] % 2 != 0:
                    num_odd += 1
                while(num_odd>k):
                    if(nums[left]%2!=0):
                        num_odd-=1
                    left+=1
                cnt+=right-left
            return cnt
        return atMost(k)-atMost(k-1)
def subarraysWithKDistinct(self, nums, k):
        def atMost(k):
            left=0
            right=0
            cnt=0
            hashi={}
            # z=0
            while(right<len(nums)):
                if nums[right] in hashi:
                    hashi[nums[right]] += 1
                else:
                    hashi[nums[right]] = 1
                while(len(hashi)>k):
                    hashi[nums[left]]-=1
                    if hashi[nums[left]] == 0:
                        del hashi[nums[left]]
                    left+=1
                cnt+=right-left+1
                right+=1
            return cnt
        return atMost(k)-atMost(k-1)
def maxScore(self, cardPoints, k):
        sum_total=sum(cardPoints[:k])
        max_sum=sum_total
        n=len(cardPoints)
        for i in range(1,k+1):
            sum_total+=cardPoints[n-i]-cardPoints[k-i]
            max_sum=max(sum_total,max_sum)
        return max_sum
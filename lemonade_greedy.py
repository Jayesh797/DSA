class Solution(object):
    def lemonadeChange(self, bills):
        five=0
        ten=0
        for i in bills:
            if(i==5):
                five+=1
            elif(i==10):
                if(five):
                    ten+=1
                    five-=1
                else:
                    return False
            else:
                if(ten and five):
                    ten-=1
                    five-=1
                elif(five>=3):
                    five-=3
                else:
                    print('loop0 3')
                    return False
        return True
        
        
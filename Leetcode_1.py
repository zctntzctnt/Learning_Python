import time
start=time.time()
'''
class SoluTion():
    def two_sum(self,nums,target):
        
        
      
        for i in range(len(nums)):
            if (target-nums[i]) in nums:
                if i==nums.index(target-nums[i]):
                    i+=1
                else:
                    return sorted([i,nums.index(target-nums[i])])                        
            else:
                i+=1

        

'''
class SoluTion():
    def two_sum(self,nums,target):
        
        
        for j in range(len(nums)):
            for i in range(j):
                if nums[i]+nums[j]==target:
                    return[i,j]

      
solution=SoluTion()
answer=solution.two_sum(list(range(2,1000000)),6)
print(answer)

end=time.time()
print(end-start)
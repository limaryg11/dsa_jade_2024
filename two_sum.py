#time taken to complete = 3 minutes

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #instantiate hash table mapping val --> index
        seen = {}

        #iterate through input arr:
        for i in range(len(nums)):
            #calculate complement val:
            complement = target - nums[i]
            #check if complement seen in hash table:
            if complement in seen:
                #return indices if complement seen already:
                return seen[complement], i
            #otherwise add curr val and index to hash table:
            else:
                seen[nums[i]] = i



# O(n) time 
# O(n) space

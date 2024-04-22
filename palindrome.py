#Time taken to complete = 5 minutes

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_string = str(x) #convert int to str

        #instantiate two pointers
        l = 0 
        r = len(x_string) - 1

        #while pointers dont overlap
        while l < r:
            #check if right and left pointers dont equal eachother
            if x_string[l] != x_string[r]:
                return False
              
            #otherwise increment left and decrement right
            l += 1
            r -= 1
          
        #if we exit while loop and it doesn't return False, then it is palindrome
        return True

#O(n) time (n = number of digits in x)
#O(n) space for converting x to str (n = number of digits in x)

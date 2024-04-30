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

# Optimized Solutions below
# ---------------------------------------------------------------

#this first solution reverses entire number and compares it to input integer
class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0: # edge case of negative number -- cannot be palindrome
            return False 

        reverse = 0 # this is what we will build our reverse number off of

        number = x #number variable is placeholder to manipulate input number without modifying original val

        while number > 0:
            last_digit = number % 10 # this will represent the ones column of number

            reverse = (reverse * 10) + last_digit #append last_digit to reverse

            number = number // 10 #remove the last digit from the number

        #check if orignal input is equal to our reversed number
        return x == reverse

#O(logn) (base10 for int) time complexity, O(1) space complexity

# ------------------------------------------------

# This solution reverses half and compares it to first half of number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if input int is negative it is not a palindrome
        # OR if last digit is 0 and the input int is not 0, it is not a palindrome
        ## because numbers don't start with 0
        if x < 0 or (x % 10 == 0 and x != 0): 
            return False

        reverse = 0

        number = x

        # this algo = revert half of input integer
        # bc reverse of last half of number should be same
        # as first half of the number if it is a palindrome
        while number > reverse:
            last_digit = number % 10 # get last digit of input num
            reverse = (reverse * 10) + last_digit   #build reverse num by continually adding last digit to appropriate place
            number = number // 10 # remove last digit from num to keep checking each place


        # when length is odd, we can get rid of middle digit by
        # reverse // 10 (middle number does not matter for palindrome)
        # so we check if number is equal to reverse or remove the last digit bc
        # this would be the middle digit if it is odd
        return number == reverse or number == reverse // 10

#O(logn) (base10 for int) time complexity, O(1) space complexity

# this one could be better for larger inputs because we are only going through the last half of int x and comparing it to what's left of number 

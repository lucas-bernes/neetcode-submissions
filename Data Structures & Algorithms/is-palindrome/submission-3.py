class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = [x.lower() for x in s if x.isalnum()]
        print(r)
        
        for index in range(0,len(r)):
            if r[index].lower() != r[-(index+1)].lower(): 
                return False
        
        return True


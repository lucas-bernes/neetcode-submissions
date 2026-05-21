class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        string_count = {}
        for string in arr:
            string_count[string] = string_count.get(string,0) + 1
        
        count = 0
        output = []
        for string,value in string_count.items():
            if count == k: break
            if value == 1:
                output.append(string)
                count += 1
        
        if len(output) < k: return ""
        else: return output[k-1]
            

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for operation in logs:
            if operation != "./":
                if operation == "../":
                    depth = max(0, depth-1)
                else: depth += 1
        
        return depth
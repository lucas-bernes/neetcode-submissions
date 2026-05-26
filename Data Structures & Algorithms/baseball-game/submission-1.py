class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for index in range(len(operations)):
            op = operations[index]
            
            if op == "C":
                record.pop(-1)
                
            
            elif op == "+":
                record.append(int(record[-1]+record[-2]))
                

            elif op == "D":
                record.append(int(record[-1] * 2))
                
            
            else:
                record.append(int(op))
                

        return sum(record)

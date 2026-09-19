class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):
            if operations[i] == '+':
                # Add last two scores
                prev1 = record[-1]
                temp1 = record.pop()
                prev2 = record[-1]
                record.append(temp1)
                record.append(prev1+prev2)
            elif operations[i] == 'C':
                # Remove last score
                record.pop()
            elif operations[i] == 'D':
                # Add double previous score
                record.append(int(record[len(record)-1]*2))
            else:
                # Add to the record
                record.append(int(operations[i]))
        cnt = 0
        for i in record:
            cnt += i
        return cnt
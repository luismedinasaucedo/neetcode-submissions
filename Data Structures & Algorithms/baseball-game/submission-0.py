class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []
        for i in range(len(operations)):
            print(i)
            if operations[i] == '+':
                points.append(points[-1]+points[-2])
            elif operations[i] == 'D':
                points.append(int(points[-1])*2)
            elif operations[i] == 'C':
                points.pop()
            else:
                points.append(int(operations[i]))
            print(points)

        return sum(points)

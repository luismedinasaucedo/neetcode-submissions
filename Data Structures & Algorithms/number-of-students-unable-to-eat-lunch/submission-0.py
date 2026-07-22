class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        es = len(students)
        con = 0

        while con != es:
            if  students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                es -=1
                con = 0

            else:
                students.append(students.pop(0))
                con += 1

        return con

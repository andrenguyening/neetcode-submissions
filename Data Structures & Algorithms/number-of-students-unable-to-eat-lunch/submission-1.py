from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_deque = deque(students)
        sandwich_deque = deque(sandwiches)
        rejections = 0
        
        while student_deque and rejections < len(student_deque):
            if student_deque[0] == sandwich_deque[0]:
                student_deque.popleft()
                sandwich_deque.popleft()
                rejections = 0
            else:
                student_deque.append(student_deque.popleft())
                rejections += 1
        return len(student_deque)
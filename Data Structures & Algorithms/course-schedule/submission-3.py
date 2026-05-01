class ListNode:
    def __init__(self):
        self.val = None
        self.prerecs = set()

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {} # Hashmap of classes to nodes

        # Put each class id and corresponding node to a hashmap while linking nodes
        for prerec in prerequisites:
            if courses.get(prerec[0], -1) == -1:
                courses[prerec[0]] = ListNode()
                courses[prerec[0]].val = prerec[0]
            if courses.get(prerec[1], -1) == -1:
                courses[prerec[1]] = ListNode()
                courses[prerec[1]].val = prerec[1]
            courses[prerec[0]].prerecs.add(courses[prerec[1]])

        # Use BFS to check prerecs for each class, if class has prerec with class as prerec,
        # return false
        seen = set()
        for ID, node in courses.items():
            queue = deque(node.prerecs)
            seen.add(ID)
            while queue:
                node = queue.popleft()
                if node.val == ID:
                    return False
                if node.val in seen:
                    continue
                seen.add(node.val)
                for prerec in node.prerecs:
                    queue.append(prerec)
               
            seen.clear()
        return True





        
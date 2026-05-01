class ListNode:
    def __init__(self):
        self.val = None
        self.prerecs = set()
        self.dependents = set()

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
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
            courses[prerec[1]].dependents.add(courses[prerec[0]])

        queue = deque()
        for ID, node in courses.items():
            if not node.prerecs:
                queue.append(node)

        finished = 0
        while queue:
            current = queue.popleft()
            for dp in current.dependents:
                dp.prerecs.remove(current)
                if not dp.prerecs:
                    queue.append(dp)
            finished += 1

        return finished == len(courses)





        
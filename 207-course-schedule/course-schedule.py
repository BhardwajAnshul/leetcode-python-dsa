from collections import defaultdict
import copy
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        for (course, req) in prerequisites:
            courses[course].append(req)

        visited = []
        rec_stack = []
        def dfs(node):
            visited.append(node)
            rec_stack.append(node)

            for nei in courses[node]:
                if nei not in visited:
                    if dfs(nei):
                        return True
                elif nei in rec_stack:
                    return True

            rec_stack.remove(node)
            return False

        for node in range(numCourses):
            if node not in visited:
                if dfs(node):
                    return False

        return True

        
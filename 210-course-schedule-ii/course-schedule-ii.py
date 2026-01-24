import copy
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1

        q = deque()
        order = []
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                order.append(i)


        # order= copy.deepcopy(indegree)
        taken = 0
        while q:
            course = q.popleft()
            taken += 1
            for nxt in adj[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    order.append(nxt)
                    q.append(nxt)

        if taken == numCourses:
            return order
        else:
            return []
        
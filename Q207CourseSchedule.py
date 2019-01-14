class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if len(prerequisites) == 0:
            return True
        course2pres = dict()
        for course in range(numCourses):
            course2pres[course] = set()
        for pair in prerequisites:
            last, pre = pair[0], pair[1]
            course2pres[last].add(pre)
        while len(course2pres):
            deleted = []
            
            for course in course2pres:
                if len(course2pres[course]) == 0:
                    deleted.append(course)
                    for pres in course2pres.values():
                        if course in pres:
                            pres.remove(course)
                        
            for course in deleted:
                course2pres.pop(course)
            
            if len(deleted) == 0:
                break
        
        if len(course2pres) > 0:
            return False
        else:
            return True

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_to_prerequisites = defaultdict(list)
        for p in prerequisites:
            course_to_prerequisites[p[0]].append(p[1])
        todo = set(course_to_prerequisites.keys())
        while todo:
            done = set()
            for course in todo:
                if all(prereq not in todo for prereq in course_to_prerequisites[course]):
                    done.add(course)
            if not done:
                return False
            todo -= done
        return True
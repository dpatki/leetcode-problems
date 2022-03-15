#submitted 12/03/2022

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {}
        for i in range(numCourses):
            courses[i] = [0, [], []]
        for req in prerequisites:
            courses[req[0]][1].append(req[1])
            courses[req[0]][0] += 1
            courses[req[1]][2].append(req[0])
        
        #print(courses)
        seen = []
        def traverse(course):
            #print(course)
            if courses[course][0] == 0:
                if course in seen:
                    return
                seen.append(course)
                for elem in courses[course][2]:
                    courses[elem][0] -= 1
                    traverse(elem)
        
        for i in range(numCourses):
            #print(i)
            traverse(i)
        
        #print(courses)
        found = True
        for i in range(numCourses):
            if courses[i][0] != 0:
                found = False
        
        return seen if found else []
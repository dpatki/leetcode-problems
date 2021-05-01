#submitted 26/03/2021

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = []
        keys = [0]
        while (visited != keys):
            for elem in keys:
                if elem not in visited:
                    newkeys = self.traverse(elem, rooms)
                    for key in newkeys:
                        if key not in keys:
                            keys.append(key)
                    visited.append(elem)

        total = len(rooms) * (len(rooms) - 1) / 2
        if sum(keys) != total:
            return False
        return True
        
    def traverse(self, val, rooms):
        return rooms[val]
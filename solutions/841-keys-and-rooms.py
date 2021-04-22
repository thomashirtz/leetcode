class Solution:
    def canVisitAllRooms(self, rooms):
        room_visited = [False]*len(rooms)

        def visit_room(key=0):
            if not room_visited[key]:
                room_visited[key] = True
                for key in rooms[key]:
                    visit_room(key)
                    
        visit_room()
        return all(room_visited)

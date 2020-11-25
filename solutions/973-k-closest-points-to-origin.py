class Solution:
    def kClosest(self, points, K):
        dictionary = {}
        for point in points:
            dictionary[tuple(point)]=point[0]**2 + point[1]**2
        return sorted(dictionary, key=dictionary.get)[:K]
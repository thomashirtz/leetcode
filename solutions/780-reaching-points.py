class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        if tx == 0 or ty == 0:
            return (sx, sy) == (tx, ty)

        while not (sx == tx and sy == ty):

            if tx < sx or ty < sy:
                return False
            elif tx == ty:
                return (0, ty) == (sx, sy) or (tx, 0) == (sx, sy)
            elif ty > tx:
                if tx == sx:
                    return (ty - sy) % tx == 0
                ty = ty - tx
            else:
                if ty == sy:
                    return (tx - sx) % ty == 0
                tx = tx - ty
        return True

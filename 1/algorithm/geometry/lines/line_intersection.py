'''
How is Orientation useful here?
Two segments (p1,q1) and (p2,q2) intersect if and only if one of the following two conditions is verified

1. General Case:
– (p1, q1, p2) and (p1, q1, q2) have different orientations and
– (p2, q2, p1) and (p2, q2, q1) have different orientations.


2. Special Case
– (p1, q1, p2), (p1, q1, q2), (p2, q2, p1), and (p2, q2, q1) are all collinear and
– the x-projections of (p1, q1) and (p2, q2) intersect
– the y-projections of (p1, q1) and (p2, q2) intersect
'''


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


def onSegment(p,q,r):
    if (( q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
     (q.y <= max(p.y, r.y)) and (q.y))
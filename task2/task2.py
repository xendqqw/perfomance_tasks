class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


def point_position(center, radius, point):
    distance = center.dist(point)
    if distance == radius:
        return "0"
    elif distance < radius:
        return "1"
    else:
        return "2"


args = input().split()
circle_file = args[0]
points_file = args[1]

with open(circle_file, 'r') as f:
    center_coords = f.readline().strip().split()
    radius = float(f.readline().strip())
    center = Point(center_coords[0], center_coords[1])

with open(points_file, 'r') as f:
    for line in f:
        point_coords = line.strip().split()
        point = Point(point_coords[0], point_coords[1])
        print(point_position(center, radius, point))

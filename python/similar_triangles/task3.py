import math

class Vector:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def to(self, other):
        return Vector(other.x - self.x, other.y - self.y)

    def len(self):
        return math.sqrt(self.dot(self))

    def __str__(self):
        return f"(x={self.x}, y={self.y})"


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        self.angles = (
                self.__angles(p1, p2, p3),
                self.__angles(p2, p1, p3),
                self.__angles(p3, p1, p2)
        )

    @classmethod
    def from_str(cls, string):
        parts = string.split()
        return Triangle(
                Vector(float(parts[0]), float(parts[1])),
                Vector(float(parts[2]), float(parts[3])),
                Vector(float(parts[4]), float(parts[5]))
        )

    def __angles(self, p1, p2, p3):
        v1 = p1.to(p2)
        v2 = p1.to(p3)
        return math.acos(v1.dot(v2) / v1.len() / v2.len()) * 180 / 3.1415926

    def is_similar_to(self, other):
        count = 0
        for a in self.angles:
            for b in other.angles:
                if abs(a-b) < 1E-5:
                    count += 1

                    if count >= 2:
                        return True

        return False

    def __str__(self):
        return f'{self.p1.x} {self.p1.y} {self.p2.x} {self.p2.y} {self.p3.x} {self.p3.y}'


def read_triangles():
    triangles = []
    with open('in3.txt') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            triangles.append(Triangle.from_str(line.strip()))
    return triangles


def find_similar(trig_list):
    partitions = []
    for trig in trig_list:
        found = False
        for p in partitions:
            if trig.is_similar_to(p[0]):
                p.append(trig)
                found = True
        if not found:
            partitions.append([trig])
    return partitions


def write_results(results):
    with open('out3.txt', 'w') as file:
        for r in results:
            file.write('\n'.join((str(x) for x in r)))
            file.write('\n\n')


triangles = read_triangles()
results = find_similar(triangles)
write_results(results)

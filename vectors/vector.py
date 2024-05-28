import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        return f"This is a 3D vector with x={self.x}, y={self.y}, z={self.z}"
    
    def calc_magnitude(self):
        magnitude = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        return magnitude
    
    def calc_dot_product(self, other):
        dot_product = self.x * other.x, self.y * other.y, self.z * other.z
        return dot_product
    
    def calc_cross_product(self, other):
        cross_i = (self.y * other.z) - (self.z * other.y)
        cross_j = (self.z * other.x) - (self.x * other.z)
        cross_k = (self.x * other.y) - (self.y * other.x)
        
        return Vector3D(cross_i, cross_j, cross_k) 
        
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)
    
if __name__ == "__main__":
    v1 = Vector3D(1, 2, 3)
    print(v1)
    print(f"The magnitude of v1 is : {v1.calc_magnitude()}")
    
    v2 = Vector3D(4, 5, 6)
    v3 = v1 + v2
    print(v3)
    
    v4 = v2 - v1
    print(v4)
    
    v5 = v2 * 5
    print(v5)
    
    dot_product = v1.calc_dot_product(v2)
    print(dot_product)
    
    cross_product = v1.calc_cross_product(v2)
    print(cross_product)
    
    def calc_distance(p1, p2):
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        
        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
        return distance
    
    p1 = (1, 2, 3)
    p2 = (4, 5 , 6)
    
    print(f"The distance between p1 and p2 is {calc_distance(p1, p2)}")
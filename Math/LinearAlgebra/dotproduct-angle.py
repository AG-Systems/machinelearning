import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
        
    def times_scalar(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)
    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return math.sqrt(sum(coordinates_squared))
        
    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1.0/magnitude)
        except ZeroDivisionError:
            raise Exception('Cannot compute')

    def dot_product(self,v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])
    
    def angle_with(self,v, in_degrees=False):
        u1 = self.normalized()
        u2 = v.normalized()
        angle_in_radians = math.acos(u1.dot_product(u2))
        if in_degrees:
            degrees_per_radian = 180. / math.pi
            return angle_in_radians * degrees_per_radian
        else:
            return angle_in_radians


v = Vector([7.887, 4.138])
w = Vector([-8.802, 6.776])
print v.dot_product(w)

v = Vector([-5.955, -4.904, -1.874])
w = Vector([-4.496, -8.755, 7.103])
print v.dot_product(w)

v = Vector([3.183, -7.627])
w = Vector([-2.668, 5.319])
print v.angle_with(w)

v = Vector([7.35, 0.221, 5.188])
w = Vector([2.751, 8.259, 3.985])
print v.angle_with(w, in_degrees=True)

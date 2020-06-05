#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.
class Circle:

    def __init__(self, radius, pi=3.14):
        self.radius = radius
        self.pi = pi

    def area(self):
        return (self.pi * self.radius**2)

    def perimeter(self):
        return (2 * self.pi * self.radius)

r = float(input('Enter the radius:'))
c = Circle(r)
print('Area of circle is {}'.format(c.area()))
print('Perimeter of a circle is {}'.format(c.perimeter()))
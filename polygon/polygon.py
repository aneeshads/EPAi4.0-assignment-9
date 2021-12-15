# Objective 1: Create a Polygon Class where initializer takes in the following
# 1. number of edges/vertices
# 2. circumradius
# That can provide these properties:
# 1. edges
# 2. vertices
# 3. interior angle
# 4. edge length
# 5. apothem
# 6. area
# 7. perimeter
# That has these functionalities:
# 1. a proper __repr__ function
# 2. implements equality (==) based on # vertices and circumradius (__eq__)
# 3. implements > based on number of vertices only (__gt__)

import math

new_line = "\n"

class Polygon:
    '''The class 'Polygon' accepts the number of vertices (greater than or equal to 3) and the circumradius \
    of a polygon as input arguments. The various functions within the class calculate the measures of \
    interior angle, edge length, apothem, area and perimeter for the polygon,to upto two places after decimal.'''

    def __init__(self, numberofvertices, circumradius):
        '''The initializer function defines that the class accepts two parameters - the number of vertices \
        of the polygon whose properties have to be calculated, and the circumradius of the same. Circumradius \
        is expressed as the radius of an imaginary circle that can be inscribed around the polygon.'''

        if (isinstance(numberofvertices, int)) == False:
            raise TypeError("Please enter an integer only")
        if (numberofvertices < 0):
            raise ValueError("The number of vertices should be a positive value")
        if (numberofvertices <= 2):
            raise ValueError("The number of vertices should be greater than or equal to three")
        if ((isinstance(circumradius, int) or isinstance(circumradius, float)) == False):
            raise TypeError("The value of circumradius should be an int or a float")

        self.numberofvertices = numberofvertices
        self.circumradius = circumradius
        self.interiorangle = round((numberofvertices - 2) * (180/numberofvertices), 2)
        self.edgelength = round(2 * circumradius * math.sin(math.pi/numberofvertices), 2)
        self.apothem = round(circumradius * math.cos(math.pi/numberofvertices), 2)
        self.area = round(((1/2) * numberofvertices * self.edgelength * self.apothem), 2)
        self.perimeter = round((numberofvertices * self.edgelength), 2)


    def __repr__(self):
        '''The dunder method of representation function describes the messages that are displayed when the class Polygon \
        is called without an argument.'''

        return (f'For a polygon with the number of vertices {self.numberofvertices} and a circumradius of {self.circumradius}{new_line}, \
        The measure of interior angle is {self.interiorangle}{new_line}. \
        The measure of edge length is {self.edgelength}{new_line}. \
        The measure of apothem is {self.apothem}{new_line}. \
        The measure of area is {self.area}{new_line}. \
        The measure of perimeter is {self.perimeter}{new_line}')


    def __eq__(self, other):
        '''The dunder method of equality has been defined to compare and return with an affirmative when the dimensions - \
        number of vertices and circumradius - of two input polygons are equal.'''

        if (self.numberofvertices == other.numberofvertices) and (self.circumradius == other.circumradius):
            return True
        else:
            return False


    def __gt__(self, other):
        '''The dunder method of greater than has been defined to compare and return with an affirmative when the number of \
        vertices of one input polygon is greater than the other.'''

        if self.numberofvertices > other.numberofvertices:
            return True
        else:
            return False

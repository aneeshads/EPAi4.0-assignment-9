# Objective 2: Implement a Custom Polygon sequence type where initializer takes in:
# 1. number of vertices for largest polygon in the sequence
# 2. common circumradius for all polygons
# that can provide these properties:
# max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
# that has these functionalities:
# a. functions as a sequence type (__getitem__)
# b. supports the len() function (__len__)
# c. has a proper representation (__repr__)

from polygon.polygon import Polygon

class PolygonSequence:
    '''This class creates a sequence of polygons with varying number of vertices and the same circumradius.The least possible \
    number of vertices that a polygon can possess is three. Thus, the indexing of the polygon in the sequence will be initiated \
    in such a way that the 0th element corresponds to 3 and so on. The circumradius is assumed to be the same for all the polygons.'''

    def __init__(self, maxvertices, circumradius):
        '''The class is initialized in a way that it can accept the arguments of maximum vertices and circumradius.'''

        self._maxn = maxvertices
        self._r = circumradius


    def __len__(self):
        '''The dunder method of length returns the number of polygons that are present within the sequence.'''

        return self._maxn


    def __getitem__(self, s):
        '''The dunder method of getitem selects the highest possible index.'''

        if isinstance(s, int):
            # single item requested
            if s > (self._maxn - 1):
                raise IndexError
            if s < 0:
                s = self._maxn + s
            if (0 <= s) and (s < 3):
                return None
            return Polygon(s, self._r)
        else:
            # slice being requested
            print(f'requesting [{s.start}:{s.stop}:{s.step}]')
            idx = s.indices(self._maxn)
            rng = range(idx[0], idx[1], idx[2])
            return [Polygon(n, self._r) if n > 2 else None for n in rng]

    def __repr__(self):
        '''The dunder method of representation returns the polygon with the maxium number  of vertices and the common circumradius.'''

        return (f'This is a PolygonSequence class with polygons upto {self._maxn} vertices and {self._r} circumradius')


    def maximum_efficient_polygon(self):
        '''A polygon that has the highest area:perimeter ratio is denoted as the maximum efficiency polygon.\
        This function finds the polygon which has the maximum efficiency among all the others within the sequence.'''

        apr_list = []
        for idx in range(3, self._maxn):
            p = Polygon(idx, self._r)
            area_perimeter_ratio = p.area / p.perimeter
            apr_list.append(area_perimeter_ratio)
        return max(apr_list)

from fractions import Fraction
from graphutil import Graph
import attr
import music21

'''
Music is formed of relationships between sounds
Those relationships can be out-of-time, in which case they can be described as sets/modules/groups
or in-time in which case the relations are much more complex, for example horizontal (chords) or vertical
how to describe these?  A score assumes an x,y relationship, this is adequate for performance but hides any deeper relations. For example chords and melodies are more or less x-transpose invariant. Rhythms are more or less scale invariant.

    There are many more deep relations in music, some invariant (like those mentioned above) and some can be chosen by the composer as canons for guiding his composition
    
    
    This has been moved to a modifier function
        :param direction: slope of line in radians as Fraction(x,y) = xPI/y default is 1/2 (forward)
                      3/2  is retrograde, 0 is up chord (from center note), 1/2 is downchord,
                      all other angles will be arpeggios calculated according to the note duration
                      fraction and the center duration
'''

"""
#+- an undefined center tone
@attr.s
class Interval(object):
    interval = attr.ib(default=0)
"""

#A fraction of an undefined time span

class Duration():
    def __init__(self, multiple=None, unit='1/4'):
        self.multiple = multiple
        self.unit     = Fraction(unit)
        self.value    = self.multiple * self.unit
        self.original = unit

"""
@attr.s
class Sequence(object):
     
    :param object is a list of durations or intervals or motifs
    A modifier is a function f(t) which can change the values of a sequence
    t can be a single global change, or a per object change, in which case it
    will be applied for every duration tick during rendering
    a modifier can give an accent pattern to a sequence
     
    sequence = attr.ib(default=[])
    modifier = attr.ib(default=None)
"""

class Motif():

    counter = 0

    """
    :param intervals:sequence
    :param durations:sequence
    :param modifier:function
    """
    def __init__(self, name=None, intervals=[], durations=None, modifier=None):
        if not name:
            name = 'unique_name_' + str(Motif.counter)
            Motif.counter += 1
        self.name = name
        if not durations:
            durations = attr.ib(default=[Fraction(1,4) for x in intervals])
        self.intervals  = []
        self.durations  = durations
        self.modifier   = modifier
        self.offset     = 0

def retrograde(m):
    return Motif(m.name + '_retro', m.intervales.reverse(), m.durations.reverse())

class Orchestration(Graph):
    """
    :param Graph(V = [motif], E = (motif:duration -> motif:duration))
    :param modifier:function

    """
    def __init__(self, motifs):
        self.graph = Graph()
        for m in motif:
            self.graph.add_node(m.name, m)


def render(orchestration, center=60, tempo=120, modifier=None):
    """

    :param orchestration:
    :param center:
    :param tempo:
    :param modifier:

    :return: piece
    """



		
#the idea is that everything is abstract relationships until instantiate
#and then all functions are evaluated and sequences are given actual 
#pitchs and durations are give actual time stamps based

"""
We have a collection of ordered intervales which can be re-ordered with modulating functions
We have a collection of ordered durations which can be re-ordered with modulating functions
interval group + duration group = motif

A piece is an ordered set of motifs with modulating functions.  So a melody that modulates up a fifth each
time it is played would be a piece with a single motif and a modulating function that adds a fifth 
recursively to each of its objects

When a piece is played it needs to be instantiatedd with a center pitch and a center duration and direction, all other
pitches ad duratioons will be dependent on this
direction can be used to define chords or arpegios (how are durations releated to direction?)

???is there a way to abstract this futherr???
intervals could be defined as fractions?  or are they the basis?

It seems like motif and piece are arbitrary, maybe it should be just one recursive structure
How is simultaneoty dealt with? A conterpoint line is just two motifs played at 1/2 radians, but the 
relation between them is like a chord (0?)

Maybe vectors makes more sense, phi is the angle (radians) and the length indicates relative duration
all durations along the vector will be made to fit.  What about pitches?  Intervals can also be stretchd along vectors





"""
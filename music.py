from fractions import Fraction
import attr
import music21

'''
Music is formed of relationships between sounds
Those relationships can be out-of-time, in which case they can be described as sets/modules/groups
or in-time in which case the relations are much more complex, for example horizontal (chords) or vertical
how to describe these?  A score assumes an x,y relationship, this is adequate for performance but hides any deeper relations. For example chords and melodies are more or less x-transpose invariant. Rhythms are more or less scale invariant.

    There are many more deep relations in music, some invariant (like those mentioned above) and some can be chosen by the composer as canons for guiding his composition
    
'''


#+- an undefined center tone
@attr.s
class Interval(object):
    interval = attr.ib(default=0)

#A fraction of an undefined time span
@attr.s
class Duration(object):
    duration = attr.ib(default=Fraction(1))

#+- an undefined center volume
@attr.s
class Accent(object):
    accent = attr.ib(default=1)

@attr.s
class Sequence(object):
    sequence = attr.ib(default=[])

@attr.s
class Motif(object):
    intervals = attr.ib(default=[])
    durations = attr.ib(default=[Fraction(1,4) for x in intervals])
    accents   = attr.ib(default=[1 for x in durations])

def play(motif, center_pitch=60, center_duration=Fraction(1,2), center_accent=60, direction=Fraction(0)):
    """

    :param motif:
    :param center_duration:
    :param center_accent:
    :param direction: slope of line in radians as Fraction(x,y) = xPI/y default is 1/2 (forward)
                      3/2  is retrograde, 0 is up chord (from center note), 1/2 is downchord,
                      all other angles will be arpeggios calculated according to the note duration
                      fraction and the center duration
    :return:
    """
    pass
		
#the idea is that everything is abstract relationships until instantiate
#and then all functions are evaluated and sequences are given actual 
#pitchs and durations are give actual time stamps based
def SinOsc(divisions, )
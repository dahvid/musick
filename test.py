from music import *


m1 = Motif('m1', [1,2,3,5,7])
m2 = retrograde(m1)

"""
append 
start aligned
end aligned

duration aligned

m1 => m2  append or m1(end) | m2
m1 | m2   simultaneos or m1(0) => m2


m1:23 => m2  23 duration units into m1 start m2

m1:(23,7/8) => m2 #23 7/8 ths into m1 start m2
m1 => (3,1/4):m2   #at end of m1 start m2 3/4 into


overloaded version

m3 = m1(end) >> m2(begin)  #append
m3 = m1(begin) | m2(begin) #simul

m3 = m1 + end >> m2 #append
m3 = m1 | m2  #start simul

x >> y #y's start is relative to x
x | y  #y and x have the same beginning reference point

================================
#problem is + means two different things depending on operator
#and if it's on the right or left side of the operator
#m3 is a graph of m1,m2 with edges indicated offsets

m3 = m1 + d(3,'7/9') >> m2 #start m2  3 7/9ths into m1
edge from m1+21/9 to m2.begin

m3 = m1 + d(3,'7/9') | m2 #start m1  3 7/9ths into and m2 immediately
trunc left m1 + 21/9 and start simul with m2

m3 = m1 >> m2 + d(3,'7/9') #after m2 start m2 21/9 from beginni
edge from m1 end to m2 + 21/9

m3 = m1 | m2 + d(3,'7/0') #start m1 from beginning and m2 21/9 into
edge from m1 end to 21/9 into m2

edge from m2 to m1 21/9 from beginning

========================================
fewer operators, start with the connection points

m3 = (m1.offset(-(3,'7/9')) >> m2.begin 
#start m1 21/9 from the end along with m2


m3 = m1.begin(dur_offset = 2/9


"""

#maybe get rid of orchestrations and just have motifs?
#rc = Orchestration([m1, m2], a)






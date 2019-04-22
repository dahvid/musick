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


m3 = m1 + d(3,'7/9') >> m2 #start m2  3 7/9ths into m1
m3 = m1 + d(3,'7/9') | m2 #start m1  3 7/9ths into and m2 immediately

also
m2 = m1 + d(3,'7/9')
m2 = m1 - d(3,'7/9') 



"""

#maybe get rid of orchestrations and just have motifs?
orc = Orchestration([m1, m2], a)





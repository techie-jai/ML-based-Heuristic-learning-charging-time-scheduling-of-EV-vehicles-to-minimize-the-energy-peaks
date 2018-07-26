#Peak due to EV's and household demand
import numpy
import matplotlib.pyplot as plt
import random
time = [9,10,11,12,1,2,3,4,5,6,7,8,9]
p=[1100,1050,900,850,825,800,1200,987,1000]
 #demand of units from 9-11, 11-1....till 9pm
#Ct=[5, 4, 8, 3, 5, 4, 2, 5, 1, 0] #current state of charge from in kW 10 cars
#Edist = [70, 90, 78, 45, 52, 46 , 23, 100, 74, 90] # distance to be traveled by each of the 10cars in km
#wk= [.4, .9, 1, .1, .6, .5, .5, .7, .9, .3] #random whittle index alloted
Ct=[]
Edist=[]
wk=[]
for x in range (100):
    Ct.append(random.randint(0,10))
    Edist.append(random.randint(50,120))
    wk.append(random.randint(1,10))
#print "following are the randomly generated values"
#print "random current state of chargings"
#print Ct
#print "random distance to be travelled"
#print Edist
#print "random whittle index"
#print wk
q = .15 # charge consumption per 100 km ie 15kWh/100km and this divided by 10 for making it within 0-1
swk=[]
swk= numpy.argsort(wk)[::-1] #this is sorting all the 10 cars according to their whittle index in descending order and returning their list index
wid=[]
#print 'the ids with descending order of priority is \n ', swk
for i in range(0,5):
    wid.append(swk[i])
#print 'top 5 car to be charged have the follwing id $$$$$$$$$$$$$$$: \n', wid # this is trimming the first 5 top whittle indexes because we have 5 slots only
rsum=0
rq = [] # list initialised for calculating the requirement parameter
diff = [] # list initialised for calculating the actual required amount
for i in range(0, 100, 1):
    r = q*Edist[i]
    rq.append(r)
    d=rq[i]-Ct[i]  # d is difference of req charge - current state of charge
    diff.append(d)
    rsum=rsum+d
print "here is the total required energy////////////////", rsum	
#print '\n the total energy required by all cars is%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%: ' , rsum
#print '\n this is the total till next day requirement \n', rq, '\n '
#print 'this is the amount of KW car needs to be charged \n',  diff, '\n'
slotsum=[0,0,0,0,0,0,0,0,0,0]
#print 'the sum of kws in each slot due to EVs are ' ,slot sum
i=0
peak=0
#print "this is creating problem:::::q3rqfzf234324132", diff
for i in wid: # charging starts with the once having the highest whittle index
    #print '---------------the car currently being charged has ID : ', i, '-----------------------\n'
    j=0
    #if(diff[i]>0 and p[i]<p[i+1]):
    while(diff[i]>0):
        if(p[j]<p[j+1]):
         #   print '............................................'
          #  print j, ' is present time slot is \n'
           # print 'this car charges now completely with ID', i
            #print '............................................'
            peak=slotsum[j]+diff[i]
            slotsum[j]=peak
            break
        else:
            #print '............................................'
            #print j ,'is the present time slot \n',
            #print 'initial diff in kw ', diff[i]
            c=diff[i]/6
            #print ' the portion of charging to take place in kw in this slot is \n', c
            diff[i]=diff[i]-c #remaining charging to be done in the other slots
            #print 'charge left is \n', diff[i]
            #print '............................................'
            peak=slotsum[j]+c
            slotsum[j]=peak
            j=j+1
#for i in slotsum:
    #print '\n the sum of energy required in each of the slots are', i
#print ' now showing the plot'
#plt.bar([1,2,3,4,5,6,7,8,9,10], slotsum)
#plt.axis([0, 12, 1, 30])
#plt.show()
p=[1100+rsum,1050,900,850,825,800,1200,987,1000]
plt.bar([1,2,3,4,5,6,7,8,9],p)
plt.show()


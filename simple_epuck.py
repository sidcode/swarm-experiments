from ePuck import ePuck
import bluetooth

mac0 = '10:00:E8:C%:6B:00'

robot0 = ePuck(mac0)
print robot0 
# Second, connect to it
robot0.connect(1)


#msg0 =robot0.send_and_receive('z')
#print msg0


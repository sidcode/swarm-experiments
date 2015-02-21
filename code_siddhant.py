from ePuck import ePuck
import bluetooth
import time
import re
from multiprocessing import Process
from multiprocessing.connection import Client

count = 0
head0 = 0;
head1 = 0;
head2 = 0;
head3 = 0;

global_speed = 180
fs_speed = 0.6
command_list = []
# First, create an ePuck object.
mac0 = '10:00:E8:C5:61:6D'
mac1 = '10:00:E8:C5:6B:00'
mac2 = '10:00:E8:C5:64:89'
mac3 = '10:00:E8:C5:64:61'
robot0 = ePuck(mac0)
robot1 = ePuck(mac1)
robot2 = ePuck(mac2)
robot3 = ePuck(mac3)

print robot0 
# Second, connect to it
robot0.connect(1)
robot1.connect(1)
robot2.connect(1)
robot3.connect(1)

'''
msg0 =robot0.send_and_receive('z')
print msg0
msg1 =robot1.send_and_receive('z')
print msg1
msg2 =robot2.send_and_receive('z')
print msg2
msg3 =robot3.send_and_receive('z')
print msg3
'''

time.sleep(1)
msg0 =robot0.send_and_receive('R')
msg1 =robot1.send_and_receive('R')
msg2 =robot2.send_and_receive('R')
msg3 =robot3.send_and_receive('R')
print "ePuck0 says:" +msg0
print "ePuck1 says:" +msg1
print "ePuck2 says:" +msg2
print "ePuck3 says:" +msg3


#robot.enable("accelerometer")
#"A"         Accelerometer
#"B,#"       Body led 0=off 1=on 2=inverse
#"C"         Selector position
#"D,#,#"     Set motor speed left,right
#"E"         Get motor speed left,right
#"F,#"       Front led 0=off 1=on 2=inverse
#"G"         IR receiver
#"H"          Help
#"I"         Get camera parameter
#"J,#,#,#,#" Set camera parameter mode,width,heigth,zoom(1,4 or 8)
#"K"         Calibrate proximity sensors
#"L,#,#"     Led number,0=off 1=on 2=inverse
#"N"         Proximity
#"O"         Light sensors
#"P,#,#"     Set motor position left,right
#"Q"         Get motor position left,right
#"R"         Reset e-puck
#"S"         Stop e-puck and turn off leds
#"T,#"       Play sound 1-5 else stop sound
#"U"         Get microphone amplitude
#"V"         Version of SerCom

def file_read():
	fp = open('test6.txt','r')
	lines = fp.readlines()
	commands = []
	for line in lines:
		curr_line = line.strip().split()
		temp = [int(curr_line[0]), int(curr_line[1]), int(curr_line[2]), int(curr_line[3])]
		commands.append(temp)
	print commands
	return commands

def head_update(n_hood,head):

	if n_hood == 7 or n_hood == 0:
		head = head - 2
	elif n_hood == 4 or n_hood == 5:
		head = head + 2
	#elif n_hood == 6:
		#head = head + 4
	else:
		head = head
	head = head % 8
	
	
	return head



def robot0_nav():
	 #receive from file
	
	#count0 = count0 + 1
	 
	robot0.navigate(n_hood0)
	
	robot0.step()
	
	
def robot1_nav():
	#receive from file
	#n_hood1 = (n_hood1 + head1)%8
	#count1 = count1 + 1
	 
	robot1.navigate(n_hood1)
	
	robot1.step()
	
	

def robot2_nav():
	#receive from file
	#n_hood2 = (n_hood2 + head2)%8
	#count2 = count2 + 1
	 
	robot2.navigate(n_hood2)
	
	robot2.step()
	

	
def robot3_nav():
	#receive from file
	#n_hood3 = (n_hood3 + head3)%8
	#count3 = count3 + 1
	 
	robot3.navigate(n_hood3)
	
	robot3.step()
	

command_list = file_read()

while True:
	
	n_hood0 = command_list[count][0]
	n_hood1 = command_list[count][1]
	n_hood2 = command_list[count][2]
	n_hood3 = command_list[count][3]
	print "count:",count," n_hood0:",n_hood0," n_hood1:",n_hood1," n_hood2:",n_hood2," n_hood3:",n_hood3
	n_hood0 = (n_hood0 + head0)%8
	n_hood1 = (n_hood1 + head1)%8
	n_hood2 = (n_hood2 + head2)%8
	n_hood3 = (n_hood3 + head3)%8
	p1 = Process(target=robot0_nav)
	p2 = Process(target=robot1_nav)
	p3 = Process(target=robot2_nav)
	p4 = Process(target=robot3_nav)
	p1.start()
	p2.start()
	p3.start()
	p4.start()
	p1.join()
	p2.join()
	p3.join()
	p4.join()
	head0 = head_update(n_hood0,head0)
	head2 = head_update(n_hood2,head2)
	head1 = head_update(n_hood1,head1)
	head3 = head_update(n_hood3,head3)
	count = count + 1
    

	#p1.terminate()
	#print "P1 ter"
	#p2.terminate()
	#print "P2 ter"
	#p3.terminate()
	#print "P3 ter"
	#p4.terminate()
	#print "P4 ter"
    
    
    

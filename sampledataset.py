
'''
Program to sample data
'''
import os
import random
# random shuffle
mypath = '/home/shreya/testsample/Atelectasis/'
newpath = "/home/shreya/testclasses/Atelectasis/"
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
sampled_list = random.sample(onlyfiles,90)

# copy files
if not os.path.exists(newpath):
    os.makedirs(newpath)

for i in sampled_list:
    source = os.path.join(mypath, i)
    destination = os.path.join(newpath, i)
    os.rename(source, destination)


        
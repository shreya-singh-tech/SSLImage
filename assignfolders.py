'''
Code to assign data into folders
'''
import os
import pandas as pd

# path to image folder, get all filenames on this folder
# and store it in the onlyfiles list

mypath = "/home/shreya/test/"
datacsv = "/home/shreya/Data_Entry_2017_v2020.csv"
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
newpath = "/home/shreya/testsample/"
df1 = pd.read_csv(datacsv)
print(onlyfiles)
# split column into multiple columns by delimiter 
df3 = df1['Finding Labels'].str.split('|', expand=True)
df3.columns = ['Finding Labels{}'.format(x+1) for x in df3.columns]
df = pd.concat([df1, df3], axis=1)
print(df.head(5))
# your list of ids's
Atelectasis = df[df['Finding Labels1'] == 'Atelectasis']['Image Index'].to_list()
# create two seperate lists from onlyfiles list based on lis1 and lis2
lis1files = [i for i in onlyfiles for j in Atelectasis if j in i]
print(lis1files)
# create two sub folders in newpath folder
subfolder1 = os.path.join(newpath, "Atelectasis")
# check if they already exits to prevent error
if not os.path.exists(subfolder1):
    os.makedirs(subfolder1)
# move files to their respective sub folders
for i in lis1files:
    source = os.path.join(mypath, i)
    destination = os.path.join(subfolder1, i)
    os.rename(source, destination)    

onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
Cardiomegaly = df[df['Finding Labels1'] == 'Cardiomegaly']['Image Index'].to_list()
lis2files = [i for i in onlyfiles for j in Cardiomegaly if j in i]
subfolder2 = os.path.join(newpath, "Cardiomegaly")
if not os.path.exists(subfolder2):
    os.makedirs(subfolder2)
for i in lis2files:
    source = os.path.join(mypath, i)
    destination = os.path.join(subfolder2, i)
    os.rename(source, destination)


onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]    
Consolidation = df[df['Finding Labels1'] == 'Consolidation']['Image Index'].to_list()
lis3files = [i for i in onlyfiles for j in Consolidation if j in i]
subfolder3 = os.path.join(newpath, "Consolidation")
if not os.path.exists(subfolder3):
    os.makedirs(subfolder3)
for i in lis3files:
    source = os.path.join(mypath, i)
    destination = os.path.join(subfolder3, i)
    os.rename(source, destination)

onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]   
Edema = df[df['Finding Labels1'] == 'Edema']['Image Index'].to_list()
lis4files = [i for i in onlyfiles for j in Edema if j in i]
subfolder4 = os.path.join(newpath, "Edema")
if not os.path.exists(subfolder4):
    os.makedirs(subfolder4)
for i in lis4files:
    source = os.path.join(mypath, i)
    destination = os.path.join(subfolder4, i)
    os.rename(source, destination)

onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]   
Effusion = df[df['Finding Labels1'] == 'Effusion']['Image Index'].to_list()
lis5files = [i for i in onlyfiles for j in Effusion if j in i]
subfolder5 = os.path.join(newpath, "Effusion")
if not os.path.exists(subfolder5):
    os.makedirs(subfolder5)
for i in lis5files:
    source = os.path.join(mypath, i)
    destination = os.path.join(subfolder5, i)
    os.rename(source, destination)

onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))] 
Emphysema = df[df['Finding Labels1'] == 'Emphysema']['Image Index'].to_list()
lis6files = [i for i in onlyfiles for j in Emphysema if j in i]
subfolder6 = os.path.join(newpath, "Emphysema")
if not os.path.exists(subfolder6):
    os.makedirs(subfolder6)
for i in lis6files:
    source = os.path.join(mypath, i)
    destination = os.path.join(subfolder6, i)
    os.rename(source, destination)

onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))] 
Fibrosis = df[df['Finding Labels1'] == 'Fibrosis']['Image Index'].to_list()
lis7files = [i for i in onlyfiles for j in Fibrosis if j in i]
subfolder7 = os.path.join(newpath, "Fibrosis")
if not os.path.exists(subfolder7):
    os.makedirs(subfolder7)
for i in lis7files:
    source = os.path.join(mypath, i)
    destination = os.path.join(subfolder7, i)
    os.rename(source, destination) 

onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))] 
Hernia = df[df['Finding Labels1'] == 'Hernia']['Image Index'].to_list()
lis8files = [i for i in onlyfiles for j in Hernia if j in i]
subfolder8 = os.path.join(newpath, "Hernia")
if not os.path.exists(subfolder8):
    os.makedirs(subfolder8)
for i in lis8files:
    source = os.path.join(mypath, i)
    destination = os.path.join(subfolder8, i)
    os.rename(source, destination)

onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]     
Infiltration = df[df['Finding Labels1'] == 'Infiltration']['Image Index'].to_list()
lis9files = [i for i in onlyfiles for j in Infiltration if j in i]
subfolder9 = os.path.join(newpath, "Infiltration")
if not os.path.exists(subfolder9):
    os.makedirs(subfolder9)
for i in lis9files:
    source = os.path.join(mypath, i)
    destination = os.path.join(subfolder9, i)
    os.rename(source, destination)


onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))] 
Mass = df[df['Finding Labels1'] == 'Mass']['Image Index'].to_list()
lis10files = [i for i in onlyfiles for j in Mass if j in i]
subfolder10 = os.path.join(newpath, "Mass")
if not os.path.exists(subfolder10):
    os.makedirs(subfolder10)
for i in lis10files:
    source = os.path.join(mypath, i)
    destination = os.path.join(subfolder10, i)
    os.rename(source, destination)

onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
Nodule = df[df['Finding Labels1'] == 'Nodule']['Image Index'].to_list()
lis11files = [i for i in onlyfiles for j in Nodule if j in i]
subfolder11 = os.path.join(newpath, "Nodule")
if not os.path.exists(subfolder11):
    os.makedirs(subfolder11)
for i in lis11files:
    source = os.path.join(mypath, i)
    destination = os.path.join(subfolder11, i)
    os.rename(source, destination)

onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]    
Pleural_Thickening = df[df['Finding Labels1'] == 'Pleural_Thickening']['Image Index'].to_list()
lis12files = [i for i in onlyfiles for j in Pleural_Thickening if j in i]
subfolder12 = os.path.join(newpath, "Pleural_Thickening")
if not os.path.exists(subfolder12):
    os.makedirs(subfolder12)
for i in lis12files:
    source = os.path.join(mypath, i)
    destination = os.path.join(subfolder12, i)
    os.rename(source, destination)

onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]    
Pneumonia = df[df['Finding Labels1'] == 'Pneumonia']['Image Index'].to_list()
lis13files = [i for i in onlyfiles for j in Pneumonia if j in i]
subfolder13 = os.path.join(newpath, "Pneumonia")
if not os.path.exists(subfolder13):
    os.makedirs(subfolder13)
for i in lis13files:
    source = os.path.join(mypath, i)
    destination = os.path.join(subfolder13, i)
    os.rename(source, destination)


onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
Pneumothorax = df[df['Finding Labels1'] == 'Pneumothorax']['Image Index'].to_list()
lis14files = [i for i in onlyfiles for j in Pneumothorax if j in i]
subfolder14 = os.path.join(newpath, "Pneumothorax")
if not os.path.exists(subfolder14):
    os.makedirs(subfolder14) 
for i in lis14files:
    source = os.path.join(mypath, i)
    destination = os.path.join(subfolder14, i)
    os.rename(source, destination)   

onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
No_Finding = df[df['Finding Labels1'] == 'No Finding']['Image Index'].to_list()
lis15files = [i for i in onlyfiles for j in No_Finding if j in i]
subfolder15 = os.path.join(newpath, "No_Finding")
if not os.path.exists(subfolder15):
    os.makedirs(subfolder15) 
for i in lis15files:
    source = os.path.join(mypath, i)
    destination = os.path.join(subfolder15, i)
    os.rename(source, destination)    
print(lis15files)

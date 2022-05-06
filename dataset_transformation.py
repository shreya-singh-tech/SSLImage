# python code to load the image dataset and check features

import torchvision
from torchvision import transforms
from torch.utils.data import DataLoader
from PIL import Image

data_path = '/home/shreya/classes/'

transform_img = transforms.Compose([
    transforms.ToTensor(),
])

image_data = torchvision.datasets.ImageFolder(
  root=data_path,transform=transform_img
)

image_data_loader = DataLoader(
  image_data, 
  batch_size=len(image_data), 
  shuffle=False, 
  num_workers=0
)

def mean_std(loader):
  images, lebels = next(iter(loader))
  # shape of images = [b,c,w,h]
  mean, std = images.mean([0,2,3]), images.std([0,2,3])
  return mean, std

mean, std = mean_std(image_data_loader)
print("mean and std: \n", mean, std)

im = Image.open('/home/shreya/classes/Atelectasis/00000711_004.png')
im2 = Image.open('/home/shreya/classes/Edema/00010887_024.png')
im3 = Image.open('/home/shreya/classes/Pleural_Thickening/00020286_012.png')

print(im.size)
print(type(im.size))
print(im2.size)
print(type(im2.size))
print(im3.size)
print(type(im3.size))
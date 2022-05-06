'''
Code is adoped from https://github.com/kekmodel/FixMatch-pytorch/blob/master/dataset/cifar.py
This script does the data preparation part
'''

import logging
import math
import os
import numpy as np
import torchvision
from torchvision import transforms
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision import datasets
import torch

torch.cuda.empty_cache()
from .randaugment import RandAugmentMC

logger = logging.getLogger(__name__)

mean_chest = (0.5015, 0.5015, 0.5015)
std_chest = (0.2532, 0.2532, 0.2532)

data_path = '/home/shreya/unique-fixmatch1/classes'
test_path = '/home/shreya/unique-fixmatch1/test'


def get_data(args, root):

    #change resize if required
    transform_img = transforms.Compose([
        transforms.Resize([int(128), int(128)]),
    transforms.ToTensor(),
    ])

    transform_labeled = transforms.Compose([
        transforms.Resize([int(128), int(128)]),
        transforms.RandomHorizontalFlip(),
        transforms.RandomCrop(size=128,
                              padding=int(128*0.125),
                              padding_mode='reflect'),

        transforms.ToTensor(),
        transforms.Normalize(mean=mean_chest, std=std_chest)
    ])
    transform_val = transforms.Compose([
        transforms.Resize([int(128), int(128)]),
        transforms.ToTensor(),
        transforms.Normalize(mean=mean_chest, std=std_chest)
    ])

    #base_dataset = datasets.CIFAR10(root, train=True, download=True)

    #using ImageFolder automatically converts dataset to RGB
    
    base_dataset = torchvision.datasets.ImageFolder(root=data_path, transform=transform_img)
    print("Base datadownload done")
    

    train_labeled_idxs, train_unlabeled_idxs = x_u_split(
        args, base_dataset.targets)

    print("train data split done")

    train_labeled_dataset = CHESTSSL(
        root, train_labeled_idxs, train=True,
        transform=transform_labeled)

    print("train data labelled done")
    train_unlabeled_dataset = CHESTSSL(
        root, train_unlabeled_idxs, train=True,
        transform=TransformFixMatch(mean=mean_chest, std=std_chest))

    print("train data unlabelled done")    

    test_dataset = torchvision.datasets.ImageFolder(root=test_path, transform=transform_val)
    
    print("test data  done")
    return train_labeled_dataset, train_unlabeled_dataset, test_dataset


def x_u_split(args, labels):
    label_per_class = args.num_labeled // args.num_classes

    labels = np.array(labels)
    labeled_idx = []
    # unlabeled data: all data (https://github.com/kekmodel/FixMatch-pytorch/issues/10)
    unlabeled_idx = np.array(range(len(labels)))
    for i in range(args.num_classes):
        idx = np.where(labels == i)[0]
        idx = np.random.choice(idx, label_per_class, False)
        labeled_idx.extend(idx)
    labeled_idx = np.array(labeled_idx)

    assert len(labeled_idx) == args.num_labeled

    if args.expand_labels or args.num_labeled < args.batch_size:
        num_expand_x = math.ceil(
            args.batch_size * args.eval_step / args.num_labeled)
        labeled_idx = np.hstack([labeled_idx for _ in range(num_expand_x)])
    np.random.shuffle(labeled_idx)
    return labeled_idx, unlabeled_idx


class TransformFixMatch(object):
    def __init__(self, mean, std):
        self.weak = transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.RandomCrop(size=128,
                                  padding=int(128*0.125),
                                  padding_mode='reflect')])
        self.strong = transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.RandomCrop(size=128,
                                  padding=int(128*0.125),
                                  padding_mode='reflect'),
            RandAugmentMC(n=2, m=10)])
        self.normalize = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(mean=mean, std=std)])

    def __call__(self, x):
        weak = self.weak(x)
        strong = self.strong(x)
        return self.normalize(weak), self.normalize(strong)



class CHESTSSL(datasets.ImageFolder):
    def __init__(self, root, indexs, train=True,
                 transform=None, target_transform=None,
                 download=False):
        super().__init__(root, transform=transform, target_transform=target_transform)

        classes, class_to_idx = super().find_classes(root)
        imgs = super().make_dataset(root, class_to_idx, ".png")
        self.root = root
        self.imgs = imgs
        self.classes = classes
        self.class_to_idx = class_to_idx
        

    def __getitem__(self, index):
        path, target = self.imgs[index]
        img = self.loader(path)
        if self.transform is not None:
            img = self.transform(img)
        if self.target_transform is not None:
            target = self.target_transform(target)

        return img, target


DATASET_GETTERS = {'chestdata': get_data}

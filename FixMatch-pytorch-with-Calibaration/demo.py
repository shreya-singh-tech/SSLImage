import fire
import os
import torch
import torchvision as tv
from torch.utils.data.sampler import SubsetRandomSampler
import models.wideresnet as models
from torchvision import transforms
from temperature_scaling import ModelWithTemperature
from dataset.chestdata import DATASET_GETTERS
import argparse
from torch.utils.data import DataLoader, RandomSampler, SequentialSampler

def demo(data, save, depth=40, growth_rate=12, batch_size=16):
    """
    Applies temperature scaling to a trained model.

    Takes a pretrained resnet model, and a validation set
    (parameterized by indices on train set).
    Applies temperature scaling, and saves a temperature scaled version.

    NB: the "save" parameter references a DIRECTORY, not a file.
    In that directory, there should be two files:
    - model.pth (model state dict)
    - valid_indices.pth (a list of indices corresponding to the validation set).

    data (str) - path to directory where data should be loaded from/downloaded
    save (str) - directory with necessary files (see above)
    """
    #parser = argparse.ArgumentParser(description='PyTorch calibration FixMatch Training')
    # Load model state dict
    model_filename = os.path.join(save, 'model_best.pth.tar')
    if not os.path.exists(model_filename):
        raise RuntimeError('Cannot find file %s to load' % model_filename)
    state_dict = torch.load(model_filename)

    # Load validation indices
    valid_indices_filename = os.path.join(save, 'valid_indices_best.pth.tar')
    if not os.path.exists(valid_indices_filename):
        raise RuntimeError('Cannot find file %s to load' % valid_indices_filename)
    valid_indices = torch.load(valid_indices_filename)
    

    # Regenerate validation set loader
    mean_chest = (0.5015, 0.5015, 0.5015)
    std_chest = (0.2532, 0.2532, 0.2532)

    test_path = '/home/shreya/unique-fixmatch1/test'
    transform_val = transforms.Compose([
        transforms.Resize([int(128), int(128)]),
        transforms.ToTensor(),
        transforms.Normalize(mean=mean_chest, std=std_chest)
    ])
    test_dataset = tv.datasets.ImageFolder(root=test_path, transform=transform_val)

    #valid_loader = torch.utils.data.DataLoader(test_dataset, pin_memory=True, batch_size=batch_size,
    #                                           sampler=SubsetRandomSampler(valid_indices))

    valid_loader = torch.utils.data.DataLoader(
        test_dataset,
        sampler=SequentialSampler(test_dataset),
        batch_size= batch_size,
        num_workers=4)

    #for chest data there are 14 classes
    no_classes = 14
    model_depth =28
    model_width =2
    # Load original model
    if (depth - 4) % 3:
        raise Exception('Invalid depth')
    block_config = [(depth - 4) // 6 for _ in range(3)]

    #change model to resnet or wideresnet here
    orig_model = models.build_wideresnet(
        depth=model_depth,widen_factor=model_width,dropout=0,num_classes=no_classes
    ).cuda()

    orig_model.load_state_dict(state_dict,strict=False)

    # Now we're going to wrap the model with a decorator that adds temperature scaling
    model = ModelWithTemperature(orig_model)

    # Tune the model temperature, and save the results
    model.set_temperature(valid_loader)
    model_filename = os.path.join(save, 'model_with_temperature.pth')
    torch.save(model.state_dict(), model_filename)
    print('Temperature scaled model sved to %s' % model_filename)
    print('Done!')

#/home/shreya/FixMatch-pytorch-with-Calibaration/results/chest-unique-calibred
#/home/shreya/unique-fixmatch1/classes

if __name__ == '__main__':
    """
    Applies temperature scaling to a trained model.

    Takes a pretrained DenseNet-CIFAR100 model, and a validation set
    (parameterized by indices on train set).
    Applies temperature scaling, and saves a temperature scaled version.

    NB: the "save" parameter references a DIRECTORY, not a file.
    In that directory, there should be two files:
    - model.pth (model state dict)
    - valid_indices.pth (a list of indices corresponding to the validation set).

    --data (str) - path to directory where data should be loaded from/downloaded
    --save (str) - directory with necessary files (see above)
    """
    fire.Fire(demo)
    
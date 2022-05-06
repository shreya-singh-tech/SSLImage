This is the implementation for Fix-Match and Mean-Teacher on NIH Chest-XRay.(https://nihcc.app.box.com/v/ChestXray-NIHCC)
For more details refer to poster.pdf

# Data Preparation
Download images from https://nihcc.app.box.com/v/ChestXray-NIHCC.
Then run assignfolders.py to divide them into classes. Then run sampledataset.py to divide into train and test set.

# FixMatch
## Usage
cd FixMatch-pytorch
### Train

Train the model by 50 labeled data of chestdata dataset:

```
python train.py --dataset chestdata --num-labeled 50 --arch wideresnet --batch-size 16 --lr 0.03 --expand-labels --seed 5 --out results/chestdata@50
```

### Monitoring training progress
```
tensorboard --logdir=<your out_dir>
```

## Temperature Scaling with FixMatch
cd FixMatch-pytorch-with-Calibration.

Train the model using above command.Then to run with temperature scaling :check parameter of orig_model , then run demo.py

# Mean Teacher
## Usage
cd mean-teacher-master/pytorch
prepare dataset using ./data-local/bin/prepare_semisupervised_sets.sh
### Train
To train on chest-data run :
```
python main.py --dataset chestdata  --labels /home/shreya/mean-teacher-master/pytorch/data-local/labels/bin/labels/chestdata/700_balanced_labels/00.txt --arch cifar_shakeshake26 --consistency 100.0 --consistency-rampup 5 --labeled-batch-size 16 --epochs 180 --lr-rampdown-epochs 210
```

To reproduce the chest data results run 'python -m experiments.chest_test'

## Temperature Scaling with mean teacher
cd mean-teacher-master-with-calib. 

Train the model using above command.Then to run with temperature scaling :check parameter of orig_model , then run demo.py

## Requirements
- python 3.6+
- torch 1.4
- torchvision 0.5
- tensorboard
- numpy
- tqdm
- apex (optional)


## Citations
```
@article{sohn2020fixmatch,
    title={FixMatch: Simplifying Semi-Supervised Learning with Consistency and Confidence},
    author={Kihyuk Sohn and David Berthelot and Chun-Liang Li and Zizhao Zhang and Nicholas Carlini and Ekin D. Cubuk and Alex Kurakin and Han Zhang and Colin Raffel},
    journal={arXiv preprint arXiv:2001.07685},
    year={2020},
}
```
```
  author = {Zech, J.},
  title = {reproduce-chexnet},
  year = {2018},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/jrzech/reproduce-chexnet}}
}
```
```
@misc{https://doi.org/10.48550/arxiv.1706.04599,
  doi = {10.48550/ARXIV.1706.04599},
  url = {https://arxiv.org/abs/1706.04599},
  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},
  keywords = {Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {On Calibration of Modern Neural Networks},
  publisher = {arXiv},
  year = {2017},
  copyright = {arXiv.org perpetual, non-exclusive license}
}

```
```
@misc{https://doi.org/10.48550/arxiv.1703.01780,
  doi = {10.48550/ARXIV.1703.01780},
  url = {https://arxiv.org/abs/1703.01780},
  author = {Tarvainen, Antti and Valpola, Harri},
  keywords = {Neural and Evolutionary Computing (cs.NE), Machine Learning (cs.LG), Machine Learning (stat.ML), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Mean teachers are better role models: Weight-averaged consistency targets improve semi-supervised deep learning results},
  publisher = {arXiv},
  year = {2017},
  copyright = {arXiv.org perpetual, non-exclusive license}
}

```

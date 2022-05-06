
# Copyright (c) 2018, Curious AI Ltd. All rights reserved.
#
# This work is licensed under the Creative Commons Attribution-NonCommercial
# 4.0 International License. To view a copy of this license, visit
# http://creativecommons.org/licenses/by-nc/4.0/ or send a letter to
# Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

"""Train chest labels and all training images. Evaluate against test set."""

import sys
import logging

import torch

import main
from mean_teacher.cli import parse_dict_args
from mean_teacher.run_context import RunContext

torch.cuda.empty_cache()

LOG = logging.getLogger('runner')


def parameters():
    defaults = {
        # Technical details
        'workers': 2,
        'checkpoint_epochs': 20,

        # Data
        'dataset': 'chestdata',
        'train_subdir': 'classes',
        'eval_subdir': 'test',

        # Data sampling
        'base_batch_size': 16,
        'base_labeled_batch_size': 8,

        # Architecture
        'arch': 'cifar_shakeshake26',

        # Costs
        'consistency_type': 'mse',
        'consistency_rampup': 5,
        'consistency': 100.0,
        'logit_distance_cost': .01,
        'weight_decay': 2e-4,

        # Optimization
        'lr_rampup': 0,
        'base_lr': 0.05,
        'nesterov': True,
    }

    

    # 700 labels:
    for data_seed in range(10, 20):
        yield {
            **defaults,
            'title': '700-label chest-data',
            'n_labels': 700,
            'data_seed': data_seed,
            'epochs': 32,
            'lr_rampdown_epochs': 64,
            'ema_decay': 0.97,
        }


def run(title, base_batch_size, base_labeled_batch_size, base_lr, n_labels, data_seed, **kwargs):
    LOG.info('run title: %s, data seed: %d', title, data_seed)

    ngpu = torch.cuda.device_count()
    assert ngpu > 0, "Expecting at least one GPU, found none."

    adapted_args = {
        'batch_size': base_batch_size * ngpu,
        'labeled_batch_size': base_labeled_batch_size * ngpu,
        'lr': base_lr * ngpu,
        'labels': '/home/shreya/mean-teacher-master/pytorch/data-local/labels/bin/labels/chestdata/{}_balanced_labels/{:02d}.txt'.format(n_labels, data_seed),
    }
    context = RunContext(__file__, "{}_{}".format(n_labels, data_seed))
    main.args = parse_dict_args(**adapted_args, **kwargs)
    main.main(context)


if __name__ == "__main__":
    for run_params in parameters():
        run(**run_params)

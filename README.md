# **CellMap Segmentation Challenge Experiments**
### This repository contains the code for the experiments conducted by the CellMap Project Team in order to establish baseline performance metrics for the [CellMap Segmentation Challenge](https://cellmapchallenge.janelia.org). This uses the [challenge repository](https://github.com/janelia-cellmap/cellmap-segmentation-challenge) heavily. In general the code is organized as follows:
```
├── <experiment_name>/
│   ├── logs/
│   ├── checkpoints/
│   ├── __init__.py
│   ├── model.py
│   ├── data.py
│   ├── train_config.py
│   ├── process_config.py
│   ├── datasplit.csv
│   ├── README.md
│   └── ... other experiment specific files/directories
│
├── <experiment_name>/
│   └── ...
│
└── ...
__init__.py
unite_tensorboards.py
README.md
LICENSE
.gitignore
```

You will notice that the experiments contained within these directories use more advanced configurations than those covered in the tutorial examples, as well as making use of other tools/repos such as `cellmap-models`. In general, the `model.py` file contains the model architecture and any checkpoint loading, `data.py` contains configuration of training/validation data splitting/augmentations/transforms/etc., the `train_config.py` file contains the overall training configuration (including settings imported from `model.py` and `data.py`), and the `process_config.py` file contains the prediciton post-processing configuration. The `datasplit.csv` file contains the exact data split used for training and validation, most often generated using a probabilistic split via `cellmap_segmentation_challenge.utils.make_datasplit_csv`. The `logs/` directory contains the training logs as well as any system logs (such as those produced when running jobs on a HPC cluster), and the `checkpoints/` directory contains the model checkpoints. The `__init__.py` file is used to make the experiment directory a Python package. A `README.md` file is also included in each experiment directory to provide additional information about the experiment, including summary results and the team members involved in designing and running it. Logs and checkpoints are not included in this repository, but can be provided upon request (the folder structure is provided to allow for easy replication of the experiments). This general structure is designed to allow for easy and rapid iteration of experiments, as well as to provide a clear and consistent way to organize the code and results.

# Setup:
Follow the instructions in the [main challenge repo](https://github.com/janelia-cellmap/cellmap-segmentation-challenge/tree/main?tab=readme-ov-file#getting-started). This will guide you through setting up the environment and downloading the data. After completing these steps (including activating the virtual environment), install the additional dependencies required for these experiments by running:
```bash
pip install -r requirements.txt
```

# Advanced tools and configurations:

## cellmap-models
The `cellmap-models` repository contains pretrained models and tools for working with them. The pretrained models are used in some of the experiments in this directory. You can find more information about `cellmap-models` [here](https://github.com/janelia-cellmap/cellmap-models).

## cellmap_data
The `cellmap_data` repository contains tools for working with the CellMap Segmentation Challenge data. You can find more information about `cellmap_data` [here](https://github.com/janelia-cellmap/cellmap-data/tree/main). Tools from `cellmap_data` are wrapped for convenience in the `cellmap_segmentation_challenge.utils` module's `dataloader`. In these experiments, you will see more extensive use of `cellmap_data` tools, such as direct use of `CellMapDataSplit` and `CellMapDataLoader`.


## True Negative Masking
Some of the experiments in this directory use a technique called "true negative masking". where possible to provide loss to the model when a mutually exclusive class is present in the ground truth. For instance, if the ground truth contains a mitochondria label at a given pixel, the model will be penalized for predicting extra-cellular space at that pixel. We know this to be a case of a true negative for mitochondria because a mitochondria cannot exist in the extra-cellular space. Since not all crops are densely labelled for all classes, this approach of using true negatives helps us infer labels where possible, thus effectively increasing the amount of training data available to the model.

`cellmap_segmentation_challenge.utils` contains `get_class_relations` to return a dictionary of class relations. This is then passed as an argument during the creation of the `cellmap_data.CellMapDataSplit` object to enable true negative masking.

#

# Models:

## **setup_04**: cellmap-models pretrained UNet
<details>
<summary>Click to expand</summary>
The `setup_04` model was trained as part of the original COSEM Project team, which produced [Whole-cell organelle segmentation in volume electron microscopy](https://www.nature.com/articles/s41586-021-03977-3). You can read more about COSEM pretrained models at the [cellmap-models](https://github.com/janelia-cellmap/cellmap-models/tree/main/src/cellmap_models/pytorch/cosem) repository. `setup_04` is an upsampling UNet, trained to predict 4x4x4nm signed distance transforms for 14 class labels from 8x8x8nm FIBSEM data from the COSEM datasets (~50 densely labeled crops). The classes it was trained to predict are:

    - Extra-cellular space (ecs)
    - Plasma membrane (pm)
    - Mitochondria (mito)
    - Mitochondria membrane (mito_mem)
    - Vesicles (ves)
    - Vesicle membranes (ves_mem)
    - Endosomes (endo)
    - Endosome membranes (endo_mem)
    - Endoplasmic reticulum (er)
    - Endoplasmic reticulum membranes (er_mem)
    - Endoplasmic reticulum exit sites (eres)
    - Nucleus (nuc)
    - Microtubules (mt)
    - Microtubule out (mt_out)
</details>

#

# Experiments:

## setup_04_all
This experiment uses the `setup_04` pretrained model from `cellmap-models` to predict binary masks for all class labels included in the CellMap Segmentation Challenge, using **true negative masking** (see above for details) where possible. This setup uses Binary Cross Entropy loss with a RAdam optimizer.


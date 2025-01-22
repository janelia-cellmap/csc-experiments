import numpy as np
import torch
import torchvision.transforms.v2 as T
import os
import random
from cellmap_segmentation_challenge.utils import get_tested_classes

from cellmap_data.transforms.augment import (
    RandomContrast,
    RandomGamma,
    GaussianNoise,
    Normalize,
    Binarize,
    NaNtoNum,
)

random_seed = getattr(os.environ, "SEED", 13)  # random seed for reproducibility

# %% Set the random seed
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(random_seed)
torch.manual_seed(random_seed)
np.random.seed(random_seed)
random.seed(random_seed)

classes = get_tested_classes()
# use_mutual_exclusion = "named_classes"  # whether to use mutual exclusion loss
use_mutual_exclusion = True  # whether to use mutual exclusion loss
force_all_classes = (
    "validation"  # whether to force all classes to be present in the datasets sampled
)

# Define the spatial transformations to apply to the training data
spatial_transforms = {  # dictionary of spatial transformations to apply to the data
    "mirror": {"axes": {"x": 0.5, "y": 0.5, "z": 0.1}},
    "transpose": {"axes": ["x", "y", "z"]},
    "rotate": {"axes": {"x": [-180, 180], "y": [-180, 180], "z": [-180, 180]}},
}

# Define the value transforms to be applied to the raw and groundtruth data
train_raw_transforms = T.Compose(
    [
        Normalize(),
        T.ToDtype(torch.float, scale=True),
        NaNtoNum({"nan": 0.0, "posinf": None, "neginf": None}),
        T.RandomApply(
            [
                RandomGamma((0.9, 1.1)),
                RandomContrast((0.9, 1.1)),
                # T.GaussianBlur(3, (0.0, 1.1)),
                # TODO: Add IntensityAugmentation
                GaussianNoise(0.0, 0.01),
                # T.RandomErasing(0.1, (0.001, 0.1), value="random"),  # type: ignore
            ]
        ),
    ]
)
val_raw_transforms = T.Compose(
    [
        Normalize(),
        T.ToDtype(torch.float, scale=True),
        NaNtoNum({"nan": 0.0, "posinf": None, "neginf": None}),
    ],
)

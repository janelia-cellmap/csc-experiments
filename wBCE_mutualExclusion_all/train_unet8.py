# %%
import leibnetz

from upath import UPath

from shared import (
    random_seed,
    classes,
    use_mutual_exclusion,
    force_all_classes,
    spatial_transforms,
    train_raw_transforms,
    val_raw_transforms,
)


# %% Set hyperparameters and other configurations
learning_rate = 0.000001  # learning rate for the optimizer
batch_size = 4  # batch size for the dataloader
max_grad_norm = 100  # maximum gradient norm for gradient clipping
epochs = 1000  # number of epochs to train the model for
iterations_per_epoch = 1000  # number of iterations per epoch

# Defining model (comment out all that are not used)
# 3D UNet
model_to_load = model_name = (
    __file__.split("/")[-1].split("_")[-1].removesuffix(".py")
    + f"_all.{random_seed}"  # name of the model for saving
)
load_model = "best"  # load the latest model or the best validation model

model_kwargs = {
    "output_nc": len(classes),
    "top_resolution": (8, 8, 8),
    "final_activation": "Identity",
    "base_nc": 12,
    "nc_increase_factor": 3,
    # "dropout_prob": 0.3,
    "residual": True,
    # "norm_layer": "instance",
    # "squeeze_excitation": True,
}

model = leibnetz.build_unet(**model_kwargs)
model.step_up_size(steps=13, step_size=23)

input_array_info = model.input_shapes[
    "input"
]  # shape and voxel size of the data to load for the input
target_array_info = model.output_shapes["output"]
# shape and voxel size of the data to load for the target

# Define the paths for saving the model and logs, etc.
logs_save_path = UPath(
    "tensorboard/{model_name}"
).path  # path to save the logs from tensorboard
model_save_path = UPath(
    "checkpoints/{model_name}_{epoch}.pth"  # path to save the model checkpoints
).path
datasplit_path = "datasplit.csv"  # path to the datasplit file that defines the train/val split the dataloader should use

# Set a limit to how long the validation can take
validation_time_limit = 60  # time limit in seconds for the validation step

# torch.autograd.set_detect_anomaly(True)

# %%
if __name__ == "__main__":
    from cellmap_segmentation_challenge import train

    train(__file__)

# %%

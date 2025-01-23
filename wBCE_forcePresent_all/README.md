# Experiment: *\<experiment name>*
These models were trained to predict [all of the classes tested in the CellMap Segmentation Challenge](https://janelia-cellmap.github.io/cellmap-segmentation-challenge/annotation_classes.html#detailed-class-descriptions), using only crops that contain annotations for all classes. These setups uses weighted Binary Cross Entropy loss with a RAdam optimizer that has decoupled weight decay. Data augmentation includes random rotations, transposes, mirroring, intensity shifts, and Gaussian noise. Validation time is limited to 1 minute per validation period, so variability in validation scores may be observed.

# Model(s):

## *setup_04_all*: COSEM pretrained model, with upsampling layers removed
<details>
<summary>Click to expand</summary>
The `setup_04_all` model was trained as part of the original COSEM Project team, which produced [Whole-cell organelle segmentation in volume electron microscopy](https://www.nature.com/articles/s41586-021-03977-3). You can read more about COSEM pretrained models at the [cellmap-models](github.com/janelia-cellmap/cellmap-models) repository. `setup_04_all` is an upsampling UNet, trained to predict 4x4x4nm signed distance transforms for 14 class labels from 8x8x8nm FIBSEM data from the COSEM datasets (~50 densely labeled crops). The classes it was trained to predict are:

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

In this case, the upsampling layers and final output head have been removed, and replaced with several 3x3x3 convolutions to predict binary masks for all class labels included in the CellMap Segmentation Challenge. 
</details>

## *unet8_all*: 8x8x8nm FIBSEM data trained UNet
<details>
<summary>Click to expand</summary>
The `unet8_all` model was trained from scratch here on 8x8x8nm FIBSEM data from the CellMap Segmentation Challenge datasets. It is a standard UNet architecture with 3x3x3 convolutions, no normalization, residual connections across blocks at each encoder/decoder level, and ReLU activations. It was trained to predict binary masks for all class labels included in the CellMap Segmentation Challenge. LeibNetz is used to construct the model.
</details>

## *unet32_all*: 32x32x32nm FIBSEM data trained UNet
<details>
<summary>Click to expand</summary>
The `unet32_all` model was trained from scratch here on 32x32x32nm FIBSEM data from the CellMap Segmentation Challenge datasets. It is a standard UNet architecture with 3x3x3 convolutions, no normalization, residual connections across blocks at each encoder/decoder level, and ReLU activations. It was trained to predict binary masks for all class labels included in the CellMap Segmentation Challenge. LeibNetz is used to construct the model.
</details>

## *unet128_all*: 128x128x128nm FIBSEM data trained UNet
<details>
<summary>Click to expand</summary>
The `unet128_all` model was trained from scratch here on 128x128x128nm FIBSEM data from the CellMap Segmentation Challenge datasets. It is a standard UNet architecture with 3x3x3 convolutions, no normalization, residual connections across blocks at each encoder/decoder level, and ReLU activations. It was trained to predict binary masks for all class labels included in the CellMap Segmentation Challenge. LeibNetz is used to construct the model.
</details>


# Results:
**setup_04_all**: ...
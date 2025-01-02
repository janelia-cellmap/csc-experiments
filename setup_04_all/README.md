# Experiment: setup_04_all
This experiment uses the `setup_04` pretrained model from `cellmap-models` to predict binary masks for all class labels included in the CellMap Segmentation Challenge, using **true negative masking** (see above for details) where possible. This setup uses Binary Cross Entropy loss with a RAdam optimizer.


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

from upath import UPath
from cellmap_segmentation_challenge.utils import make_datasplit_csv
from shared import (
    classes,
    force_all_classes,
)

# %% Make the data split
if not (UPath(__file__).parent / "datasplit.csv").exists():
    make_datasplit_csv(
        classes=classes,
        force_all_classes=force_all_classes,
        validation_prob=0.1,
        csv_path=(UPath(__file__).parent / "datasplit.csv").path,
    )

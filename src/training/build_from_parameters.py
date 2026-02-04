
from typing import Any, Dict



from src.dataset.h5_dataset import H5Dataset



def get_dataset(
    param: Dict[str, Any],
):
    """
    Constructs the dataset based on provided parameters.

    Args:
        param (Dict[str, Any]): Dictionary containing configuration parameters.

    Returns:
        Dataset: The constructed dataset.

    Raises:
        ValueError: If the dataset extension specified in param is not supported.
    """

    dataset_params = param.get("dataset", {})
    targets = dataset_params.get("targets", [])
    if len(targets) == 0:
        raise ValueError("Please provide a list of target properties to predict.")
    extension = dataset_params.get("extension", "")

    if extension == "h5":
        return H5Dataset(
            h5_path=dataset_params["h5_path"],
            meta_path=dataset_params["meta_path"],
            targets=targets,
        )

    else:
        raise ValueError(f"Dataset extension '{extension}' not supported.")

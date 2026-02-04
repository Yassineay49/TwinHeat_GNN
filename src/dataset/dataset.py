import json
from abc import ABC

from torch_geometric.data import Data, Dataset








class BaseDataset(Dataset, ABC):
    def __init__(
        self,
        meta_path: str,
        targets: list[str],
    ):

        with open(meta_path, "r") as fp:
            meta = json.load(fp)
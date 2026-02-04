


from src.dataset.dataset import BaseDataset



class H5Dataset(BaseDataset):
    def __init__(
        self,
        h5_path: str,
        meta_path: str,
        targets: list[str] = None,
    ):

        super().__init__(
                meta_path=meta_path,
                targets=targets,
            )


        self.h5_path = h5_path

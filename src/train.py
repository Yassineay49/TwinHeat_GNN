import json


import torch
from absl import app, flags
from loguru import logger


from src.training.build_from_parameters import (
    get_dataset
)

FLAGS = flags.FLAGS



flags.DEFINE_string(
    "training_parameters_path", None, "Path to the training parameters JSON file"
)

def main(argv):

    # Check that the training parameters path is provided
    if not FLAGS.training_parameters_path:
        raise ValueError("The 'training_parameters_path' flag must be provided.")


    # Load training parameters from JSON file
    training_parameters_path = FLAGS.training_parameters_path
    logger.info(f"Opening training parameters from {training_parameters_path}")
    try:
        with open(training_parameters_path, "r") as fp:
            parameters = json.load(fp)
    except Exception as e:
        logger.error(f"Error reading training parameters: {e}")
        return


    # Select GPU (CUDA) if available, otherwise fall back to CPU
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    logger.info(f"Using device: {device}")


    # Get training dataset
    train_dataset = get_dataset(
        param=parameters,
    )








    print("yes")












if __name__ == "__main__":
    app.run(main)
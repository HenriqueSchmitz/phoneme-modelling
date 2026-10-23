import argparse
import json
import os
from pathlib import Path

from phoneme_modelling.synthetic_audio.pipeline import SyntheticAudioPipeline


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_path", default="config/default.json")
    parser.add_argument("--output_folder", default="phonemes")
    parser.add_argument("--output_metadata_path", default="data/phonemes_metadata.csv")
    args = parser.parse_args()

    config_path = Path(args.config_path)
    output_folder = Path(args.output_folder)
    output_metadata_path = Path(args.output_metadata_path)
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(output_metadata_path.parent, exist_ok=True)

    with open(config_path, "r", encoding="utf-8") as config_file:
        config = json.load(config_file)

    SyntheticAudioPipeline.run(config, output_folder, output_metadata_path)

if __name__ == "__main__":
    main()
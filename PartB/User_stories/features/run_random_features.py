import os
import random
import subprocess

# Get the directory of the current Python file
current_file_directory = os.path.dirname(os.path.abspath(__file__))

# Path to the features directory, assuming it's in the same directory as this Python script
# features_dir = os.path.join(current_file_directory, "features")

# Get a list of all feature files in the features directory
features = [os.path.join(current_file_directory, f) for f in os.listdir(current_file_directory) if f.endswith(".feature")]

# Shuffle feature files
random.shuffle(features)

# Run each feature file with Behave
for feature in features:
    subprocess.run(["behave", feature])
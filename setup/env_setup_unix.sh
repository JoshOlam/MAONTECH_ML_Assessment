# Setup the work environment

## Clone the repository in your present working directory
git clone https://github.com/JoshOlam/MAONTECH_ML_Assessment.git

## Move the present working directory into the git repository
cd MAONTECH_ML_Assessment

## Create a virtual environment in the current directory
python3 -m venv maon_venv

## Activate the environment (Linux or MacOS)
source maon_venv/bin/activate

## Install the requirement packages in the working environment
pip install setup/requirements.txt

## Create a jupyter kernel
python -m ipykernel install --user --name=maonKernel

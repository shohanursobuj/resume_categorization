<div align="center">

# Resume Categorization
| Version Info | [![Python](https://img.shields.io/badge/python-v3.10.0-green)](https://www.python.org/downloads/release/python-3913/) [![Platform](https://img.shields.io/badge/Platforms-Ubuntu%2022.04.1%20LTS%2C%20win--64-orange)](https://releases.ubuntu.com/20.04/) |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Author       | [![LinkedIn-profile](https://img.shields.io/badge/LinkedIn-Profile-informational?logo=linkedin)](https://www.linkedin.com/in/shohanursobuj/) [![GitHub-profile](https://img.shields.io/badge/GitHub-Profile-informational?logo=github)](https://github.com/shohanursobuj)
---

</div>

This project uses Machine Learning and Natural Language Processing to categorize resumes. A script that takes a directory of resumes and categorizes them according to the content of the resume.



## 🚀 Installation

To run this project you need to clone this repository and install the dependencies.
### Prerequisites
- Python 3.9.0 or higher
- pip 21.2.4 or higher
- conda 4.10.3 or higher (optional)

#### Step 1: Clone this repository

```bash
git clone https://github.com/shohanursobuj/resume_categorization
cd resume_categorization # change directory
```

#### Step 2: Create virtual environment

*Conda environment:*

```bash
conda create -n <env_name> python=3.10.0 # create virtual environment
conda activate <env_name> # activate virtual environment
```
#### *virtualenv:*

Windows OS:
```bash
python -m venv venv_name # create virtual environment
venv_name\Scripts\activate # activate virtual environment
```

Linux/Mac OS:
```bash
python3 -m venv venv_name # create virtual environment
source venv_name/bin/activate # activate virtual environment
```
>Replace `venv_name` with the desired name of your virtual environment.


#### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```
> Run the [`resume_categorization.ipynb`](resume_categorization.ipynb) file in jupyter notebook to get the model.


## 📦 Running the Application

#### Step 4: Run the script

Run the [`script.py`](script.py) file with the `--input_dir` argument to categorize the resumes.

```bash
python script.py --input_dir <input_dir> 
```

For example:

```bash
python script.py --input_dir ./test_data
```


> By running the script will move the resumes to the respective folders according to the category of the resume and will create a `categorize_resume.csv` file in the current directory.

**Note:** This project is tested on Python 3.10.0
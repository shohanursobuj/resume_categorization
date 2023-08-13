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

#### Clone this repository

```bash
git clone https://github.com/shohanursobuj/resume_categorization
```

#### Install dependencies

```bash
pip install -r requirements.txt
```
> Run the [`resume_categorization.ipynb`](resume_categorization.ipynb) file in jupyter notebook to get the model.


## 📦 Running the Application

```bash
python script.py --input_dir <input_dir> 
```

For example:

```bash
python script.py --input_dir ./test_data
```

> By running the script will move the resumes to the respective folders according to the category of the resume and will create a `categorize_resume.csv` file in the current directory.

**Note:** This project is tested on Python 3.10.0
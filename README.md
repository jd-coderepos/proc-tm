### proc-tm: Prompts for Structured Procedure Extraction from Product Manual Specifications

#### About

This repository hosts an annotated dataset of prompts for structured procedural extraction 
using large language models (LLMs)
from domain-specific product manuals as non-machine-actionable PDFs written in natural language text. 


#### Repository Structure

```commandline
.
└── proc-tm           <- root directory of the repository
    ├── data
    │   ├── processed             <- contains the processed data
    │   └── raw                   <- contains the raw data
    ├── models                          <- contains the trained/used models
    ├── notebooks                       <- contains the notebooks used
    ├── README.md                       <- README file for documenting the service.
    ├── requirements.txt                <- contains python requirements listed with specifying the versions
    └── src
        ├── data                        <- contains python scripts for interacting with the dataset
        │   ├── __init__.py
        │   └── make_dataset.py
        ├── __init__.py
        ├── main.py                     <- main python script that shows the order of running the scripts
        ├── models                      <- containts python scripts for interacting with the models
        │   ├── evaluate.py
        │   ├── __init__.py
        │   ├── predict.py
        │   └── train.py
        └── util                        <- contains utility scripts/functions
        │   ├── functions.py
        │   ├── __init__.py
        │   ├── io.py
        │   └── type.py	

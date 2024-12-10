### proc-tm: Prompts for Structured Procedure Extraction from Product Manual Specifications

#### About

This repository hosts an annotated dataset of prompts for structured procedural extraction (or text mining (tm))
using large language models (LLMs)
from domain-specific product manuals as non-machine-actionable PDFs written in natural language text. 


#### Repository Structure

```commandline
.
└── proc-tm                                      <- root directory of the repository
    ├── photography                              <- data domain 1
        ├── manual-chunks                  <- split PDF procedure-wise page chunks
	        ├── procedure[x].pdf
	        └── ...
        └── type1 - list prompts           <- first prompt instruction type for procedural tm using LLMs
            └── raw				  <- prompt ChatGPT out-of-the-box
	           ├── prompts.txt   <- prompts collection
	           ├── chatgpt-response-example[x].txt   <- response from ChatGPT
	           ├── ...
	           ├── goldstd-response-example[x].txt   <- human-annotated response
	           └── ...	
            └── 2shot				  <- prompt ChatGPT in a 2-shot setting
	           ├── prompts.txt
	           └── chatgpt-response.txt
            └── ontology			  <- prompt ChatGPT out-of-the-box with an ontology
	           ├── prompts.txt
	           ├── ...	 
	           └── ...		
            └── ontology+2shot		  <- prompt ChatGPT in a 2-shot setting with an ontology
	           ├── prompts.txt
	           ├── ...	 
	           └── ...
        └── type2 - count prompts          <- second prompt instruction type for procedural tm using LLMs
            ├── raw				  <- prompt ChatGPT out-of-the-box	
            ├── ...            
            └── ontology+2shot		  <- prompt ChatGPT in a 2-shot setting with an ontology
        └── type3 - comparison prompts     <- third prompt instruction type for procedural tm using LLMs
            ├── raw				  <- prompt ChatGPT out-of-the-box	
            ├── ...            
            └── ontology+2shot		  <- prompt ChatGPT in a 2-shot setting with an ontology
        └── type4 - nested_proc prompts    <- fourth prompt instruction type for procedural tm using LLMs
            ├── raw				  <- prompt ChatGPT out-of-the-box	
            ├── ...            
            └── ontology+2shot		  <- prompt ChatGPT in a 2-shot setting with an ontology
        └── type5 - sequence prompts       <- fifth prompt instruction type for procedural tm using LLMs
            ├── raw				  <- prompt ChatGPT out-of-the-box	
            ├── ...            
            └── ontology+2shot		  <- prompt ChatGPT in a 2-shot setting with an ontology
	├── agriculture                              <- data domain 2
	├── medicine                                 <- data domain 3
	├── manufacturing                            <- data domain 4
	├── ontology-procedure.ttl                   <- the procedural ontology structure	
    └── README.md                       <- README file for documenting the dataset
```

#### Citation

Our work is published as a research paper in the [12th Knowledge Capture Conference (K-CAP 2023)](https://www.k-cap.org/2023/) proceedings. If you find this resource helpful, we kindly ask that you cite our work!

```commandline
@inproceedings{10.1145/3587259.3627572,
author = {Rula, Anisa and D'Souza, Jennifer},
title = {Procedural Text Mining with Large Language Models},
year = {2023},
isbn = {9798400701412},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3587259.3627572},
doi = {10.1145/3587259.3627572},
abstract = {Recent advancements in the field of Natural Language Processing, particularly the development of large-scale language models that are pretrained on vast amounts of knowledge, are creating novel opportunities within the realm of Knowledge Engineering. In this paper, we investigate the usage of large language models (LLMs) in both zero-shot and in-context learning settings to tackle the problem of extracting procedures from unstructured PDF text in an incremental question-answering fashion. In particular, we leverage the current state-of-the-art GPT-4 (Generative Pre-trained Transformer 4) model, accompanied by two variations of in-context learning that involve an ontology with definitions of procedures and steps and a limited number of samples of few-shot learning. The findings highlight both the promise of this approach and the value of the in-context learning customisations. These modifications have the potential to significantly address the challenge of obtaining sufficient training data, a hurdle often encountered in deep learning-based Natural Language Processing techniques for procedure extraction.},
booktitle = {Proceedings of the 12th Knowledge Capture Conference 2023},
pages = {9–16},
numpages = {8},
keywords = {knowledge capture, knowledge representation},
location = {Pensacola, FL, USA},
series = {K-CAP '23}
}
```
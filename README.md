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
        ├── manual-chunks                 <- split PDF procedure-wise page chunks
	    │   ├── procedure[x].pdf
	    │   └── ...
        ├── type1 - list prompts           <- first prompt instruction type for procedural tm using LLMs
        │   ├── raw				  <- prompt ChatGPT out-of-the-box
	    │   │  ├── prompts.txt
	    │   │  ├── chatgpt-response-example[x].txt
	    │   │  ├── ...
	    │   │  ├── goldstd-response-example[x].txt
	    │   │  └── ...	
        │   ├── 2shot				  <- prompt ChatGPT in a 2-shot setting
	    │   │  ├── prompts.txt
	    │   │  └── chatgpt-response.txt
    │   │   ├── ontology			  <- prompt ChatGPT in a 2-shot setting
	│   │   │  ├── prompts.txt
	│   │   │  ├── chatgpt-response-example[x].txt
	│   │   │  ├── ...
	│   │   │  ├── goldstd-response-example[x].txt
	│   │   │  └── ...		
    │   │   └── ontology+2shot		  <- prompt ChatGPT in a 2-shot setting
	│   │   │  ├── prompts.txt
	│   │   │  ├── chatgpt-response-example[x].txt
	│   │   │  ├── ...
	│   │   │  ├── goldstd-response-example[x].txt
	│   │   │  └── ...		
    │   ├── type2 - count prompts          <- second prompt instruction type for procedural tm using LLMs
    │   │   ├── raw				  <- prompt ChatGPT out-of-the-box	
	│   │   ├── ...            
	│   │   └── ontology+2shot		  <- prompt ChatGPT 
    │   ├── type3 - comparison prompts     <- third prompt instruction type for procedural tm using LLMs
    │   │   ├── raw				  <- prompt ChatGPT out-of-the-box	
	│   │   ├── ...            
	│   │   └── ontology+2shot		  <- prompt ChatGPT 	
    │   ├── type4 - nested_proc prompts    <- fourth prompt instruction type for procedural tm using LLMs
    │   │   ├── raw				  <- prompt ChatGPT out-of-the-box	
	│   │   ├── ...            
	│   │   └── ontology+2shot		  <- prompt ChatGPT 	
    │   └── type5 - sequence prompts       <- fifth prompt instruction type for procedural tm using LLMs
    │   │   ├── raw				  <- prompt ChatGPT out-of-the-box	
	│   │   ├── ...            
	│   │   └── ontology+2shot		  <- prompt ChatGPT 	
    └── README.md                       <- README file for documenting the service.

# RespondeoQA: a Benchmark for Bilingual Latin-English Question Answering

This repository contains the code and data for the RespondeoQA benchmark, introduced in the paper "RespondeoQA: a Benchmark for Bilingual Latin-English Question Answering" by Marisa Hudspeth, Patrick J. Burns, and Brendan O'Connor.

## Data

The final version of the dataset used in the paper can be found in the `data/final_dataset` folder.

We have also provided the original pdf scans of the textbooks in the `data/pdfs` folder, and the raw text of the textbooks after OCR processing in the `data/raw_text` folder.

## Code

The `scripts` folder contains the code for
- running pdfs through OCR (`scripts/ocr/`)
- converting the raw text to structured output, through a mix of regex, LLMs, and manual review (`scripts/structured_output_scripts/`)
- running LLMs on the dataset (`scripts/run_models_scripts/`)
- evaluating the model responses (`scripts/evaluation_scripts/`)




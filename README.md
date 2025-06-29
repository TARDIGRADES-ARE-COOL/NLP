# NLP

# Text Preprocessing Pipeline 🚀
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

> **Exploring NLP:** A modular pipeline for cleaning and tokenizing text data from TripAdvisor hotel reviews, with next steps toward full-featured natural language processing.

---

## 📖 Table of Contents
1. [Overview](#overview)  
2. [Features](#features)  
3. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
4. [Usage](#usage)  
5. [Pipeline Steps](#pipeline-steps)  
6. [Roadmap & Exploration](#roadmap--exploration)  
7. [Contributing](#contributing)  
8. [License](#license)  

---

## 🔍 Overview
This repository implements the **text-preprocessing** portion of an NLP workflow using Python, NLTK, and pandas. You’ll see how to prepare raw text for downstream tasks like sentiment analysis or topic modeling by:

- Normalizing case  
- Removing stopwords and punctuation  
- Tokenizing into words  
- Lemmatizing to dictionary forms  
- Extracting and counting unigrams  

---

## ⭐ Features
- **Lowercasing**: Normalize all text to lowercase.  
- **Stopword Removal**: Drop common words (excluding negation words like `not`).  
- **Punctuation Stripping**: Replace rating symbols (`*`) and remove other non-word characters.  
- **Tokenization**: Convert sentences into word tokens.  
- **Lemmatization**: Map tokens to their base forms with WordNet.  
- **Unigram Extraction**: Compute frequency counts of individual words.  

---

## 🛠 Getting Started

### Prerequisites
- Python **3.7** or higher  
- pip package manager  

### Installation
1. **Clone** the repo:  
   ```bash
   git clone https://github.com/your-username/text-preprocessing-pipeline.git
   cd text-preprocessing-pipeline

# Fake Ukrainian News Detection Project 

## Project Description  
This is a student project for the **Machine Learning** course, aimed at developing an application for detecting fake news.  

📌 The main goal is to create a machine learning model capable of analyzing Ukrainian news texts and determining their authenticity.   

## Approach 

### 1. Data Collection   
- Searching for available Ukrainian news datasets  
- Downloading datasets
- Analyzing the data structure and identifying key fields (**URL, title, text, source, date**)  

### 2. Data Preprocessing  
- Extracting website domains for **source analysis**  
- Removing duplicates and unnecessary data  
- Analyzing data distribution and identifying the most common **news sources**  
- Balancing classes (if needed)  

### 3. Model Development  
- Choosing a **machine learning algorithm** 
- Using **vectorization** or **transformer models** 
- Training the model and evaluating its performance 
- Optimizing hyperparameters to improve **accuracy** 
- Evaluating model performance on a **test dataset**   

## 📊 Datasets Used  

1. **Ukrainian Fake and True News**  
   - Source: [Kaggle](https://www.kaggle.com/datasets/zepopo/ukrainian-fake-and-true-news)  
   - Description: Contains Fake and True news about Russo-Ukrainian war

2. **Ukrainian News**  
   - Source: [Hugging Face](https://huggingface.co/datasets/zeusfsx/ukrainian-news)  
   - Description: A dataset of news articles downloaded from various Ukrainian websites and Telegram channels

3. **Divided Dataset from Hugging Face**  
   - Source: [Filemail](https://bebra-bebrynka.filemail.com/d/rhfwkzhvbwtwmen)  
   - Description: A modified version of the Hugging Face dataset, divided into 22 parts, each containing 1 million rows.  


## 🚀 Development Journey
### 📌the part about our project success story
**🗓 2025-02-03** – Team Formation

**💡2025-02-06** – Development of the Idea to Tackle Disinformation

**🔍2025-02-14** – Searched for datasets with Ukrainian news, but failed

**📰2025-02-16** – The first try to scrap news from [`TSN.ua`](https://tsn.ua/)
 - News is scrapping very slowly so we decided to find other ways of collecting data

**🤔2025-02-17** 
 - Came across the problem of labeling data (how to label a huge amount of data (fake or real) by ourselves?)
 - The second try to find the dataset and already successful. (We found [`ukrainian-news`](https://huggingface.co/datasets/zeusfsx/ukrainian-news) on HuggingFace and
  [`Ukrainian News`](https://www.kaggle.com/datasets/zepopo/ukrainian-fake-and-true-news) on Kaggle)
- We consider the idea of labeling data this way: Choose sources we trust and mark that news as '**real**', then choose some suspicious sources and mark them as '**fake**'

**🗂️2025-02-18**
 - Trying to download [`ukrainian-news`](https://huggingface.co/datasets/zeusfsx/ukrainian-news) dataset on HuggingFace but came across of lacking resources (the dataset is really large and takes a lot of RAM to process). So we decide to divide the dataset into 20 subsets for better processing.

Coming soon...

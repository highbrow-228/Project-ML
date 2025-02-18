# 📖 Documentation for project: **Detection of fake Ukrainian news**

### 📌 Description:
This is a student project for the **Machine Learning** course, aimed at developing an application for detecting fake news.

### 🎯 The main goal:
Create a machine learning model capable of analyzing Ukrainian news texts and determining their authenticity.

# ✅Approach
### 1️⃣ Data Collection
- Searching for available Ukrainian news datasets in internet
- Downloading datasets (*if we find it*)
- Analyze the data structure and identify key fields (**URL, title, text, source, date**). What sources the news is from, etc.

### 2️⃣ Data Preprocessing
- Extracting relevant information for further work. For example:
   * Title
   * Text of news
   * Time when the news was published
   * Additional info that will be needed later
- Removing duplicates and unnecessary data
- Analyzing data distribution and identifying news sources. We divide them into the following
   - **Sources we trust:**
      * [**TSN**](https://tsn.ua/news)
      * [**BBC**](https://www.bbc.com/ukrainian)
      * [**Суспільне**](https://t.me/suspilnenews)
      * [**ҐРУНТ**](https://t.me/gruntmedia)
      * [**STERNENKO**](https://t.me/ssternenko)
      * [**Лачен пише**](https://t.me/lachentyt)
   - **Sources we do not trust:**
      * [**Вокс Україна**](https://voxukraine.org/category/voks-informue)
      * [**Война с фейками**](https://t.me/warfakes)
- Balancing classes (if necessary)

### 3️⃣ Model Development
- Selection of a **machine learning algorithm** by the selection method.
- Training of the selected algorithm
- Determining its performance.
- Optimization of hyperparameters to increase the accuracy.
- (Optional) If the approach fails, consider:
   - Using an LLM model.
   - Falling back to GPT-based classification.

# 📊 Datasets Used

### 1️⃣ **Ukrainian Fake and True News**
- Source: [Kaggle](https://www.kaggle.com/datasets/zepopo/ukrainian-fake-and-true-news)
- Description: Contains Fake and True news about Russo-Ukrainian war

### 2️⃣ **Ukrainian News**
- Source: [Hugging Face](https://huggingface.co/datasets/zeusfsx/ukrainian-news)
- Description: A dataset of news articles downloaded from various Ukrainian websites and Telegram channels

* **Divided the Dataset from Hugging Face**
   - Source: [Filemail](https://bebra-bebrynka.filemail.com/d/rhfwkzhvbwtwmen)
   - Description: A modified version of the Hugging Face dataset, divided into 22 parts, each containing 1 million rows.
   - Using this [code](split_all_dataset_from_hf.py) for that purpose.

# 🚀 Development Journey
## 📌 Part about our project success story
**1️⃣ 2025-02-03** – Team Formation

**💡2025-02-06** – Development of the Idea to Tackle Disinformation

**🔍2025-02-14** – Searched for datasets with Ukrainian news, but failed

**📰2025-02-16** – The first try to scrap news from **[TSN.ua](https://tsn.ua/news)**
 - News is scrapping very slowly so we decided to find other ways of collecting data

**🤔2025-02-17**
 - Came across the problem of labeling data (how to label a huge amount of data (fake or real) by ourselves?)
 - The second try to find the dataset and already successful. (We found [`ukrainian-news`](https://huggingface.co/datasets/zeusfsx/ukrainian-news) on HuggingFace and
  [`Ukrainian News`](https://www.kaggle.com/datasets/zepopo/ukrainian-fake-and-true-news) on Kaggle)
- We consider the idea of labeling data this way: Choose sources we trust and mark that news as '**real**', then choose some suspicious sources and mark them as '**fake**'

**🗂️2025-02-18**
 - Trying to download [`ukrainian-news`](https://huggingface.co/datasets/zeusfsx/ukrainian-news) dataset on HuggingFace but came across of lacking resources (the dataset is really large (*22 milion rows*) and takes **a lot of RAM to process**). So we decide to divide the dataset into 23 subsets for better processing.


**📌 Next Steps... Stay Tuned!**
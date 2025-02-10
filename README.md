# Ecommerce Recommendation Chatbot

This project is an **Ecommerce Recommendation Chatbot** that leverages user reviews to provide personalized product recommendations. The chatbot is built using **Flipkart Chatbot** and various AI-powered models to enhance user experience.

## 🛠️ Setup and Installation

### 1️⃣ Install Anaconda (if not already installed)
If you don't have Anaconda, download and install it from here:  
🔗 [Anaconda Download](https://www.anaconda.com/download/success)

### 2️⃣ Create a Conda Environment
```sh
conda create -p <env_name> python=3.10 -y
```

### 3️⃣ Activate the Conda Environment
For **Windows**:
```sh
conda activate <env_path>
```
For **Linux/macOS (Bash Terminal)**:
```sh
source activate ./<env_name>
```

### 4️⃣ Install Dependencies
Create a `requirements.txt` file and install all required dependencies:
```sh
pip install -r requirements.txt
```

### 5️⃣ Setup Environment Variables
Create a `.env` file in your project directory and add the following:
```sh
## Only for reference ##
GROQ_API_KEY="gskJOElTaKd7mCQo9bMnT4EwAHCxdFCte4EO"
ASTRA_DB_API_ENDPOINT="https://8d7297e-16b3-4020-8960-81054f7a25-us-east-2.apps.astra.datastax.com"
ASTRA_DB_APPLICATION_TOKEN="AstraCS:TnEJBnBFkaaZqQ:d66326e48341462f4dc2ec8922b51fc7839c140a6b95a2dc06fbeeeead40c4cd"
ASTRA_DB_KEYSPACE="default_keyspace"
HF_TOKEN="hf_CwWlvvzqTwzVqH
jVpTphwW"
```

### 6️⃣ Install Local Package
You can install the local package using **setup.py**:
```sh
python setup.py install
```
Alternatively, add `-e .` inside `requirements.txt` to install it automatically.

## 🚀 Usage
Once installed, you can start the chatbot service and interact with it for personalized product recommendations based on user reviews.

## 📌 Features
- 🛒 **Personalized Recommendations** based on user reviews.
- 🤖 **AI-powered Chatbot** for enhanced user experience.
- 📊 **Data-driven Insights** from Flipkart reviews.
- 🔒 **Secure API Integration** with Astra DB & Hugging Face models.

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repository, create a new branch, and submit a pull request.

## 📜 License
This project is licensed under the MIT License.

---
Developed with ❤️ for smarter shopping experiences! 🛍️🤖


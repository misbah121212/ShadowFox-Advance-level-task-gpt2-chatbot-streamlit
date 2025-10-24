# 🤖 Fine-Tuned GPT-2 Chatbot with Streamlit

![Python Version](https://img.shields.io/badge/python-3.11-blue) 
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-orange) 
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-purple)
![PyTorch](https://img.shields.io/badge/PyTorch-2.1.0-red)

---

## 🌟 Introduction

Welcome to the **GPT-2 Fine-Tuned Chatbot Project**!  
This project demonstrates the **full lifecycle of building a language model-based chatbot**:

- Fine-tuning **GPT-2** on a custom dataset
- Evaluating its conversational and contextual understanding
- Deploying it as a real-time **interactive chatbot** with **Streamlit**

It’s designed as a practical showcase for **AI, NLP, and ML skills** while following **Advanced project guidelines** for exploring LMs, conducting analysis, and visualizing results.

---

## 📌 Project Overview

The project aims to:

1. Implement and fine-tune a **Language Model (LM)** of choice (GPT-2)  
2. Conduct a detailed **performance and capability analysis**  
3. Build a **web-based interactive interface** using Streamlit  
4. Visualize results to understand the LM's contextual understanding and text generation behavior  

**Dataset Used:** `data.txt` – a conversational text corpus for fine-tuning GPT-2.  
You can replace this with your own dataset in the same file if desired.

---

## 🗂️ Project Structure

LM_Project/
├── app.py # Streamlit Chatbot Interface
├── data.txt # Custom fine-tuning dataset
├── GPT2_LM_Project.ipynb # Jupyter notebook (implementation & analysis)
├── models/ # Fine-tuned GPT-2 checkpoints
├── README.md # Project documentation
└── requirements.txt # Dependencies

yaml
Copy code

---

## 🧠 Model Selection: GPT-2

- **Model:** GPT-2 (OpenAI)  
- **Reason:** Strong contextual understanding, suitable for conversational AI, and fully compatible with Hugging Face Transformers  
- **Fine-Tuning:** Adapted to domain-specific conversational patterns from `data.txt`

---

## 🛠️ Implementation Highlights

1. **Environment Setup**  
   Python 3.11, PyTorch, Transformers, Streamlit  

2. **Data Preparation**  
   Custom text corpus for fine-tuning

3. **Model Training**  
   Fine-tuned GPT-2 using Hugging Face `Trainer` API  
   - Tokenization  
   - Data collator for causal LM  
   - Training arguments: epochs, batch size, learning rate

4. **Evaluation & Analysis**  
   - Contextual understanding  
   - Creativity in text generation  
   - Multi-turn dialogue testing  

5. **Streamlit Deployment**  
   Real-time chatbot with user input field and GPT-2 responses  

---

## 💬 Streamlit Chatbot Usage

Run the app locally:

```bash
streamlit run app.py
Open the URL provided in your browser (e.g., http://localhost:8501) and start chatting with your fine-tuned GPT-2 model.

📊 Results & Analysis
GPT-2 maintained strong contextual consistency after fine-tuning

Demonstrated creative responses with minimal dataset

Occasional repetition for vague prompts, which is expected with small-scale LMs

Visualization:

Training loss curves

Token prediction heatmaps

Generated text comparisons (baseline vs. fine-tuned)

🔍 Research Questions
How well can GPT-2 understand conversational context?

Can GPT-2 adapt to domain-specific conversational styles?

What are its limitations for abstract or multi-turn prompts?

🧭 Conclusion & Future Work
Insights:

Fine-tuning improves context retention and response relevance

GPT-2 is effective for conversational AI with small datasets

Future Enhancements:

Larger datasets for better generalization

Multi-turn memory integration

Reinforcement learning or prompt engineering for improved control

🧑‍💻 Author
Misba Sikandar
Department of AIML, HKBK College of Engineering
Project: Fine-Tuned GPT-2 Chatbot with Streamlit
Date: October 2025

🔗 Resources
Hugging Face Transformers

Streamlit Documentation

PyTorch

AI Data Scientist Roadmap

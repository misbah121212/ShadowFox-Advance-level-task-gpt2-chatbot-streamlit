# =====================================================
# STEP 13: STREAMLIT CHATBOT FOR FINE-TUNED GPT-2
# =====================================================

import streamlit as st
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# -------------------------------
# Load fine-tuned model
# -------------------------------
model_path = "./gpt2-finetuned"  # Make sure this folder exists with your fine-tuned model
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

# Use GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🤖 GPT-2 Chatbot")
st.write("Chat with your fine-tuned GPT-2 model!")

# User input
user_input = st.text_input("You:", "")

if user_input:
    # Tokenize input
    inputs = tokenizer(user_input, return_tensors="pt").to(device)

    # Generate response
    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_p=0.9,
        temperature=0.8
    )

    # Decode output
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Display response
    st.text_area("GPT-2:", value=response, height=200)

import ollama
import streamlit as st
import torch
import json

# IMPORTANT to run use this command in terminal: streamlit run c:/Users/nyila/Documents/Progamming_projects/llama_translate.py

st.title("Translator AI (Beta)")

model = 'llama3.2:3b'

def translate(source_lang, target_lang, prompt):
  """Performs translation using Ollama and returns the translated text"""
  if torch.cuda.is_available():
    device = torch.device("cuda")
  else:
    device = torch.device("cpu")

  system_message = {
    'role': 'system',
    'content': f"""
    You are an expert interpreter. 
    Jour job is to accuratily translate from {source_lang} to {target_lang}

    Do not add more sentence to the translation, if you need to add something for better understanding highlight it with () as Translator comment
    """
  }

  user_message = {
      'role': 'user',
      'content': f"""
      {prompt}
      """
  }
  stream = ollama.chat(
      model=model,
      messages=[system_message, user_message],
      stream=False,
      )
  
  llm_output = json.dumps(stream['message']['content'], ensure_ascii=False)
  
  return llm_output

# Initialize session state variables
if "source_lang" not in st.session_state:
  st.session_state["source_lang"] = "English"
if "target_lang" not in st.session_state:
  st.session_state["target_lang"] = "Spanish"


# Language selection dropdown menus
source_lang = st.selectbox("From", ["English", "Spanish", "French", "German", "Italian", "Arabic", "Russian", "Chinese"], key="source_lang")
target_lang = st.selectbox("To", ["English", "Spanish", "French", "German", "Italian", "Arabic", "Russian", "Chinese"], key="target_lang")

# Text input field for user prompt
prompt = st.text_area("Enter text to translate", key="user_prompt")

st.write(f"Characters: {len(prompt)}")

# Translate button
if st.button("Translate"):
  llm_output = translate(source_lang, target_lang, prompt)
  
  st.success(f"Translation: {llm_output}")


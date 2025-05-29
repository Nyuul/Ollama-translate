Translator AI
Overview
Translator AI is a simple web application built with Streamlit and Ollama that allows users to translate text between various languages. It leverages a large language model (specifically llama3.2:3b) running via Ollama to perform accurate translations.

Features
Translate text between a selection of common languages (English, Spanish, French, German, Italian, Arabic, Russian, Chinese).

User-friendly interface for inputting text and selecting source/target languages.

Displays character count of the input text.

Utilizes GPU (if available) for faster translation processing via PyTorch.

Technologies Used
Python: The core programming language.

Streamlit: For creating the interactive web interface.

Ollama: For running the llama3.2:3b language model locally.

PyTorch: Used to check for GPU availability for accelerated inference.

JSON: For handling the LLM output.

Prerequisites
Before running this application, ensure you have the following installed:

Python 3.8+

Ollama: Download and install Ollama from https://ollama.com/.

Llama3.2:3b Model: Once Ollama is installed, download the specific model used by the application by running:

ollama run llama3.2:3b

This command will download the model if it's not already present.

Setup and Installation
Clone the repository (or save the code):
Save the provided Python code into a file named app.py (or any other .py file).

Create a virtual environment (recommended):

python -m venv venv

Activate the virtual environment:

On Windows:

.\venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

Install the required Python packages:

pip install streamlit ollama torch

How to Run the Application
Ensure Ollama is running in the background.

Navigate to the directory where you saved app.py in your terminal.

Run the Streamlit application:

streamlit run app.py

The application will open in your default web browser, usually at http://localhost:8501.

How to Use
Select Source Language: Choose the language of your input text from the "From" dropdown menu.

Select Target Language: Choose the language you want to translate to from the "To" dropdown menu.

Enter Text: Type or paste the text you wish to translate into the "Enter text to translate" text area.

Translate: Click the "Translate" button. The translated text will appear below the button.

Note:
The translation quality depends on the llama3.2:3b model and its training data.

The application will automatically detect and use a CUDA-enabled GPU if available, otherwise, it will fall back to CPU.

Translator comments will be highlighted with () in the translated text.

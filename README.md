# Language Translation Web App

This Flask web application allows users to translate English sentences to French and German using Hugging Face's Transformers library. It provides a simple user interface for language translation.

## Features

- Translate English sentences to French and German.
- Dynamically update the translation result on the same page.

## Requirements

Make sure you have the following libraries installed:

- Flask
- Transformers
- Torch
- SentencePiece

## Setting Up a Virtual Environment
It's recommended to create a virtual environment to isolate your project's dependencies. You can use the following steps to set up a virtual environment:

1. Navigate to your project directory: cd /path/to/your/project

2. Create a virtual environment (replace myenv with your preferred environment name):

```bash
python -m venv myenv

3. Activate the virtual environment:

On Windows:
```bash
myenv\Scripts\activate
```

On macOS and Linux:
```bash
source myenv/bin/activate
```

4. Install the required libraries within the virtual environment:
```bash
pip install Flask transformers torch sentencepiece
```

## Customizing Translations
You can extend this project to support additional languages by adding new translation models and updating the HTML form to include the new languages.

## Acknowledgments
This project uses the Hugging Face Transformers library for natural language processing.

## License
This project is open-source and available under the MIT License.

Happy translating!

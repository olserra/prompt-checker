# Prompt Consistency Checker

A Streamlit-based Python application designed to test the consistency of prompt generations using Langchain and the OpenAI API. This tool allows users to input generation prompts, set acceptance criteria, and specify the number of tests to run, ensuring consistent outputs from language models.

## Features

- **Prompt Generation Testing**: Test the consistency of responses from language models to specific prompts.
- **Customizable Tests**: Define your own acceptance criteria and number of iterations for testing.
- **Streamlit Interface**: Easy-to-use web interface for inputting test parameters and viewing results.
- **Langchain Integration**: Utilizes the Langchain framework with OpenAI

## Getting Started

### Prerequisites

- Python 3.6+
- Pip (Python package installer)

### Installation

1. **Clone the Repository**

```bash
git clone https://github.com/[YourUsername]/prompt-consistency-checker.git
```

```bash
cd prompt-consistency-checker
```

2. **Create a Virtual Environment (Optional but Recommended)**

```bash
python -m venv venv
```

```bash
source venv/bin/activate
```

3. **Install the dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Streamlit App**

```bash
streamlit run main.py

```

5. **Access the App**

```bash
Local URL: http://localhost:8501

```

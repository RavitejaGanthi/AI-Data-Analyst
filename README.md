# 🤖 AI Data Analyst

An AI-powered data analysis application that allows users to upload CSV datasets, automatically explore and clean data, create interactive visualizations, ask questions using natural language, and generate AI-powered business insights.

Built with **Python, Streamlit, Pandas, Plotly, and Generative AI**.

---

## 📌 Project Overview

**AI Data Analyst** is a beginner-friendly Generative AI application designed to make data analysis easier through a simple web interface.

Instead of manually writing Python code for every dataset, users can upload a CSV file and interact with the data through an intuitive Streamlit application.

The application provides:

* Dataset exploration
* Automatic data cleaning
* Interactive visualizations
* Natural-language AI questions
* AI-powered business insights
* Downloadable datasets and reports

The project demonstrates practical concepts in **Data Science, Python Development, Streamlit, Prompt Engineering, and Generative AI**.

---

## 🚀 Features

### 📂 Dataset Upload

Upload any CSV dataset directly through the application.

The application displays:

* Dataset preview
* Number of rows
* Number of columns
* Column names
* Data types
* Missing values
* Duplicate rows
* Summary statistics

---

### 🧹 Automatic Data Cleaning

The application provides basic automatic preprocessing.

It can:

* Remove duplicate rows
* Handle missing values
* Detect numerical columns
* Detect categorical columns
* Prepare the dataset for analysis

Users can also download the cleaned dataset.

---

### 📈 Interactive Visualizations

Create interactive charts from the uploaded dataset.

Supported visualizations include:

* Histogram
* Box Plot
* Scatter Plot
* Correlation Heatmap
* Bar Chart
* Pie Chart
* Line Chart

The visualization system automatically detects numerical and categorical columns.

---

### 🤖 AI Dataset Assistant

Users can ask questions about their uploaded dataset using natural language.

Example questions:

```text
Summarize this dataset.

Explain the important columns.

Which category performs best?

What are the major trends?

Are there missing values?

Which columns are correlated?

Find unusual values.

Give me business insights.

Explain this dataset like I'm a beginner.
```

The AI receives relevant information from the uploaded dataset and generates a natural-language response.

---

### 💡 Business Insights

The application can generate an AI-powered business analysis containing:

* Executive Summary
* Key Findings
* Important Trends
* Possible Problems
* Recommendations

The generated report can be downloaded as a text file.

---

### 🎨 Professional Streamlit UI

The application includes a colorful and responsive interface with:

* Custom CSS
* Gradient design
* Sidebar navigation
* Feature cards
* Styled metrics
* Interactive charts
* Responsive layout

---

## 🛠️ Technologies Used

### Programming Language

* Python 3.12+

### Frontend

* Streamlit
* CSS

### Data Analysis

* Pandas
* NumPy

### Visualization

* Plotly
* Matplotlib

### Generative AI

* Groq API
* Large Language Model (LLM)
* Prompt Engineering

### Utilities

* python-dotenv

### Version Control

* Git
* GitHub

---

## 🏗️ Project Architecture

```text
User
  │
  ▼
Streamlit Interface
  │
  ├── Upload Dataset
  │
  ▼
Data Loader
  │
  ▼
Pandas DataFrame
  │
  ├───────────────┐
  │               │
  ▼               ▼
Preprocessing   Visualization
  │               │
  │               ▼
  │           Interactive Charts
  │
  ▼
Clean Dataset
  │
  ├────────────────────┐
  │                    │
  ▼                    ▼
AI Assistant       Business Insights
  │                    │
  ▼                    ▼
Groq LLM            Groq LLM
  │                    │
  ▼                    ▼
AI Response        Business Report
```

---

## 📁 Project Structure

```text
AI-Data-Analyst/
│
├── assets/
│   └── style.css
│
├── data/
│
├── uploads/
│
├── outputs/
│
├── notebooks/
│
├── pages/
│   ├── 1_Upload_Dataset.py
│   ├── 2_Dataset_Overview.py
│   ├── 3_Visualizations.py
│   ├── 4_Ask_AI.py
│   ├── 5_Business_Insights.py
│   └── 6_About.py
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── visualization.py
│   ├── ai_assistant.py
│   ├── insights.py
│   └── utils.py
│
├── streamlit_app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
└── LICENSE
```

> `.env` should never be committed to GitHub because it contains the API key.

---

## 🔄 Application Workflow

```text
1. Start Application
        │
        ▼
2. Upload CSV Dataset
        │
        ▼
3. Explore Dataset
        │
        ▼
4. Clean Dataset
        │
        ▼
5. Create Visualizations
        │
        ▼
6. Ask Questions to AI
        │
        ▼
7. Generate Business Insights
        │
        ▼
8. Download Results
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Data-Analyst.git
```

Navigate into the project:

```bash
cd AI-Data-Analyst
```

---

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Configuration

Create a `.env` file in the project root:

```text
GROQ_API_KEY=your_groq_api_key_here
```

The application uses the API key to communicate with the Generative AI model.

### Important

Never upload `.env` to GitHub.

Your `.gitignore` should contain:

```text
.env
```

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run streamlit_app.py
```

The application will open in your browser.

---

## 🤖 Generative AI Concepts Demonstrated

This project demonstrates several important Generative AI concepts.

### 1. LLM API Integration

The application communicates with a Large Language Model through an API.

```text
Application
     │
     ▼
Dataset Information
     │
     ▼
Prompt
     │
     ▼
LLM API
     │
     ▼
AI Response
```

---

### 2. Prompt Engineering

The application constructs prompts containing relevant dataset information and the user's question.

Example:

```text
You are an AI Data Analyst.

Analyze the following dataset information.

Dataset columns:
...

Dataset statistics:
...

User question:
...

Provide a clear and beginner-friendly answer.
```

---

### 3. Context Injection

The application provides dataset context to the LLM so that the generated response is related to the uploaded data.

---

### 4. Natural Language Data Analysis

Users don't need to write Python or SQL queries for basic questions.

For example:

```text
User:
Which category has the highest sales?

        ↓

AI Data Analyst

        ↓

LLM

        ↓

Natural-language explanation
```

---

## 📊 Example Use Cases

The application can be used for datasets such as:

* Sales data
* Customer data
* Marketing data
* Financial data
* E-commerce data
* Employee data
* Education data
* Healthcare datasets
* Survey datasets

---


## 🔐 Security

The project follows basic security practices:

* API keys are stored in `.env`
* `.env` is excluded using `.gitignore`
* API keys are not hard-coded
* No database is required
* No user credentials are stored

---

## 🎯 Learning Objectives

This project was developed to gain practical experience with:

* Python
* Pandas
* Data preprocessing
* Exploratory Data Analysis
* Data visualization
* Streamlit
* Generative AI
* LLM APIs
* Prompt Engineering
* Context injection
* Git
* GitHub
* Modular Python architecture

---

## 🔮 Future Improvements

Possible future enhancements include:

* Support for Excel files
* Support for larger datasets
* Advanced statistical analysis
* Automatic chart recommendations
* SQL-based data querying
* More advanced AI agents
* Export reports as PDF
* Conversation history
* Advanced data profiling
* Deployment on Streamlit Cloud

These features are intentionally not included in the current version to keep the project simple and beginner-friendly.

---

## 📌 Project Status

**Status:** Completed 
The current version focuses on demonstrating the fundamentals of AI-powered data analysis without unnecessary enterprise-level complexity.

---

## 👨‍💻 Author

**RAVITEJA GANTHI**

Computer Science & Engineering — Data Science

Interested in:

* Data Science
* Machine Learning
* Generative AI
* Python Development
* AI Engineering

---

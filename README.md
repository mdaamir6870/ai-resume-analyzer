# AI Resume Analyzer

An AI-powered Resume Analyzer built using **Python, Generative AI, and Streamlit** to help candidates understand and improve their resumes.

## About This Project

AI Resume Analyzer is a GenAI-based application designed to compare a candidate's resume against a Job Description (JD) and provide useful insights for resume improvement.

The application is planned to use Python for development, an LLM for resume analysis, and Streamlit for the user interface.

## Project Status

🚧 **In Development**

## Setup Completed

- Project folder created
- Git repository initialized
- Python virtual environment (`.venv`) created and activated
- `.gitignore` file created and configured
- `README.md` created
- Initial Python imports and environment configuration added
- Resume text extraction logic written for PDF and DOCX files

## Technology Stack

- **Python** — Application development
- **Generative AI / LLM** — Resume analysis
- **OpenAI API** — LLM integration
- **Streamlit** — User interface
- **PyPDF** — PDF text extraction
- **python-docx** — DOCX text extraction
- **python-dotenv** — Environment variable management
- **Git & GitHub** — Version control

## Current Project Structure

```text
ai-resume-analyzer/
│
├── .venv/          # Python virtual environment
├── .gitignore      # Git ignore configuration
├── README.md       # Project documentation
└── app.py          # Main application (in development)
```

## Current Code Functionality

### 1. Environment Configuration

- Loads environment variables from `.env`
- Reads the OpenAI API key
- Configures the LLM model name

### 2. Report Sections

Defines the planned sections for the resume analysis report:

- Strengths
- Gaps
- Missing or Weak Skills
- Improvement Suggestions
- Overall Summary

### 3. Resume Text Extraction

The `extract_resume_text()` function has been written to support:

- **PDF:** Extract text from each page using PyPDF.
- **DOCX:** Extract text from document paragraphs using python-docx.
- **Text Processing:** Combine extracted content into a single string and remove leading and trailing whitespace.

*Note: The extraction code has been written; execution and testing are still pending.*

## Git Ignore Configuration

The following entries are configured in `.gitignore`:

```gitignore
.venv/
.env
__pycache__/
*.pyc
.vscode/
```

### Purpose

- `.venv/` — Local Python virtual environment
- `.env` — API keys and secret credentials
- `__pycache__/` — Python cache files
- `*.pyc` — Compiled Python files
- `.vscode/` — Local editor settings

## Security

- Store API keys in `.env`.
- Never upload `.env` or API credentials to GitHub.
- Keep the virtual environment local.

## Development Status

**Completed so far:** Initial project setup, Git initialization, environment configuration code, report section definitions, and PDF/DOCX text extraction logic.

**In progress:** Building the complete resume analysis workflow.

The LLM analysis, readable report generation, Streamlit interface, and Markdown report download are not yet implemented.


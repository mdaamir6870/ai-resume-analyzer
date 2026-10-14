# AI Resume Analyzer

An AI-powered Resume Analyzer built using **Python, Generative AI, OpenAI API, and Streamlit**. The application compares a candidate's resume with a Job Description (JD) and generates structured feedback to help improve the resume.

## Project Overview

The AI Resume Analyzer accepts a resume in PDF or DOCX format and a Job Description as input. It uses a Large Language Model (LLM) to identify matching skills, missing skills, gaps, strengths, and improvement opportunities.

## Key Features

- Upload resumes in PDF and DOCX formats.
- Extract text from uploaded resumes.
- Compare resume content against a Job Description.
- Identify candidate skills, qualifications, experience, and matching skills.
- Identify missing skills and potential gaps.
- Generate readable resume feedback using Generative AI.
- Display results through a Streamlit web interface.
- Download the final report as a Markdown (`.md`) file.
- Keep API credentials in environment variables.

## Technology Stack

- **Python** — Application development
- **Generative AI / LLM** — Resume analysis and report generation
- **OpenAI API** — Language model integration
- **Streamlit** — Web interface
- **PyPDF** — PDF text extraction
- **python-docx** — DOCX text extraction
- **python-dotenv** — Environment variable management
- **JSON** — Structured analysis and report data
- **Git & GitHub** — Version control

## Application Workflow

### Step 1: Resume Text Extraction.

The `extract_resume_text()` function reads uploaded PDF or DOCX files and converts their text into a single string for analysis.

### Step 2: Structured Resume Analysis — LLM Call #1

The `analyze_resume()` function sends the extracted resume text and Job Description to the OpenAI API. The model returns structured JSON containing:

- Candidate skills
- Candidate experience
- Candidate qualifications
- Required and preferred skills
- Matching skills
- Missing skills
- Gaps

### Step 3: Final Report Generation — LLM Call #2

The `generate_final_report()` function converts the structured analysis into readable feedback with five sections:

- Strengths
- Gaps
- Missing or Weak Skills
- Improvement Suggestions
- Overall Summary

The function also standardizes report sections into Markdown-compatible text.

### Step 4: Display and Download

The `main()` function manages the Streamlit interface, input validation, analysis workflow, error messages, and result display.

The `create_downloadable_report()` function creates a Markdown report that users can download as `resume_analysis.md`.

## Project Structure

```text
ai-resume-analyzer/
│
├── .venv/          # Python virtual environment
├── .env            # API key and model configuration
├── .gitignore      # Files excluded from Git
├── app.py          # Main application and complete workflow
├── README.md       # Project documentation
└── requirements.txt # Project dependencies (if created)
```

**Note:** `.env` and `.venv/` should remain local and must not be uploaded to GitHub.

## Setup and Installation

### 1. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install openai python-dotenv pypdf python-docx streamlit
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4o-mini
```

Replace the placeholder with your actual API key. Never share or commit your API key.

### 4. Run the application

```powershell
streamlit run app.py
```

The Streamlit application will open in your browser.

## Git Ignore Configuration

The `.gitignore` file should contain:

```gitignore
.venv/
.env
__pycache__/
*.pyc
.vscode/
```

This prevents local environment files, API credentials, Python cache files, and editor settings from being tracked by Git.

## Important Notes

- The application supports text-based PDFs and DOCX files.
- Scanned or image-only PDFs may require OCR to extract text.
- Resume feedback is based on the information provided in the resume and Job Description.
- AI-generated results should be reviewed before making career decisions.
- OpenAI API usage may incur charges depending on the model and usage.

## Project Status

**Implementation:** Complete code drafted in `app.py`.

**Testing status:** Execution and end-to-end testing are not yet confirmed.

**Future improvements:** Add automated tests, improve error handling, support OCR for scanned PDFs, and refine the user interface.

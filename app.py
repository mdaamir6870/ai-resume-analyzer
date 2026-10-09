"""
AI Resume Analyzer
==================

A small Streamlit app that compares a resume against a Job Description.

The whole workflow lives in this one file:

    Step 1  Read the uploaded resume (PDF or DOCX) as plain text
    Step 2  LLM call #1  ->  turn the resume + JD into structured JSON
    Step 3  LLM call #2  ->  turn that JSON into a readable report
    Step 4  Show the report and offer a Markdown download
"""
import os
import json
import streamlit as st
from openai import OpenAI

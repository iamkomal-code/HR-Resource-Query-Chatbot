# HR Resource Query Chatbot


##Overview

The **HR Resource Query Chatbot** is an intelligent assistant designed for HR teams to quickly identify internal talent using natural language queries.

It allows users to search for employees based on:
- Skills
- Experience
- Project history
- Availability

The chatbot processes a user's request and returns a natural language response listing the most relevant candidates.

This version uses:
- A **simple keyword matching engine**
- **FastAPI** for backend query processing
- **Streamlit** for a responsive frontend chat interface
- A **JSON dataset** representing employees with realistic attributes


## Features

-Search employees using plain English (e.g., "Who has worked on healthcare projects?")
-Employee profiles with structured data (skills, projects, experience, availability)
-FastAPI backend with live `/chat` endpoint
-Simple rule-based matcher (can be upgraded to AI later)
-Streamlit chat interface with response display
-Modular code structure 



### Component Overview

- `app/data_loader.py` → Loads `employee_data.json`
- `app/simple_chatbot.py` → Logic for matching and formatting employee data
- `app/main.py` → FastAPI app with "chat" endpoint
- `frontend/app.py` → Streamlit frontend UI
- `employee_data.json` → Employee sample dataset

# Architecture

hr-chatbot/
├── app/
│ ├── main.py # FastAPI backend
│ ├── data_loader.py # Loads employee_data.json
│ └── simple_chatbot.py # Matching & response logic
├── frontend/
│ └── app.py # Streamlit frontend
├── employee_data.json # Sample employee profiles
├── requirements.txt
└── README.md

# Future Improvements
If more time or resources were available, here’s what could be added:

Semantic search using embeddings + FAISS

GPT-4 or local LLM integration for smarter recommendations

Filters for availability, experience range, tech stacks

Conversational memory for follow-up queries

Deploy app on Streamlit Cloud, Hugging Face Spaces, or Vercel




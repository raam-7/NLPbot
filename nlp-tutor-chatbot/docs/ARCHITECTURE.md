# AI-Powered NLP Tutor Chatbot

## Overview

The AI-Powered NLP Tutor Chatbot is a Retrieval-Augmented Generation (RAG)
application that helps students learn Natural Language Processing.

The chatbot answers only NLP-related questions by retrieving information
from a local knowledge base before generating responses using a locally
running Large Language Model (Qwen 3 via Ollama).

---

# High-Level Architecture

```
                Frontend (Next.js)

                        │

                 REST API (Axios)

                        │

                  FastAPI Backend

        ┌───────────────────────────────┐
        │                               │
        │       Authentication          │
        │                               │
        ├───────────────────────────────┤
        │                               │
        │         Chat Service          │
        │                               │
        ├───────────────────────────────┤
        │                               │
        │         RAG Engine            │
        │                               │
        └───────────────────────────────┘

                │              │

                │              │

        PostgreSQL       FAISS Vector DB

                                │

                     Markdown Knowledge Base

                                │

                Sentence Transformer Embeddings

                                │

                        Ollama (Qwen 3)
```

---

# Technology Stack

## Frontend

- Next.js 16
- React
- TypeScript
- Tailwind CSS
- shadcn/ui
- Zustand
- React Query

## Backend

- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL

## AI

- Ollama
- Qwen 3
- Sentence Transformers
- FAISS

---

# Backend Structure

```
backend/

api/
core/
database/
models/
schemas/
services/
rag/
embeddings/
knowledge/
utils/
tests/
```

---

# Database

Current Tables

- users

Future Tables

- conversations
- messages
- knowledge_documents
- quiz_results
- assignments
- settings

---

# Authentication Flow

User

↓

Register

↓

Password Hashing (bcrypt)

↓

PostgreSQL

↓

Login

↓

JWT Token

↓

Protected APIs

---

# RAG Pipeline

User Question

↓

Generate Embedding

↓

FAISS Search

↓

Retrieve Top Documents

↓

Prompt Builder

↓

Qwen 3 (Ollama)

↓

Educational Response

---

# Project Goals

- Modular Architecture
- Production Ready
- Local LLM
- Retrieval-Augmented Generation
- Conversation Memory
- Expandable Knowledge Base
- Clean Code
- REST API
- Responsive UI

---

# Development Status

## Completed

- FastAPI Setup
- PostgreSQL
- SQLAlchemy
- Alembic
- User Model
- Password Hashing

## Upcoming

- JWT Authentication
- Conversation Management
- Chat APIs
- Knowledge Base
- Embeddings
- FAISS
- Ollama
- RAG
- Frontend
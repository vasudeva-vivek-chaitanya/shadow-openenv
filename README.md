# 🚀 Shadow OpenEnv

<p align="center">
  <b>A production-grade environment for simulating real-world software development workflows and evaluating AI coding agents</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-green.svg" />
  <img src="https://img.shields.io/badge/OpenEnv-Compatible-orange.svg" />
  <img src="https://img.shields.io/badge/Docker-Ready-blue.svg" />
  <img src="https://img.shields.io/badge/Status-Production--Grade-success.svg" />
</p>

---

## 📌 Overview

**Shadow OpenEnv** replicates how engineers **actually build software in production** — not just solving isolated problems, but iterating through debugging, fixing, and optimizing code.

Unlike traditional benchmarks, Shadow introduces a **stateful, iterative environment** where AI agents:

- Diagnose and fix syntax/runtime errors  
- Debug logical failures  
- Refactor inefficient implementations  
- Improve correctness across multiple iterations  

> 🎯 Goal: Enable **realistic evaluation of AI coding systems** in practical development scenarios.

---

## ⚠️ Problem Statement

Modern development workflows suffer from inefficiencies:

- Developers get **blocked due to unclear bugs or knowledge gaps**
- Leads to:
  - Increased development time  
  - Poor architectural decisions  
  - Incomplete or incorrect implementations  

### 🚫 Limitations of Current AI Assistants

Existing copilots:

- Depend heavily on **prompt engineering**
- Require **multiple re-prompts**
- Lack:
  - Execution awareness  
  - Code evolution tracking  
  - Context persistence  

Developers must repeatedly:
- Re-read generated code  
- Debug manually  
- Restart the interaction loop  

> ⚡ Result: Marginal productivity gains over traditional workflows

---

## 💡 Shadow’s Approach

Shadow introduces a **next-generation AI-assisted development paradigm**

### 🔁 Iterative Development Loop
- Agents improve code **step-by-step**, not one-shot

### 🧠 Stateful Environment
- Maintains **execution context, errors, and history**

### 💬 Conversational Debugging
- Developers interact naturally:
  - Explain problems  
  - Ask questions  
  - Receive structured guidance  

### 🔗 Workflow Alignment
- Mirrors real-world engineering cycles:
  - Write → Run → Debug → Optimize → Repeat  

---

## 📈 Key Outcomes

- ⚡ Faster development cycles  
- 🧠 Improved developer understanding  
- 🧹 Cleaner, optimized code  
- 🤖 More realistic AI evaluation  

---

## 🏗️ System Architecture

    shadow-openenv/
      │
      ├── app/
      │   ├── env.py          # Environment logic
      │   ├── grader.py       # Scoring system
      │   ├── tasks.py        # Task definitions
      │   ├── models.py       # Pydantic models
      │   ├── main.py         # FastAPI server
      │
      ├── server/
      │   └── app.py          # Entry point for deployment
      │
      ├── inference.py        # Baseline agent
      ├── baseline.py         # Rule-based runner
      ├── openenv.yaml        # OpenEnv config
      ├── pyproject.toml      # Project config
      ├── Dockerfile          # Container setup
      ├── requirements.txt    # Dependencies


    Local_setup:
      pip install -r requirements.txt
      uvicorn app.main:app --reload

    Playground:
      http://localhost:8000/docs

    Run baseline agent:
      python inference.py



    

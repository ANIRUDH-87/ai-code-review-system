---
title: AI Code Review System
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: "docker"
app_port: 7860
---

# AI Code Review System

## 📌 Description
This project is an AI-powered code review environment where an agent analyzes Python code, detects issues, and suggests improvements. It is designed as a structured evaluation system for benchmarking AI models on real-world code review tasks.

## 🎯 Motivation
Code review is a critical part of software development. Automating code analysis helps improve code quality, detect bugs early, and assist developers in writing better code efficiently.

## 🧠 Environment Design

### Observation Space
- Python code snippet
- Instruction to review the code

### Action Space
- AI-generated code review (text output)
- Identification of bugs and improvements

### Reward Function
- Correct detection → 1.0  
- Partial detection → 0.5  
- Incorrect detection → 0.0  

## 🧩 Tasks

### 🟢 Easy
- Detect syntax errors in Python code

### 🟡 Medium
- Identify logical bugs

### 🔴 Hard
- Suggest optimizations and handle edge cases

## 🚀 API Endpoints

### 🔹 /reset
- Initializes a new task  
- Returns code + instruction  

### 🔹 /step
- Accepts AI review  
- Returns:
  - reward score  
  - matched issues  
  - completion status  

### 🔹 /state
- Returns internal environment state  
- Includes:
  - code  
  - true issues  
  - task type  
  - done flag  

## ⚙️ Installation

```bash
pip install -r requirements.txt
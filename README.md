# 🗣️ Natural Language to SQL Query Engine

An intelligent database interface built with **Flask** that allows users to query databases using plain English. By leveraging Large Language Models (LLMs) alongside the **Model Context Protocol (MCP)**, this application dynamically translates natural language questions into executable SQL or NoSQL commands and returns the live data.

---

## 🎯 Project Objective

To develop an AI-powered data retrieval application that eliminates the need for users to write manual database queries. The system interprets user intent, interacts with a structured database, and visually presents the results.

---

## ⚙️ Tech Stack

* **Backend:** Python, Flask
* **Database:** MySQL (Relational) or MongoDB (NoSQL)
* **AI & Integration:** Large Language Models (LLMs), Model Context Protocol (MCP)
* **Frontend:** HTML5, CSS3 (Custom styling, no Bootstrap), JavaScript (Dynamic table rendering)

---

## 🚀 Features & Implementation

### 1. Database & Schema Setup
* **Data Initialization:** Connects to a local or cloud instance of MySQL or MongoDB, pre-populated with sample datasets for querying and testing.
* **Schema Mapping:** Exposes database schema metadata securely so the AI can understand table structures, relationships, and data types.

### 2. LLM-to-SQL Translation Engine
* **MCP Integration:** Utilizes the Model Context Protocol to bridge the gap between the LLM and the local environment, ensuring secure and context-aware query generation.
* **Natural Language Processing:** Accepts plain English questions (e.g., *"Show me all users who signed up last month"*) and generates the exact SQL or MongoDB syntax required to fetch that data.

### 3. Full-Stack Execution
* **Flask API Routing:** The backend receives the user's plain-text query, passes it through the LLM translation layer, securely executes the resulting SQL command against the database, and returns the raw data.
* **Interactive Data UI:** A clean, responsive frontend where users can type their questions in a search bar and instantly view the returned database records in a dynamically generated, easy-to-read table format.

---

## 🛠️ Local Installation & Setup

**1. Clone the repository**
```bash
git clone [https://github.com/AryanOnGitCrackingLife/NL-to-SQL-Engine.git](https://github.com/AryanOnGitCrackingLife/NL-to-SQL-Engine.git)
cd NL-to-SQL-Engine

# 🔍 AI-Powered Scam Detection Video Analyzer

This project is a **full-stack web application** designed to analyze **YouTube and Instagram videos** for potential **scams or misleading financial content**.  

It uses a **FastAPI** backend to orchestrate data collection from multiple APIs (YouTube, Supadata) and a **Llama 3 language model** to generate a **risk rating (0–5)** and detailed, explainable AI analysis.

The frontend is a **single-page HTML** app that allows users to paste a URL and instantly receive an AI-generated scam analysis.


---

## ⚙️ How It Works — The Analysis Pipeline

The system’s workflow is split between the **frontend** and **backend** components:

---

### 🖥️ Frontend (`index.html`)
1. User pastes a YouTube or Instagram URL into the text box.  
2. On clicking **“Analyze”**, a **POST** request is sent to the FastAPI server (e.g., `http://127.0.0.1:8000/youtube_ID`) with:
   ```json
   {"url": "https://example.com/video"}
## ⚡ Backend (`main.py`)

---

### 1️⃣ Data Fetching

#### 🎬 YouTube
- Uses the **Google/YouTube API** to fetch video title and description.  
- Uses the **youtube_transcript_api** to get the video transcript.

#### 📱 Instagram
- Uses the **Supadata API** to fetch the reel transcript.

---

### 2️⃣ AI Prompting

- The backend compiles all collected text into a **prompt template**.  
- Sends it to a **Llama 3 model** (via Hugging Face API).  
- The model acts as a financial analyst, returning:

```json
{
  "rating": 4,
  "reasons": ["False claims about investment returns", "No verifiable sources"],
  "sources": ["Investopedia", "SEC"]
}
```
### 3️⃣ Response

- **FastAPI** returns the model’s raw JSON string to the frontend.

---

### 4️⃣ Frontend Parsing & Display

- **JavaScript** parses the AI response using `.match()` or `JSON.parse()`.  
- The extracted data is formatted and displayed in a **“result” box** with the **risk level** and **reasons**.

---

## 🚀 Features

- 🎬 **YouTube Video Analysis:** Detects potential scams in YouTube videos.  
- 📱 **Instagram Reel Analysis:** Evaluates short videos from Instagram.  
- 🧠 **AI-Powered Insights:** Generates a 0–5 scam/risk score with reasoning and references.  
- 💻 **Simple Web Interface:** Clean, single-page app — paste a link, get results instantly.  
- 🔗 **RESTful Backend:** Built using FastAPI for scalable, asynchronous processing.

---

## 🧩 Getting Started

To run this project, set up both the **backend** and **frontend**.  
The backend setup is the most crucial step.

---

## 🔑 Prerequisites

You’ll need the following API keys:

---

### 1️⃣ Google / YouTube API Key

Used to fetch video metadata.

**Setup Steps:**
1. Go to [Google Cloud Console](https://console.cloud.google.com)  
2. Create a new project and enable **YouTube Data API v3**  
3. Generate a new **API key**

---

### 2️⃣ Supadata API Key

Used to fetch **Instagram reel transcripts**.

**Setup Steps:**
1. Sign up at [Supadata.io](https://supadata.io)  
2. Generate an **API key**

---

### 3️⃣ Hugging Face API Token

Used to call the **Llama 3 model**.

**Setup Steps:**
1. Sign up or log in at [Hugging Face](https://huggingface.co)  
2. Go to **Settings → Access Tokens** and create a new token

---

## 🧠 Backend Setup (`main.py`)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/YouCantScamMe.git
cd YOUR_REPO_NAME ```

from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import os
import requests


prompt = """You are an AI financial content analyst. Your task is to evaluate whether a given video content is **misleading or potentially a scam**, with a focus on **educational and financial claims**. 

Instructions:
1. **Analyze the transcript most carefully**. Give slightly less weight to the title and description, but include them in your reasoning.
2. Provide a **rating from 0 to 5**, where:
   - 0 = Completely useful, trustworthy content
   - 1 = Mostly trustworthy, minor exaggeration
   - 2 = Some misleading claims
   - 3 = Misleading claims present
   - 4 = Mostly misleading, potentially scammy
   - 5 = Completely misleading or a scam
3. Provide **concise bullet points** explaining why you gave this rating. Each point should be brief, clear, and specific.
4. Provide the **sources of knowledge** or references you used to make your judgment. If no external sources were consulted, state "Based on internal knowledge."

Here is the video content to analyze:

---
Title: {video_title}
Description: {video_description}
Transcript: {video_transcript}
---

Strictly give in the following format itself:
1. Score -> one line description of your rating
2. Reasoning -> list of points explaining why you gave this rating
3. Sources -> Different RELIABLE sources for the reasons

}
"""

VIDEO = input("Enter the video Link: ")
VIDEO_ID = ""

# Your YouTube Data API key
API_KEY = "AIzaSyCNwsKjsLaJul3PNWAMQzSObplPShcN36A"

i = len(VIDEO)-11

while i<len(VIDEO):
    VIDEO_ID+=VIDEO[i]
    i+=1 
    

# Set up the YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Fetch video metadata
response = youtube.videos().list(
    part="snippet",
    id=VIDEO_ID
).execute()

# Extract title and description
snippet = response['items'][0]['snippet']
title = snippet['title']
description = snippet['description']

# Fetch transcript
transc = YouTubeTranscriptApi().fetch(video_id=VIDEO_ID)
cleaned_text = " ".join([segment.text for segment in transc])

## Print results
#print("Title:", title)
#print("Description:", description)
#print("Transcript:", cleaned_text)

API_URL = "https://router.huggingface.co/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

response = query({
    "messages": [
        {
            "role": "user",
            "content": prompt + '\n' + "Title: " + title + '\n' + "Description: " + description + '\n' + "Transcript: " + cleaned_text
        }
    ],
    "model": "meta-llama/Meta-Llama-3-8B-Instruct:novita"
})

print(response["choices"][0]["message"])


#$env:HF_TOKEN = "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"







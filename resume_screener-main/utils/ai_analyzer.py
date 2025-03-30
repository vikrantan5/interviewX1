import requests

# Directly set your Gemini API key here
GEMINI_API_KEY = "AIzaSyCThrpm-bsBYuoKwHM0P4hkg7-J0PnK35A"

def analyze_resume(job_description, resume_text):
    api_url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-pro:generateContent?key={GEMINI_API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    # Correct payload structure according to Gemini API requirements
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"text": f"""
You are an AI resume screener evaluating resumes for job fit.

Job Description:
{job_description}

Resume:
{resume_text}

Provide the following:
1. ATS Score (0-100)
2. Resume Fit Score (1-10)
3. Accuracy Score (1-10)
4. Improvement Suggestions (2-3 bullet points)
"""}
                ]
            }
        ]
    }

    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            data = response.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            return f"Error decoding JSON: {e}. Response text: {response.text}"
    else:
        return f"Error: {response.status_code} {response.text}"

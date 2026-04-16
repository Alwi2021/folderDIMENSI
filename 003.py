
from google import genai

client = genai.Client(api_key="AIzaSyDtFtmVUaPlqMJaUw1funakiu3zHW22tBE")

# Gunakan model gemini-2.0-flash atau gemini-1.5-flash
response = client.models.generate_content(
    model="gemini-2.0-flash", 
    contents="Jelaskan cara kerja AI dalam beberapa kata"
)

print(response.text)




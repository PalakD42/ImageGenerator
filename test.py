import requests

try:
    response = requests.get("https://huggingface.co", timeout=10)
    print("Hugging Face status:", response.status_code)

    response = requests.get("https://api-inference.huggingface.co", timeout=10)
    print("API status:", response.status_code)

except Exception as e:
    print("Error:", e)
# 🖼️ AI Image Generator

A Flask-based web application that generates AI images from text prompts using the Hugging Face Inference API and Stable Diffusion 3 Medium.

---

## ✨ Features

* 🎨 Generate images from text prompts
* 🤖 Powered by Stable Diffusion 3 Medium
* ⚡ Fast and simple Flask backend
* 🔒 Secure API key management using `.env`
* 🌐 Clean web interface

---

## 🛠️ Tech Stack

* Python
* Flask
* HTML/CSS
* Hugging Face Inference API
* Stable Diffusion 3 Medium
* Requests
* python-dotenv

---

## 📁 Project Structure

```text
ImageGenerator/
│── templates/
│   └── index.html
│── app.py
│── requirements.txt
│── .gitignore
│── README.md
└── .env (not included)
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/PalakD42/ImageGenerator.git
cd ImageGenerator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```env
HF_API_KEY=your_huggingface_api_key
```

### 4. Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🧠 Model Used

* Stable Diffusion 3 Medium
* Accessed through the Hugging Face Inference API

---

## 📸 Screenshots

### Home Page

![Home Page](screenshots/home.png)

### Generating Image

![Generating](screenshots/generating.png)

### Generated Image

![Result](screenshots/result.png)

---

## 🔮 Future Improvements

* Download generated images
* Image history
* Multiple image generation
* Prompt enhancement
* Dark mode
* User authentication

---

## 👩‍💻 Author

**Palak**

GitHub: https://github.com/PalakD42

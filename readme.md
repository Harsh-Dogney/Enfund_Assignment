
```markdown
# 🚀 Enfund Assignment

Welcome to the **Enfund Assignment** repository! This project is a full-stack web application built with **Django** that features:

- 🔐 Google OAuth 2.0 Authentication
- 📂 Google Drive Integration (Picker API + Drive API)
- 💬 Real-time WebSocket Chat
- 🧑‍🤝‍🧑 One-to-One Private Messaging

---

## 🧠 Overview

This application is designed to showcase integration with **Google APIs** for file management and implement real-time communication using **WebSockets**. It demonstrates practical use of third-party APIs, authentication mechanisms, and interactive frontend/backend sync using Django Channels.

---

## 🌐 Features

### ✅ Google OAuth 2.0
- Secure login with your Google account
- Authenticated user session management

### 📁 Google Drive Integration
- Pick files from your Google Drive using **Google Picker API**
- List your Drive files within the app
- Download files directly via the app interface

### 💬 Real-Time Chat
- Global group chat room
- Sidebar listing all users
- Initiate one-on-one private messaging
- WebSocket-based real-time communication

---

## 🏗️ Tech Stack

| Technology | Description |
|------------|-------------|
| **Django** | Backend web framework |
| **Django Channels** | WebSocket support for real-time communication |
| **Google APIs** | OAuth 2.0, Picker API, Drive API |
| **HTML/CSS/JS** | Frontend UI |
| **WebSockets** | Real-time messaging |


---

## 🚀 Getting Started

### 📦 Clone the Repository

```bash
git clone https://github.com/Harsh-Dogney/Enfund_Assignment.git
cd Enfund_Assignment
```

### 🛠️ Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### ⚙️ Environment Setup

Create a `.env` file in the root directory with the following:

```env
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
SECRET_KEY=your_django_secret_key
DEBUG=True
```

Make sure your Google Cloud Console has:
- OAuth Consent Screen enabled
- Picker API & Drive API enabled
- Redirect URI set to: `http://localhost:8000/auth/complete/google-oauth2/`

### 💻 Run the App

```bash
python manage.py migrate
python manage.py runserver
```

Visit: [http://localhost:8000](http://localhost:8000)

---

## 🗂️ Project Structure

```
Enfund_Assignment/
├── auth_test/          # Handles Google OAuth logic
├── chat/               # Real-time chat app (channels, consumers, models)
├── templates/          # HTML templates
│   ├── auth_test/
│   └── chat/
├── static/             # Static files (JS, CSS)
├── manage.py
└── requirements.txt
```

---

## 🔐 Google Picker Integration Guide

To use Google Picker:
1. Log in using Google
2. Click **"Upload to Drive"** or **"Select File"**
3. Picker UI will open → choose file → upload/download automatically handled
4. Files are also listed on the "Drive Files" page using the Drive API

---

## 💬 Chat Instructions

1. Go to `/chat/`
2. Use the **sidebar** to select users for one-on-one chat
3. Messages appear in real time using Django Channels (WebSockets)

---

## 🧪 Testing

>  Postman collection available for reference 

---

## 🙌 Acknowledgements

- [Google Developer Console](https://console.cloud.google.com/)
- [Django Channels Docs](https://channels.readthedocs.io/)
- [Google Picker API Guide](https://developers.google.com/picker)


# 💬 Flutter + FastAPI Real-Time Chat App

A simple and efficient real-time chat application built using **Flutter** for the frontend and **FastAPI** for the backend via **WebSocket communication**.

---

## 🚀 Features

* 🔁 Real-time messaging via WebSockets
* 👤 User joins by entering a name
* 📩 Message broadcasting to all connected clients
* 🧭 Differentiated UI for sender and receiver
* 🕒 Timestamps on each message
* 💡 Built with simplicity & scalability in mind

---

## 🛠️ Tech Stack

| Layer    | Technology       |
| -------- | ---------------- |
| Frontend | Flutter          |
| Backend  | FastAPI (Python) |
| Protocol | WebSockets       |

---

## 📦 Project Structure

```
├── backend/
│   └── main.py              # FastAPI server with WebSocket endpoint
│
├── frontend/
│   ├── lib/
│   │   ├── chatScreen.dart  # Chat UI and socket logic
│   │   └── userScreen.dart  # User name input screen
│   └── pubspec.yaml         # Flutter dependencies
```

---

## ▶️ Getting Started

### Backend (FastAPI)

```bash
cd backend
pip install fastapi uvicorn
uvicorn main:app --reload --host 0.0.0.0 --port 8080
```

### Frontend (Flutter)

```bash
cd frontend
flutter pub get
flutter run
```

---

## 🧪 Sample Chat Flow

1. User opens app and enters a name.
2. App connects to FastAPI server using WebSocket.
3. Messages are sent in the format: `username: message`.
4. Server receives & broadcasts message to all connected users.
5. Messages are shown in chat UI with timestamp.

---

## 🧱 Built With

* ❤️ Flutter (Dart)
* ⚡ FastAPI (Python)
* 🔗 WebSocket Protocol

---

## 📌 Future Improvements

* 💾 Message persistence (File/Database)
* 🔐 Authentication system
* 📱 Responsive Web App version
* 🧑‍🤝‍🧑 Group chats or private rooms
* 🐳 Docker support

---

## 📃 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

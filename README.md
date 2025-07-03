# 📁 Secure File Sharing System (Flask + MongoDB)

A secure backend file-sharing system between two user types: **Ops User** and **Client User**. This project provides REST APIs for uploading, downloading, and managing secure files.

---

## 🔧 Tech Stack

- Python (Flask)
- MongoDB (via PyMongo)
- JWT (Authentication)
- Flask-CORS
- Itsdangerous (for encrypted download URLs)
- Thunder Client / Postman for API testing

---

## 🚀 API Features

### 👨‍💼 Ops User
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/auth/login` | POST | Login for Ops |
| `/ops/upload` | POST | Upload file (`.pptx`, `.docx`, `.xlsx`) |

### 👨‍💻 Client User
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/client/signup` | POST | Signup (returns encrypted URL) |
| `/client/verify/<token>` | GET | Verify email |
| `/auth/login` | POST | Login |
| `/client/files` | GET | List all uploaded files |
| `/client/download-link/<filename>` | GET | Get encrypted download link |
| `/client/download/<token>` | GET | Download file securely |

---

## ✅ Setup Instructions (Local)

```bash
# 1. Clone repo and navigate into it
git clone <repo_url>
cd secure_file_sharing

# 2. Create virtual environment and install dependencies
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# 3. Start MongoDB locally
mongod

# 4. Set up environment variables in .env file
MONGO_URI=mongodb://localhost:27017/filesharedb
JWT_SECRET=your_jwt_secret

# 5. Run the server
python run.py
```

---

## 🧪 Postman Collection

Use the provided `SecureFileSharing.postman_collection.json` to test all endpoints. Import it into Postman or Thunder Client.

---

## 🧪 Test Cases (Examples)

1. ✅ Valid login as ops and client (assert JWT is returned)
2. ❌ Invalid login (wrong email/password)
3. ✅ Ops uploads valid file format
4. ❌ Ops uploads invalid file format (e.g. `.exe`)
5. ✅ Client generates download link
6. ❌ Client tries to use expired or wrong token
7. ❌ Ops tries to download using client’s link (access denied)

More test cases can be written using `pytest` and `Flask-Testing`.

---

## ☁️ Production Deployment Plan

1. Use **Docker** to containerize the app
2. Use **MongoDB Atlas** for a managed NoSQL DB
3. Host backend on **Render**, **Heroku**, or **AWS EC2**
4. Configure HTTPS using **Nginx** reverse proxy or use **Gunicorn + SSL**
5. Use **environment variables** securely with `.env` and secret managers
6. Enable logging, request rate limiting, and CORS configuration
7. Set `debug=False` and apply production WSGI server (like Gunicorn)

---

## 📂 Folder Structure

```
secure_file_sharing/
├── app/
│   ├── routes/
│   ├── __init__.py
├── uploads/
├── run.py
├── .env
├── requirements.txt
├── README.md
```

---

## 📬 Contact

Made with ❤️ for backend internships.
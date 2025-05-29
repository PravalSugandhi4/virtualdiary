# 🖋️ Virtual Diary

**Virtual Diary** is a secure, personal digital space for users to journal their thoughts, emotions, and daily experiences. Built with Django (backend) and HTML/CSS (frontend), this web app offers privacy, intuitive writing features, and session security using CSRF protection. Admin control ensures only active users can log in and stay logged in.

---

## 🚀 Features

- 📝 Write, edit, and delete diary entries
- 🔐 Secure login with CSRF token protection
- ☁️ Cloud-based journaling – access anytime, anywhere
- 🔎 Search and filter entries by date or keyword
- 👤 Admin-controlled user access
- 💡 Auto logout of inactive users if marked inactive by admin

---

## ⚙️ Functionality: Admin-Inactive Account Handling

- Admins can mark user accounts as **inactive** (`is_active = False`).
- If a user is marked **inactive**:
  - ❌ They will be **unable to log in**.
  - ⚠️ If already logged in, they will be **automatically logged out** on the next request (middleware-based check).
- This ensures tight control over account access for privacy and security.

---

## 🛠️ Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS
- **Security:** Django’s built-in CSRF protection, session management

---



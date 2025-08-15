# 📰 Daily News Email Automation — Python

A lightweight Python automation script that **fetches daily news via an API** and **emails it to subscribers automatically**.  
Showcases my skills in:
- **Requests** (API data fetching)
- **SMTP & SSL** (secure email delivery)
- **Automation scripting** in Python

---

## 🚀 Features
- Fetches the latest news headlines from a public API
- Sends a daily email digest to multiple recipients
- Secure email sending with SSL encryption
- Customizable email subject and format
- Lightweight and easy to set up

---

## 📦 Installation
Make sure you have **Python 3.8+** installed.

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/daily-news-email.git
cd daily-news-email
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration
1. **Get a News API Key**  
   - Sign up at [NewsAPI.org](https://newsapi.org/) (or any other news provider)
   - Copy your API key.

2. **Update the configuration file or script variables**  
   - `NEWS_API_KEY` — Your API key
   - `SMTP_SERVER`, `SMTP_PORT` — Email server details
   - `SENDER_EMAIL`, `SENDER_PASSWORD` — Email account credentials
   - `RECIPIENTS` — List of recipients

---

## 🖥 Usage
Run the script manually:
```bash
python daily_news_email.py
```

Or schedule it daily with **cron (Linux/Mac)** or **Task Scheduler (Windows)** for automation.

---

## 📂 File Structure
```
📁 daily-news-email
 ├── daily_news_email.py  # Main script
 ├── requirements.txt     # Dependencies
 ├── README.md            # Documentation
 └── config.json          # Optional config file
```

---

## 🧰 Dependencies
- **requests** — For fetching data from the news API
- **smtplib** — For sending emails
- **ssl** — For secure email delivery
- **json** (built-in) — For data handling

Install them all:
```bash
pip install -r requirements.txt
```

---

## 💡 How It Works
1. **Fetch News** → Uses `requests` to retrieve the latest headlines.
2. **Format Email** → Creates a clean, readable news digest.
3. **Send Securely** → Uses `smtplib` + `ssl` to send the email to all recipients.

---

## 📜 License
Licensed under the MIT License — free to use and modify.

---

## ⭐ Show Your Support
If you find this project useful, give it a ⭐ on GitHub!

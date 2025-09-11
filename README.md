# 🌍 World of Games

A Flask-based web application featuring three mini-games:  
- **Memory Game** – test your memory by recalling sequences.  
- **Guess Game** – guess a number within the given range.  
- **Currency Roulette** – guess the value of USD in ILS based on real-time rates.  

The app is containerized with **Docker**, deployable with **Ansible**, and has a **Jenkins CI/CD pipeline**.  
It also integrates with **ELK Stack** for logging.

---

## 🚀 Features
- Flask backend with session-based gameplay
- Three mini-games available from the homepage
- Logging to Logstash for centralized monitoring
- Dockerized for easy deployment
- Jenkins pipeline with health checks
- Ready for Ansible automation

---

## 🛠️ Requirements
- Python 3.9+  
- Docker & Docker Compose  
- Jenkins (for CI/CD)  
- ELK Stack (optional, for logs)

---

## 🏗️ Setup & Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/world-of-games.git
cd world-of-games

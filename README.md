# 🏥 Lazarus Medical Recovery System

## 🚨 Problem Statement
In the event of a ransomware attack, hospital databases can become corrupted, leading to:
- Broken patient identities  
- Encrypted medical records  
- Missing or inconsistent vital data  

This creates serious risks, as doctors rely on accurate data for life-saving decisions.

---

## 💡 Our Solution
We developed a **data reconstruction system** that restores corrupted hospital data by:
- Decoding encrypted values  
- Rebuilding patient identities  
- Filling missing data intelligently  
- Detecting critical health conditions  

---

## ⚙️ How It Works

### 🔹 1. Data Cleaning
- Handles incomplete and inconsistent records  
- Replaces missing oxygen values with safe defaults  

### 🔹 2. Data Decoding
- Converts hexadecimal BPM values into readable numbers  
- Decrypts medicine names using Caesar cipher logic  

### 🔹 3. Identity Reconstruction
- Assigns patient wards based on ID parity (even/odd logic)  

### 🔹 4. Alert System 🚨
- Detects abnormal BPM (<60 or >100)  
- Highlights critical patients in real-time  

---

## 🖥️ Features
- 👤 Patient Identity Cards  
- ❤️ Real-time BPM Monitoring  
- 🫁 Oxygen Level Tracking  
- 💊 Medicine Decryption Panel  
- 🚨 Critical Alert System  
- 🎨 Interactive Dashboard UI  

---

## 🧠 Tech Stack
- **Backend:** Python  
- **Framework:** Flask  
- **Frontend:** HTML, CSS  
- **Logic Used:** Data Cleaning, Cipher Decoding, Rule-based Alerts  

---

## 📊 Sample Data Processing

| Raw Data | Processed Output |
|--------|----------------|
| BPM: 0x5A | BPM: 90 |
| Medicine: khoor | Medicine: hello |
| Oxygen: null | Oxygen: 95 |

---

## ▶️ How to Run the Project

```bash
pip install flask
python app.py

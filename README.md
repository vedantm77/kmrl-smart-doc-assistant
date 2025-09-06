# 🚇 Kochi Metro Smart Document Assistant

## 📌 Problem
Kochi Metro Rail Limited (KMRL) generates **thousands of documents daily**: engineering drawings, safety reports, HR policies, invoices, and more.  
Currently, this leads to:
- ⏳ Hours wasted skimming long documents
- 🏢 Departments working in silos
- ⚠️ Risk of missing regulatory updates
- 📉 Loss of knowledge when employees retire/transfer
- 🔄 Duplicate manual effort in making summaries

---

## 💡 Solution
An **AI-powered Smart Document Assistant** that:
- 📑 Uploads & analyzes documents (PDF, Word, Images, Scans)
- 🧠 Generates **automatic summaries** with key action points
- 🏷️ Classifies documents into categories (Safety, HR, Finance, Engineering, Legal)
- 🌐 Supports **English + Malayalam**
- 🔍 Provides **searchable knowledge base**
- 🔗 Maintains traceability to original documents

---

## 🛠️ Tech Stack
- **Frontend:** Streamlit (Python)
- **NLP Models:** HuggingFace Transformers (Summarization, Classification, Translation)
- **OCR:** PyTesseract (for scanned docs/images)
- **PDF Processing:** PyPDF2
- **Search (Future):** FAISS / Vector DB
- **Deployment:** Streamlit Cloud

---

## 📂 Repository Structure
```
kmrl-smart-doc-assistant/
│── app.py # Streamlit frontend
│── requirements.txt # Dependencies
│── README.md # Documentation
│── sample_docs/ # Example documents for testing
│── assets/ # Screenshots & mockups
│── backend/ # (Optional) AI processing scripts
```

---

## 🚀 How to Run Locally
1. Clone the repo:
   ```bash
   git clone https://github.com/vedantm77/kmrl-smart-doc-assistant.git
   cd kmrl-smart-doc-assistant
2. Install dependencies:
   pip install -r requirements.txt
3. Run the app:
   streamlit run app.py
4. Open in browser:
👉 http://localhost:8501
8501

## 🌍 Deployment

We deployed on Streamlit Cloud:

Push code to GitHub.

Go to Streamlit Cloud
.

Connect repo → Deploy.

Get a public link to share with judges 🚀

## 👥 Team Roles

Frontend (UI/UX): Vedant

Backend (AI Models): Teammate A

Integration & DB: Teammate B

Documentation & Presentation: Teammate C

## 📌 Future Roadmap

Integration with Email, SharePoint, WhatsApp PDFs

Multilingual support (beyond English/Malayalam)

Role-based dashboards (Engineering, HR, Finance, Safety)

AI-powered chatbot for querying past documents

🏆 Built for Smart India Hackathon 2025

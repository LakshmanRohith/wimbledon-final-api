# 🎾 Wimbledon Final Info API

This project is a RESTful API built using **FastAPI** that provides historical information about **Wimbledon Men's Singles Finals** based on the year provided.

It also includes a simple frontend (HTML + JavaScript) to interact with the API.

---

## 📂 Project Structure

wimbledon_api/
├── main.py # FastAPI backend
├── data.py # Match data (dictionary)
├── templates/
│ └── index.html # Frontend page
├── static/ # (Optional) for CSS/JS files
├── requirements.txt # Python dependencies
└── README.md


---

## 🧪 Example API Response

**Request:**

GET /wimbledon?year=2021

**Response:**
json
{
  "year": 2021,
  "champion": "Novak Djokovic",
  "runner_up": "Matteo Berrettini",
  "score": "6–7(4–7), 6–4, 6–4, 6–3",
  "sets": 4,
  "tiebreak": true
}
🛠 Tech Stack
Python 3.9

FastAPI

HTML + JavaScript (Frontend)

Uvicorn (ASGI server)


📥 Installation
1. Clone the repository
bash
git clone https://github.com/YOUR_USERNAME/wimbledon-final-api.git
cd wimbledon-final-api

2. Create and activate virtual environment
bash
conda create -n wimbledonapi python=3.9
conda activate wimbledonapi

3. Install dependencies
bash
pip install -r requirements.txt
4. Run the FastAPI server
bash
uvicorn main:app --reload

💡 Usage
Open the frontend (index.html) or visit http://127.0.0.1:8000

Enter a year in the input field (e.g., 2021) and click "Get Details"

The backend will return Wimbledon final match details for that year






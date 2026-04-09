🎬 Movie Recommendation System

A simple and practical Streamlit web app that recommends similar movies based on a selected movie title.

🔗 Live Demo:
👉 https://movie-recommendation-system-nspu.onrender.com

📌 Overview

This project uses precomputed similarity scores between movies to deliver fast and relevant recommendations in real time.
The user interface is built using Streamlit, and model artifacts are loaded from local serialized files.

✨ Features
🎯 Interactive movie selection via dropdown
⚡ Fast recommendations using precomputed similarity matrix
🧼 Clean and minimal Streamlit UI
🚀 Deployed and accessible online
💻 Easy local setup
🛠️ Tech Stack
Python
Streamlit
Pandas
Scikit-learn
Joblib
Pickle
📁 Project Structure
Movie_Recommendation_System/
├── app.py               # Streamlit application
├── movies.pickle        # Movie metadata/features
├── similarity.joblib    # Precomputed similarity matrix
├── requirements.txt     # Python dependencies
└── README.md
⚙️ How It Works
Load movie data from movies.pickle
Load similarity matrix from similarity.joblib
User selects a movie from dropdown
On clicking Recommend:
Find the movie index
Compute similarity scores
Return top 5 similar movies
🚀 Installation

Clone the repository:

git clone https://github.com/dharmender12/Movie-Recommendation-System.git
cd Movie-Recommendation-System

Create a virtual environment:

python -m venv .venv
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt
▶️ Run Locally
streamlit run app.py

Open in browser:
👉 http://localhost:8501

🌐 Deployment

This project is deployed and accessible online:
👉 https://movie-recommendation-system-nspu.onrender.com

📝 Notes
Ensure movies.pickle and similarity.joblib are in the same directory as app.py
Currently returns top 5 recommendations per movie
🔮 Future Improvements
🎥 Add movie posters and details
🔍 Implement search with autocomplete
🌍 Integrate TMDB API for richer recommendations
☁️ Deploy on Streamlit Community Cloud

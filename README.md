# Movie Recommendation System

A simple and practical Streamlit web app that recommends similar movies based on a selected movie title.

## Overview

This project uses precomputed similarity scores between movies to return top recommendations in real time.
The UI is built with Streamlit, and the model artifacts are loaded from local files.

## Features

- Interactive movie selection with a dropdown input
- Fast recommendation results using a precomputed similarity matrix
- Clean and minimal Streamlit interface
- Ready-to-run local setup

## Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- Joblib
- Pickle

## Project Structure

```
Movie_Recommendation_System/
├── app.py               # Streamlit application
├── movies.pickle        # Movie metadata/features
├── similarity.joblib    # Precomputed movie-to-movie similarity matrix
├── requirements.txt     # Python dependencies
└── README.md
```

## How It Works

1. The app loads movie data from `movies.pickle`.
2. It loads a similarity matrix from `similarity.joblib`.
3. A user selects a movie title from the dropdown.
4. On clicking **Recommend**, the app finds the selected movie index.
5. It ranks similarity scores and returns the top 5 similar movies.

## Installation

Clone the repository and move into the project directory:

```bash
git clone https://github.com/dharmender12/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

Start the Streamlit server:

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal (usually `http://localhost:8501`).

## Notes

- Ensure `movies.pickle` and `similarity.joblib` are present in the same folder as `app.py`.
- The app currently returns 5 recommendations for every selected movie.

## Future Improvements

- Add movie posters and metadata in the UI
- Add search input with autocomplete
- Use TMDB API for richer recommendations
- Deploy online with Streamlit Community Cloud

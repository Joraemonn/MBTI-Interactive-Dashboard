# MBTI Interactive Dashboard

A Streamlit dashboard for exploring MBTI personality distributions, career fields,
job satisfaction, and fictional characters associated with personality types.
Created for ICT 305 Data Visualization.

## Run locally on Windows

Requires Python 3.11. From this repository's directory, open PowerShell and run:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run home_pagev5.py
```

Open http://localhost:8501 in your browser. Keep the terminal running and use
Ctrl+C to stop the app.

## Pages

- Home: introduction and animated space characters.
- About: MBTI concepts and an overview of the dashboard.
- Explore: interactive charts of personality types, jobs, and satisfaction.
- Find Out More: fictional characters and personality resources.

`home_pagev5.py` is the main entrypoint and shared navigation. The homepage
content is in `home_content.py`, and the other pages are in `pages/`.
The current dashboard uses `cleaned_kpmi_data.csv` and bundled image/animation
assets. Older prototypes and analysis notebooks are retained for reference;
they may need additional dependencies beyond the current app's requirements.

An internet connection is needed for hosted fonts and the Lottie animation player.
The virtual environment and local secrets are excluded from Git.

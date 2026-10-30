# 🌦️ Weather App

A Python-based weather application built with **Streamlit** and the **OpenWeatherMap API**. The application allows users to retrieve current weather information by entering a city name.

## Features

- Search for current weather by city.
- Retrieve real-time weather information through the OpenWeatherMap API.
- Display weather conditions and temperature.
- Present weather information through an interactive Streamlit interface.
- Secure API key configuration using environment variables.

## Technologies Used

- Python
- Streamlit
- Requests
- OpenWeatherMap API

## Project Structure

```text
python-for-ai/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/KE2541/python-for-ai.git
cd python-for-ai
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the API key

Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).

In PowerShell:

```powershell
$env:OPENWEATHER_API_KEY="YOUR_API_KEY"
```

Replace `YOUR_API_KEY` with your actual API key.

### 5. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser, usually at:

`http://localhost:8501`

## Security

The OpenWeatherMap API key is configured through an environment variable rather than being hardcoded in the application.

Never commit API keys, passwords, or other credentials to a public repository.

## Future Improvements

- Add multi-day weather forecasts.
- Include weather icons and improved visual presentation.
- Add temperature unit conversion.
- Improve error handling for invalid city names and API failures.
- Deploy the application using Streamlit Community Cloud.

## Author

**KE2541**

GitHub: [https://github.com/KE2541](https://github.com/KE2541)

*Developed as a practical Python application integrating a third-party API with an interactive web interface.*

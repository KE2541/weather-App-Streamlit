# 🌦️ Weather App – Streamlit

A Python-based weather application built with **Streamlit** and the **OpenWeatherMap API**. It provides current weather conditions and a five-day forecast through an interactive web interface.

**Live Application:** [Weather App](https://weather-app-app-hxynmmbnsfhqpmtnq75zmq.streamlit.app/)

## Features

- **City Search:** Retrieve weather information by entering a city name.
- **Current Weather:** Display temperature, feels-like temperature, humidity, atmospheric pressure and wind speed.
- **Five-Day Forecast:** View upcoming weather conditions, including daily minimum and maximum temperatures.
- **Weather Icons:** Visual representation of weather conditions.
- **Temperature Conversion:** Switch between Celsius and Fahrenheit.
- **Error Handling:** Handle invalid city names, API errors and network connection issues.
- **Responsive Interface:** Streamlit-based interface designed to work across different screen sizes.
- **Secure API Configuration:** Retrieve API credentials through environment variables or Streamlit Secrets.

## Technologies Used

- **Python** – Application logic and API integration.
- **Streamlit** – Interactive web application framework.
- **Requests** – HTTP requests and API communication.
- **OpenWeatherMap API** – Weather data and forecast services.
- **Git and GitHub** – Source code management and version control.
- **Streamlit Community Cloud** – Application deployment.

## Project Structure

```text
weather-App-Streamlit/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```powershell
git clone https://github.com/KE2541/weather-App-Streamlit.git

cd weather-App-Streamlit
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Configure the OpenWeatherMap API key

Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).

For local development using PowerShell:

```powershell
$env:OPENWEATHER_API_KEY="YOUR_API_KEY"
```

Replace `YOUR_API_KEY` with your actual API key.

For Streamlit Community Cloud deployment, configure the key under **App Settings → Secrets**:

```toml
OPENWEATHER_API_KEY = "YOUR_API_KEY"
```

Never hardcode API credentials or commit secrets to GitHub.

### 5. Run the application

```powershell
python -m streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## Deployment

The application is deployed using Streamlit Community Cloud.

Access the live application:

[https://weather-app-app-hxynmmbnsfhqpmtnq75zmq.streamlit.app/](https://weather-app-app-hxynmmbnsfhqpmtnq75zmq.streamlit.app/)

## Security

The application uses environment variables for local API key configuration and Streamlit Secrets for cloud deployment.

API credentials should never be hardcoded into source files or committed to a public repository.

## Future Improvements

- Add location-based weather detection.
- Introduce weather data caching to improve efficiency.
- Expand weather visualizations and historical weather trends.
- Add automated application testing.

## Author

**KE2541**

GitHub: [https://github.com/KE2541](https://github.com/KE2541)

*Developed as a practical Python project demonstrating third-party API integration, application development, error handling, secure configuration and cloud deployment.*practical Python application integrating a third-party API with an interactive web interface.*

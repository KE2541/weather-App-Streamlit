# 🌦️ Weather App – Streamlit

A Python-based weather application built with **Streamlit** and the **OpenWeatherMap API**. The application allows users to retrieve and view current weather information for a selected city through a simple web interface.

**Live Application:** [Launch Weather App](https://weather-app-app-hxynmmbnsfhqpmtnq75zmq.streamlit.app/)

## Features

- Search for weather information by city.
- Retrieve current weather data using the OpenWeatherMap API.
- Display weather information through a Streamlit interface.
- Handle API responses and invalid requests.
- Secure API key configuration using environment variables or Streamlit secrets.

## Technologies Used

- **Python** – Application development and API integration.
- **Streamlit** – Web application framework and user interface.
- **Requests** – HTTP requests to the OpenWeatherMap API.
- **OpenWeatherMap API** – Weather data provider.
- **Git and GitHub** – Version control and source code management.
- **Streamlit Community Cloud** – Application hosting and deployment.

## Project Structure

```text
weather-App-Streamlit/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

Follow these instructions to run the application locally.

### 1. Clone the repository

```powershell
git clone https://github.com/KE2541/weather-App-Streamlit.git
```

### 2. Navigate to the project directory

```powershell
cd weather-App-Streamlit
```

### 3. Create a virtual environment

```powershell
python -m venv .venv
```

### 4. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

## API Key Configuration

The application requires an API key from [OpenWeatherMap](https://openweathermap.org/api).

For local development, set the API key as an environment variable in PowerShell:

```powershell
$env:OPENWEATHER_API_KEY="YOUR_API_KEY"
```

For Streamlit Community Cloud deployment, configure the key under the application's **Settings → Secrets**:

```toml
OPENWEATHER_API_KEY = "YOUR_API_KEY"
```

**Security note:** Never hardcode API credentials in your source code or commit `.env` files or `secrets.toml` containing actual credentials to GitHub.

## Run the Application

Start the application using:

```powershell
python -m streamlit run app.py
```

Streamlit will make the application available locally at:

`http://localhost:8501`

## Deployment

The application is deployed using **Streamlit Community Cloud** and is accessible through the following link:

[https://weather-app-app-hxynmmbnsfhqpmtnq75zmq.streamlit.app/](https://weather-app-app-hxynmmbnsfhqpmtnq75zmq.streamlit.app/)

## Skills Demonstrated

This project demonstrates practical experience with:

- Python application development.
- REST API integration and HTTP requests.
- JSON-based API response handling.
- Environment variable and application secret management.
- Dependency management using `pip` and `requirements.txt`.
- Git-based version control and GitHub repository management.
- Deployment of Python applications using Streamlit Community Cloud.

## Future Improvements

Potential enhancements include:

- Five-day weather forecasting.
- Celsius and Fahrenheit temperature conversion.
- Weather trend visualizations.
- Location-based weather detection.
- API response caching.
- Automated application testing.

## Author

**KE2541**

Developed as a practical Python and Streamlit project demonstrating API integration, application development, and cloud deployment.

GitHub: [https://github.com/KE2541](https://github.com/KE2541)

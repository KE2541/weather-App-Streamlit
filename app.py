
import os
import requests
import streamlit as st

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Weather App",
    page_icon="🌦️",
    layout="centered"
)

# --------------------------------------------------
# Application styling
# --------------------------------------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #eaf4ff, #ffffff);
    }

    .weather-card {
        background: rgba(255, 255, 255, 0.95);
        padding: 22px;
        border-radius: 16px;
        border: 1px solid #d6e5f5;
        text-align: center;
        margin-bottom: 12px;
    }

    .temperature {
        font-size: 48px;
        font-weight: 700;
        color: #155eaa;
    }

    .metric {
        font-size: 24px;
        font-weight: 600;
        color: #155eaa;
    }

    .muted {
        color: #526579;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("🌦️ Weather App")
st.write("Check current weather conditions for any city.")

# Read API key from environment or Streamlit secrets.
api_key = os.getenv("OPENWEATHER_API_KEY")

if not api_key:
    try:
        api_key = st.secrets.get("OPENWEATHER_API_KEY", "")
    except Exception:
        api_key = ""

if not api_key:
    st.error(
        "Weather API key is not configured. "
        "Set OPENWEATHER_API_KEY before using the app."
    )
    st.stop()

# --------------------------------------------------
# City search
# --------------------------------------------------
with st.form("weather_search"):
    city = st.text_input(
        "Enter a city name",
        placeholder="e.g. Nairobi, London or Tokyo"
    )

    submitted = st.form_submit_button(
        "🔍 Get Weather",
        use_container_width=True
    )

# --------------------------------------------------
# Retrieve and display weather
# --------------------------------------------------
if submitted:
    city = city.strip()

    if not city:
        st.warning("Please enter a city name.")

    else:
        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }

        try:
            with st.spinner("Retrieving weather information..."):
                response = requests.get(
                    url,
                    params=params,
                    timeout=15
                )

            if response.status_code == 200:
                weather = response.json()

                city_name = weather["name"]
                country = weather["sys"]["country"]
                temperature = weather["main"]["temp"]
                feels_like = weather["main"]["feels_like"]
                humidity = weather["main"]["humidity"]
                pressure = weather["main"]["pressure"]
                wind_speed = weather["wind"]["speed"] * 3.6

                description = weather["weather"][0]["description"]
                icon_code = weather["weather"][0]["icon"]

                st.markdown("---")
                st.subheader(f"📍 {city_name}, {country}")

                icon_url = (
                    f"https://openweathermap.org/img/wn/"
                    f"{icon_code}@2x.png"
                )

                left, right = st.columns([1, 2])

                with left:
                    st.image(icon_url, width=110)

                with right:
                    st.markdown(
                        f'<div class="temperature">'
                        f'{temperature:.1f} °C</div>',
                        unsafe_allow_html=True
                    )
                    st.write(description.capitalize())
                    st.caption(
                        f"Feels like {feels_like:.1f} °C"
                    )

                st.markdown("### Weather Details")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("💧 Humidity", f"{humidity}%")
                    st.metric("💨 Wind Speed", f"{wind_speed:.1f} km/h")

                with col2:
                    st.metric("🌡️ Feels Like", f"{feels_like:.1f} °C")
                    st.metric("📊 Pressure", f"{pressure} hPa")

                st.caption(
                    "Weather data provided by OpenWeatherMap."
                )

            elif response.status_code == 404:
                st.error(
                    "City not found. Check the spelling and try again."
                )

            elif response.status_code in (401, 403):
                st.error(
                    "The API key was rejected. Check your key and "
                    "OpenWeatherMap account access."
                )

            elif response.status_code == 429:
                st.error(
                    "The API request limit may have been reached. "
                    "Please try again later."
                )

            else:
                st.error(
                    f"Weather service returned HTTP "
                    f"{response.status_code}. Please try again."
                )

        except requests.exceptions.Timeout:
            st.error("The weather request timed out. Please try again.")

        except requests.exceptions.ConnectionError:
            st.error(
                "Unable to connect to the weather service. "
                "Check your internet connection."
            )

        except requests.exceptions.RequestException:
            st.error("A network error occurred while retrieving weather.")

        except (KeyError, TypeError, ValueError):
            st.error(
                "The weather service returned unexpected data. "
                "Please try again later."
            )

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption("Python • Streamlit • OpenWeatherMap API")

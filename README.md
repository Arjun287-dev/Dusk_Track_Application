# Sunset Time Tracker

A simple and user-friendly application that fetches the sunset time of any city from an API and converts the UTC time to the local time of the selected city.

## Link

[Sunset Time Tracker](https://dusktrack.streamlit.app/)

## Features
- Fetches real-time sunset data from a reliable weather API.
- Converts UTC sunset time to the local time of the entered city.
- Built with Streamlit for a clean and interactive user experience.
- Automatically updates according to the current date.

## Prerequisites
Before running the application, ensure you have the following:
1. Python installed (version 3.6 or higher).
2. Required dependencies installed:
   - API Key from OpenWeather.
   - Install required packages:
     ```sh
     pip install streamlit requests datetime
     ```

## Installation
1. Clone this repository:
   ```sh
   git clone <repository_url>
   ```
2. Navigate to the project directory and install the required Python packages:
   ```sh
   cd sunset-time-converter
   pip install -r requirements.txt
   ```

## Running the Application
1. Replace the **API_KEY** in the code with your valid API key.
2. Start the Streamlit server by running:
   ```sh
   streamlit run filepath/filename.py
   ```
3. Open your web browser and go to [http://localhost:8501](http://localhost:8501) to use the application.

## Usage
1. Enter the name of a city (avoid entering specific area names).
2. The application will fetch and display the sunset time in the local timezone of the city.

## API Reference
- The application uses the **Geocoding API** and **Current Weather Data API** from [OpenWeather](https://openweathermap.org/).
- You can modify the code to use any other weather or time conversion API of your choice.

## Contributing
We welcome contributions! If you have any suggestions or improvements, feel free to fork the repository and submit a pull request.
- For major changes, open an issue first to discuss your proposed updates.

## Contact
For any questions or feedback, feel free to reach out:
- Email: [arjunarundiyar28@gmail.com](mailto:arjunarundiyar28@gmail.com)
- Open an issue in this repository.


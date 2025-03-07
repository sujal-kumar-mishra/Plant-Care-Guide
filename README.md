# Plant Care Guide Generator

## Overview
The Plant Care Guide Generator is a web-based application that allows users to generate personalized plant care tips based on user input. The application utilizes a large language model (LLM) to provide tailored gardening advice. Users can specify details such as plant type, growing environment, climate zone, sunlight exposure, watering frequency, soil type, fertilization needs, pest concerns, and seasonal care tips. The system processes this input and generates a comprehensive care guide for the specified plant.

## Features
- **User-Friendly Web Interface**: A simple and intuitive form-based UI.
- **Dynamic Model Selection**: Users can select from various available LLM models.
- **Customizable Plant Care Tips**: Personalized guides based on user-inputted plant parameters.
- **Integration with LLM API**: Supports both open-webui API and Ollama API for generating text.
- **Formatted and Readable Output**: The generated guides are well-structured and easy to read.
- **Copy to Clipboard**: Users can easily copy generated results.
- **Loading Indicator**: Provides feedback to users while generating content.

## Project Structure
```
plant_care_guide/
│── main.py                   # Backend API using FastAPI
│── prompt_templates.py        # Prompt templates for text generation
│── requirements.txt           # Required dependencies
│── static/
│   ├── styles.css             # CSS for styling the web app
│── templates/
│   ├── index.html             # HTML template for the UI
│── README.md                  # Documentation
│── report.pdf                 # Project Report
```

## Technologies Used
- **Backend**: FastAPI (Python)
- **Frontend**: HTML, CSS, JavaScript
- **LLM API Integration**: Open-WebUI API, Ollama API
- **Deployment**: Uvicorn (Local), Future Cloud Support

## Installation
### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/sujal-kumar-mishra/Plant-Care-Guide.git
   cd Plant-Care-Guide
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   uvicorn main:app --reload --host 127.0.0.1 --port 8001
   ```
4. Open the web interface in your browser:
   ```
   http://127.0.0.1:8001/
   ```

## API Endpoints
### `GET /`
Renders the HTML form for users to input plant details.

### `POST /generate`
- Accepts form input and generates a plant care guide.
- Uses Open-WebUI API or Ollama API for text generation.

### `GET /models`
- Fetches available LLM models from the API.

## Usage
1. Open the web app.
2. Fill in the form with your plant details.
3. Click **Generate Plant Care Tips**.
4. View the generated guide and copy it if needed.

## Future Improvements
- **Enhanced Model Selection**: Support for more AI models.
- **User Authentication**: Save and retrieve past guides.
- **Advanced Formatting**: Rich text display for improved readability.
- **Multi-language Support**: Generate guides in different languages.

## Contributors
- SUJAL KUMAR(https://github.com/sujal-kumar-mishra)
- SUHAS B M(https://github.com/suhasbm09)
- SUHAS B H(https://github.com/suhasbm09)
- SUHAS U(https://github.com/SUHAS79)
- SUJAN D(https://github.com/suhasbm09)




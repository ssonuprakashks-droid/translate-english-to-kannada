# English to Kannada Translator

This project is a web application that translates English text to Kannada using Flask. It provides a simple user interface for inputting text and receiving translations.

## Project Structure

```
english-kannada-translator
├── app.py                  # Entry point of the Flask application
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables
├── translator              # Package for translation logic
│   ├── __init__.py        # Package initialization
│   └── translator.py       # Core translation functionality
├── templates               # HTML templates
│   ├── base.html          # Base template
│   ├── index.html         # Main input page
│   └── result.html        # Translation results page
├── static                 # Static files
│   └── css
│       └── styles.css     # CSS styles
├── tests                  # Unit tests
│   └── test_translator.py  # Tests for translation functionality
└── README.md              # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd english-kannada-translator
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add any necessary environment variables.

5. **Run the application:**
   ```
   python app.py
   ```

6. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- Navigate to the main page to input English text for translation.
- Submit the text to receive the translated Kannada text on the results page.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.
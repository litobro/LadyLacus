
# LadyLacus

This webapp utilizes the Lacus to capture a screenshot of a webpage and display it immediately to the user. The image is never stored outside of a valkey database which is ephemereal in nature. 

## Structure

- app/app.py: Main Flask app
- app/templates/: Jinja2 templates
- app/.env: Environment variables (LACUS_URL)

## Usage

1. Set up your Python environment and install requirements (Flask, pylacus, python-dotenv).
2. Set LACUS_URL in app/.env if needed.
3. Run the app from the app/ directory:

   cd app
   python app.py

## Next Steps

- Dockerize Flask app
- Add a docker-compose.yml at the project root to run both the Flask app and Lacus (from the lacus/ submodule)
- Improved styling

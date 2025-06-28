
# LadyLacus

This webapp utilizes the [Lacus](https://github.com/ail-project/lacus) tool to capture a screenshot of a webpage and display it immediately to the user. The image is never stored outside of a valkey database which is ephemereal in nature. 

## Structure

- app/app.py: Main Flask app
- app/templates/: Jinja2 templates
- app/.env: Environment variables (LACUS_URL)
- lacus/: Lacus submodule from the main project

## Usage

1. Set up your Python environment and install requirements (Flask, pylacus, python-dotenv).
2. Set LACUS_URL in app/.env if needed.
3. Run the app from the app/ directory:

   cd app
   python app.py

## Docker Deployment

This application is conveniently deployed with docker compose. Simply clone the repository and run the following command:

```
docker compose up -d
```

LadyLacus will be reachable at [http://localhost:8000](http://localhost:8000) by default.

## Next Steps

- Improved styling
- Additional heuristics for user evaluation
    - AI summary of image?
    - VirusTotal integration
    - Other URL reputation lookups
- LookyLoo submission/integration for admin review?
- Auto-submit for admin review button

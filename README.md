# WebScraperBot

WebScraperBot is a web service built with FastAPI that allows users to scrape content from websites and YouTube videos by providing URLs. It supports extracting text content from webpages and captions from YouTube videos.

## Features

- **Scrape Website Content**: Extracts text content from a given webpage URL.
- **Scrape YouTube Captions**: Extracts captions from a given YouTube video URL if available.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Setup

1. Clone the repository or download the project files to your local machine.
    ```bash
    git clone <repository_url>
    cd WebScraperBot
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install the required packages:
    ```bash
    pip install fastapi uvicorn requests beautifulsoup4 pytube
    ```

## Usage

### Running the Application

1. Ensure the virtual environment is activated.
2. Run the FastAPI application using Uvicorn:
    ```bash
    uvicorn main:app --reload
    ```

3. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation.

### API Endpoints

#### 1. Scrape Website Content

- **Endpoint**: `/scrape_website`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
      "url": "https://example.com"
    }
    ```
- **Response**:
    ```json
    {
      "data": "Extracted text content from the webpage"
    }
    ```

#### 2. Scrape YouTube Captions

- **Endpoint**: `/scrape_youtube`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
      "url": "https://www.youtube.com/watch?v=example"
    }
    ```
- **Response**:
    ```json
    {
      "data": "Extracted captions from the YouTube video"
    }
    ```

### Example Requests

#### Using cURL

- **Scrape Website Content**:
    ```bash
    curl -X 'POST' \
      'http://127.0.0.1:8000/scrape_website' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "url": "https://example.com"
    }'
    ```

- **Scrape YouTube Captions**:
    ```bash
    curl -X 'POST' \
      'http://127.0.0.1:8000/scrape_youtube' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    }'
    ```

## Contributing

If you would like to contribute to this project, please fork the repository and create a pull request with your changes. Contributions are welcome!

## License

This project is licensed under the MIT License.

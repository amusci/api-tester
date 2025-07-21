# API Tester

A simple but powerful API testing tool built with Python and Tkinter.
Test all major HTTP methods with an intuitive GUI interface.

## Features

- **Multi-Method Support**: Support for all major HTTP methods (GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS)
- **Built on Requests**: Powered by Python's reliable `requests` library
- **Live Response Viewer**: Real-time response display with pretty JSON formatting
- **Click to Copy**: Copy responses to clipboard for fast documentation
- **Request Headers**: Add and customize HTTP headers
- **Request Body**: Send JSON payloads and form data

## Requirements

- Python 3.7 or higher
- Required Python packages:
  - `tkinter` (usually comes with Python)
  - `requests`
  - `json` (built-in)

## Installation

1. **Clone or download** this repository to your local machine

2. **Install required dependencies**:
   ```bash
   pip install requests
   ```

3. **Run the application**:
   ```bash
   python api_tester.py
   ```

## Usage

1. **Launch the application** by running the Python script
2. **Enter API URL**: Paste the endpoint URL you want to test
3. **Select HTTP Method**: Choose from GET, POST, PUT, DELETE, PATCH, HEAD, or OPTIONS
4. **Add Headers** (optional): Include any required authentication or content-type headers
5. **Add Request Body** (optional): For POST/PUT requests, include JSON payload or form data
6. **Send Request**: Click the test button to execute the API call
7. **View Response**: See formatted JSON response, status code, and headers
8. **Copy Results**: Use click to copy copy to save response data for documentation

### Supported HTTP Methods

- **GET**: Retrieve data from the server
- **POST**: Send data to create new resources
- **PUT**: Update existing resources
- **DELETE**: Remove resources from the server
- **PATCH**: Partially update existing resources
- **HEAD**: Get headers without response body
- **OPTIONS**: Check available methods and CORS policies

## Error Handling

The application provides clear feedback for common issues:
- Invalid URLs or malformed endpoints
- Network connection errors
- HTTP error status codes (4xx, 5xx)
- JSON parsing errors
- Timeout issues

## Response Features

- **Status Code Display**: Clear indication of HTTP response codes
- **Pretty JSON Formatting**: Automatically formats JSON responses for readability
- **Headers Viewer**: See all response headers
- **Response Time**: Track API performance

## Technical Details

- Built with Python's `tkinter` for cross-platform GUI compatibility
- Uses the `requests` library for reliable HTTP handling
- JSON responses are automatically formatted and syntax highlighted
- Handles various content types including JSON, XML, and plain text
- Timeout protection to prevent hanging requests

## Troubleshooting

**Common Issues:**

1. **"Connection Error"**: Check your internet connection and URL validity
2. **"Timeout Error"**: Server may be slow or unresponsive, try again
3. **"Invalid JSON"**: Response may not be in JSON format, check raw response
4. **"401 Unauthorized"**: Check your authentication headers and API keys

**Dependencies Issues:**
```bash
# If you encounter import errors, try:
pip install --upgrade requests

# For GUI issues on Linux:
sudo apt-get install python3-tk
```

## License

This project is for educational and development use.

## Contributing

Feel free to submit issues, feature requests, or pull requests to contribute.

---

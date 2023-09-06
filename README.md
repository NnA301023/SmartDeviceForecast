# SmartDeviceForecast
Lomba Perioda 2023

# Prerequisites

1. Python: Make sure you have Python installed on your system. You can download it from python.org.

# Installation

1. Clone the Repository: Clone this repository to your local machine using `git clone https://github.com/NnA301023/SmartDeviceForecast.git`.

2. Create a Virtual Environment: Navigate to the project directory and create a virtual environment using the following command:
   ```bash
   # If virtual environment not installed on your local
   python -m pip install virtualenv env

   # If virtual environment is installed on your local
   python -m virtualenv env
   ```

3. Activate the Virtual Environment: Activate the virtual environment based on your OS 

   - On Windows:
   ```bash
    Copy code
    env\Scripts\activate
    On macOS and Linux:
    ```

3. Install Dependencies: Install the required libraries listed in requirements.txt using pip:

    ```bash
    Copy code
    pip install -r requirements.txt
    ```

# Usage

1. Run the FastAPI Application: Start the FastAPI application using the following command:

    ```bash
    Copy code
    uvicorn app:app --reload
    # The application will be available at http://localhost:8000.
    ```

2. Access Documentation: Open the API documentation in your web browser by navigating to http://localhost:8000/docs. You can interact with the API and test the forecasting functionality.
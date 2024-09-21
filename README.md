# Wine Quality Explorer
This is a Streamlit app that allows users to explore the Wine Quality dataset. Users can filter wines based on acidity, alcohol content, and quality using interactive sliders.

## Getting Started
### Prerequisites
- Python 3.6 or higher
- Docker (optional for containerization)

### Installation
1. Clone this repository.
2. Install the required Python packages:

pip install -r requirements.txt


### Running the App
To run the app, use:

streamlit run app.py


### Docker
To run the app in a Docker container:

1. Build the Docker image:

docker build -t wine_quality_app .

2. Run the Docker container:

docker run -p 8501:8501 wine_quality_app


### Usage
Adjust the sliders to filter wines based on their properties. The app displays the filtered results and a histogram of wine quality distribution.

### License
This project is licensed under the MIT License.

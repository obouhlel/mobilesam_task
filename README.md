# Image Segmentation Microservice

This project provides a RESTful API for segmenting images using the MobileSAM model. The service accepts image files and returns segmented images.

## Project Tasks

1. Develop a microservice using FastAPI.
2. Integrate the MobileSAM segmentation model.
3. Create a POST endpoint `/segment-image` to process image inputs.
4. Save and return the segmentation results.

## Requirements

- **Python**: Required to run the project.
- **curl**: Required for making POST requests.
- **jq**: Optional, for better output formatting when testing with curl.
- **Docker**: Required for the bonus task.

## How to running the project on Linux

1. Ensure you have Python3 installed with the command :
```bash
command -v python3
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the FastAPI server:
```bash
fastapi run main.py
```
4. Now the server is running at the port 8000 and you can test with the command curl, an example :
```bash
curl -s -X 'POST' \
	'http://localhost:8000/segment-image' \
	-H 'accept: application/json' \
	-H 'Content-Type: multipart/form-data' \
	-F "image=@resources/dog.jpg;type=image/jpeg"
```

## How to Run the Test Script

1. Grant execution rights to the script:
```bash
chmod +x test.sh
```
2. Run the script
```bash
./test.sh
```

## Docker (Bonus)
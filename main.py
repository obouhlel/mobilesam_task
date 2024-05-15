from fastapi.testclient import TestClient
from services.segment_image import app

client = TestClient(app)

if __name__ == "__main__":
    with open("resources/dog.jpg", "rb") as image:
        response = client.post("/segment-image", files={"image": image})
    assert response.status_code == 200
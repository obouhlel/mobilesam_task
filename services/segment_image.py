import os
import random
import string
from fastapi import FastAPI, UploadFile
from PIL import Image
from MobileSAM.segment import segment_everything

app = FastAPI()

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

@app.post("/segment-image")
async def segment_image(image: UploadFile):
	output_path = "generated/"
	upload_path = "uploads/"

	os.makedirs(output_path, exist_ok=True)
	os.makedirs(upload_path, exist_ok=True)
	image_filename = os.path.join(upload_path, image.filename)
	with open(image_filename, "wb") as buffer:
		content = await image.read()
		buffer.write(content)
	img_file = Image.open(image_filename)
	fig = segment_everything(img_file)
	random_filename = generate_random_string() + ".png"
	fig.save(os.path.join(output_path, random_filename))
	return {"filename": random_filename, "path": f"{output_path}{random_filename}"}
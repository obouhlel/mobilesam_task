import os
from fastapi import FastAPI, UploadFile
from PIL import Image
from MobileSAM.segment import segment_everything

app = FastAPI()

@app.post("/segment-image")
async def segment_image(image: UploadFile):
	output_path = "generated/"

	os.makedirs(output_path, exist_ok=True)
	with open(image.filename, "wb") as buffer:
		content = await image.read()
		buffer.write(content)
	img_file = Image.open(image.filename)
	fig = segment_everything(img_file)
	fig.save(output_path + "test_image.png")
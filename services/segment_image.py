import os
import random
import string
from services import app
from fastapi import UploadFile, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image
from MobileSAM.segment import segment_everything

@app.post("/segment-image")
async def segment_image(image: UploadFile):
	output_path = "generated/"
	upload_path = "uploads/"
	img_extensions = ['jpg', 'jpeg', 'png']

	# Create the directories if they don't exist
	os.makedirs(output_path, exist_ok=True)
	os.makedirs(upload_path, exist_ok=True)

	# Save the uploaded image
	image_filename = os.path.join(upload_path, image.filename)
	with open(image_filename, "wb") as buffer:
		content = await image.read()
		buffer.write(content)

	# Check extension of the image file
	if image_filename.split('.')[-1] not in img_extensions:
		return HTTPException(status_code=400, detail="Invalid image file extension")
	
	# Open the image file
	try:
		img_file = Image.open(image_filename)
	except:
		return HTTPException(status_code=400, detail="Invalid image file")
	
	# Segment the image
	try:
		fig = segment_everything(img_file)
	except:
		return HTTPException(status_code=500, detail="Error segmenting image")
	
	# Save the segmented image
	try:
		id = 0
		img_name = image.filename.rpartition('.')[0]
		output_filename = img_name + f"_msam_{id}" + ".png"
		while output_filename in os.listdir(output_path):
			id += 1
			output_filename = img_name + f"_msam_{id}" + ".png"
		fig.save(os.path.join(output_path, output_filename))
	except:
		return HTTPException(status_code=500, detail="Error saving segmented image")

	return JSONResponse(content={"filename": output_filename, "path": output_path + output_filename})
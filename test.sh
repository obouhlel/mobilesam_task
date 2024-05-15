#!/bin/bash

resource_dir="resources"
image_files=($(ls ${resource_dir}/*))

for image_file in "${image_files[@]}"
do
    echo "Sending POST request to the server with image: $image_file"
    response=$(curl -s -X 'POST' \
        'http://localhost:8000/segment-image' \
        -H 'accept: application/json' \
        -H 'Content-Type: multipart/form-data' \
        -F "image=@$image_file;type=image/jpeg")
    echo $response | jq
    echo ""
done
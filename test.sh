#!/bin/bash

resource_dir="resources"
image_files=($(ls ${resource_dir}/*))

if command -v jq >/dev/null 2>&1; then
    use_jq=true
else
    use_jq=false
    echo "jq is not installed. The JSON response will not be formatted."
fi

for image_file in "${image_files[@]}"
do
    echo "Sending POST request to the server with image: $image_file"
    response=$(curl -s -X 'POST' \
        'http://localhost:8000/segment-image' \
        -H 'accept: application/json' \
        -H 'Content-Type: multipart/form-data' \
        -F "image=@$image_file;type=image/jpeg")
    if [ "$use_jq" = false ]; then
        echo $response
    else
        echo $response | jq
    fi
done
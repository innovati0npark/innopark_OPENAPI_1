from dotenv import load_dotenv          #.env 파일의 환경변수 사용을 위함
import os
from openai import OpenAI

import base64
import requests


openai_api_key = os.getenv("OPENAI_API_KEY")    #.env에 정의된 api_key 사용가능.


# Function to encode the image
def encode_image(image_path):               
  with open(image_path, "rb") as image_file:                #경로의 이미지를 받아서 읽는다. rb(이진 모드) 바이너리모드
    return base64.b64encode(image_file.read()).decode('utf-8')  #이미지 파일을 읽어, 이미지를 base64형식으로 인코딩.

load_dotenv()     #이 함수는 루트 디렉토리에서 .env 파일찾고 환경변수 로드할 때 사용

# Path to your image            로컬에 있는 이미지 적용 !
image_path = "image.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)         #base64 형식의 문자열

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {openai_api_key}"
}


payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "어떤 내용의 이미지이니 ??"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())
from dotenv import load_dotenv          #.env 파일의 환경변수 사용을 위함
import os
from openai import OpenAI
from PIL import Image
import requests


# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

# 환경 변수를 사용하여 API 키를 불러옵니다.
openai_api_key = os.getenv("OPENAI_API_KEY")
MODEL="dall-e-3"                    #이미지는 달리씀 !

client = OpenAI(api_key=openai_api_key)

response = client.images.generate(
    model =MODEL,
    prompt="열매를 많이 맺는 아름다운 남한의 포도나무.",
    size="1024x1024",
    quality="standard",
    n=1,        #이미지 하나 보내줘
)


image_url = response.data[0].url

#저장파일 이름 설정
file_name = "image.jpg"

response = requests.get(image_url)      #이미지 url get방식으로 받기
with open(file_name, "wb") as f:
    f.write(response.content)

Image.open(file_name)

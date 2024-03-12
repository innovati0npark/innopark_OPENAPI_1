from dotenv import load_dotenv          #.env 파일의 환경변수 사용을 위함
import os
from openai import OpenAI

# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()
# 환경 변수를 사용하여 API 키를 불러옵니다.






# 환경 변수를 사용하여 API 키를 불러옵니다.
openai_api_key = os.getenv("OPENAI_API_KEY")

MODEL="gpt-3.5-turbo"
client = OpenAI(api_key=openai_api_key)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)
print(response.choices[0].message.content)
pass
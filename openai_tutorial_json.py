from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  response_format={ "type": "json_object" },            #응답할때 json
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON. 너는 고객의 후기를 바탕으로 그들의 만족도를 조사하는 최고의 조사원이야."},
    {"role": "user", "content": "오늘 구매한 컴퓨터가 정말 맘에 안들어요. 소음이 심해요"}
  ]
)
print(response.choices[0].message.content)
pass
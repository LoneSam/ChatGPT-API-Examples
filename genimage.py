import openai
import os
openai.api_key = os.getenv('OPENAI_API_KEY')

prompt = input('image prompt: ')
response = openai.Image.create(
  prompt=prompt,
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(str(response))
os.system('open '+image_url)
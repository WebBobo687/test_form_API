import os
import openai
openai.api_key = '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'

completion = openai.Completion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": 'hello'},
  ]
)

print(completion.choices[0])

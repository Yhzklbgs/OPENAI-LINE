import openai
openai.api_key = "ISI APIKEY SENDIRI"
model_engine = "text-davinci-003"
prompt = ("buatkan code untuk membuat gambar hitam putih dalam python")
completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5)
message = completions.choices[0].text
print(message)

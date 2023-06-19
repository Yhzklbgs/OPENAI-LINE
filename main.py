import openai

mintaApikey = input('JIKA PUNYA APIKEY JAWAB DENGAN YA, JIKA TIDAK JAWAB TIDAK :\n')
if 'tidak' in mintaApikey:
	print('SILAHKAN DAFTAR AKUN TERLEBIH DAHULU')
else:
	apikey = input('MASUKAN APIKEY ANDA : \n')
	openai.api_key = f'{apikey}'
	model_engine = "text-davinci-003"
	pertanyaan = input("SILAHKAN BERTANYA :\n")
	completions = openai.Completion.create(engine=model_engine, prompt=pertanyaan, max_tokens=1024, n=1,stop=None,temperature=0.5)
	message = completions.choices[0].text
	print(message)

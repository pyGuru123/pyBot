import requests
from flask import Flask, request, Response
from src.parser import parseMessage, parseCommand

TOKEN = "5830914299:AAEyaoz_yGrTzVi2cLMeC6B91QWQho3fUp0"
BOTID = "-1001439604894"
app = Flask(__name__)

def sendMsg(id, text):
	url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
	if text:
		payload = {
			'chat_id' : id,
			'text' : text
		}
		response = requests.post(url, json=payload)
		return response

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		msg = request.get_json()
		chatId, text = parseMessage(msg)
		if chatId:
			result = parseCommand(text)
			print(result)
			sendMsg(chatId, result)

		return Response('ok', status=200)
	return "<h1> Hello Bot </h1>"

if __name__ == "__main__":
	app.run(debug=True, threaded=True)

#https://api.telegram.org/bot5830914299:AAEyaoz_yGrTzVi2cLMeC6B91QWQho3fUp0/setWebhook?url=https://c35e-2409-4063-4b9a-35c4-84c5-c0d8-566e-6f84.in.ngrok.io

from flask import Flask 
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
	resp = VoiceResponse()

	resp.say("""Luke Skywalker has vanished. In his absence,
           the sinister FIRST ORDER has risen from the
           ashes of the Empire and will not rest until
           Skywalker, the last Jedi, has been destroyed.
           With the support of the REPUBLIC, General
           Leia Organa leads a brave RESISTANCE. She is
           desperate to find her brother Luke and gain
           his help in restoring peace and justice to
           the galaxy.

           Leia has sent her most daring pilot on a secret
           mission to Jakku, where an old ally has
           discovered a clue to Luke's whereabouts....""")

	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)
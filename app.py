from flask import Flask, render_template, request, jsonify
import emoji
from emojiconchar import emoji_to_description

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    emoji_input = request.form.get('emoji')
    description = emoji_to_description(emoji_input)
    return jsonify({'description': description})

if __name__ == '__main__':
    app.run(debug=True)

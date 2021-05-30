import flask, json
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/add/', methods=['POST'])
def add_url():
    content=request.get_json(force=True)
    url = content['url']
    if len(url) > 0:
        print(f'url: {url}')
        result = 'url accepted'
    else:
        result = 'please enter a valid url'
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)	#, host='0.0.0.0', port=config[api]['api_port'], use_reloader=False)
from flask import Flask

app = Flask(__name)

@app.route('/sample', methods=['GET'])
def sample_endpoint():
    return 'This is the sample endpoint.'

if __name__ == '__main__':
    app.run(debug=True)

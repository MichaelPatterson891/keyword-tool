from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/generate_keywords', methods=['POST'])
def generate_keywords():
    data = request.json
    main_keyword = data.get('keyword')
    modifiers = ["tools", "software", "apps", "platforms", "agency", "dashboard", "jobs", "cost", "strategy", "tips"]
    keywords = [f"{modifier} {main_keyword}" for modifier in modifiers]
    return jsonify(keywords)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

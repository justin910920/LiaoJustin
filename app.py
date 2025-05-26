import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/slideshow')
def slideshow():
    return render_template('slideshow.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/lung-visualization')
def lung_visualization():
    return render_template('lung-visualization.html')

# 靜態HTML文件
@app.route('/lung-visualization.html')
def lung_visualization_html():
    return send_from_directory('.', 'lung-visualization.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

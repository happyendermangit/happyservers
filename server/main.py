from flask import * 
from lightdb import LightDB

app = Flask('')

db = LightDB('./config.json')

@app.route('/')
async def main():
    return render_template('index.html')


app.run(port=8080)
from flask import Flask, render_template
import time
import redis
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
cache = redis.Redis(host=os.getenv('REDIS_HOST'), port=6379, password=os.getenv('REDIS_PASSWORD'))

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return render_template('hello.html', name= "BIPM", count = count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
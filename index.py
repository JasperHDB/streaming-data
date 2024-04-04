from flask import Flask, Response
from faker import Faker
import random
import time

app = Flask(__name__)
fake = Faker()


def generate_random_data():
    print("Started stream")
    while True:
        first_name: str = random.choice([fake.first_name_male(), fake.first_name_female()])
        last_name: str = fake.last_name()

        data = f"{round(time.time())}\t"
        data += str({
            "first_name": first_name,
            "last_name": last_name,
            "email": f"{first_name.lower()}.{last_name.lower()}@{fake.domain_name()}"
        })
        data += "\n"

        yield data
        time.sleep(random.uniform(1, 2))


@app.route('/')
def stream():
    return Response(generate_random_data(), mimetype='text/plain')


@app.route('/test')
def test():
    return "Up and running!"


if __name__ == "__main__":
    app.run(debug=True)

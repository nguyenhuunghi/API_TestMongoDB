# from flask import Flask, jsonify
# import os
# # from pymongo import MongoClient

# app = Flask(__name__)
# # client = MongoClient()
# # db = client.phones_store
# # collection = db.phones_store
# # phones = db.phones
# # phones = phones.find_one()
# # del phones['_id']

# import psycopg2

# conn = psycopg2.connect("dbname=d8ii07nljrbf7 user=wwitfzysjzlshi host=ec2-23-21-216-174.compute-1.amazonaws.com")
# cur = conn.cursor()
# key = 'phone'
# # cur.execute("CREATE TABLE {} (id serial PRIMARY KEY, name varchar);".format(key))
# # cur.execute("INSERT INTO {} (id, name) VALUES ({}, '{}');".format(key, 1, 'nghi'))
# cur.execute("SELECT * FROM {};".format(key))
# phones = []
# print cur.fetchone()
# conn.commit()

# @app.route('/phones', methods=['GET'])
# def get_phones():
#     return jsonify({'data': phones})

# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)

from flask import Flask, jsonify
import os

app = Flask(__name__)
app.config["DEBUG"] = True
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
            <p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/books', methods=['GET'])
def get_phones():
    return jsonify(books)

if __name__ == '__main__':
    app.run()
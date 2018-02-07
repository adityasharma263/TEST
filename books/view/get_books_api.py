from books.lib.get_books import get_books_from_author
from books import app
from flask import jsonify, request


@app.route('/books', methods=['GET'])
def api():
    if request.method == 'GET':
        author = request.args.get('author', None)
        # a function that will do the following: given a Author, get all Books.
        result = get_books_from_author(author)
        return jsonify(result)
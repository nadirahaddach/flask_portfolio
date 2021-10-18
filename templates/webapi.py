import random

from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')

sports = []
sports_list = [
  "Cross Country", "Feild Hockey", "Football", "Golf", "Tennis", "Volleyball"
]


def _find_next_id():
    return max(jokes["id"] for joke in jokes) + 1


def _init_jokes():
    id = 1
    for joke in joke_list:
        jokes.append({"id": id, "joke": joke, "haha": 0, "boohoo": 0})
        id += 1


@api_bp.route('/joke')
def get_joke():
    if len(jokes) == 0:
        _init_jokes()
    return jsonify(random.choice(jokes))


@api_bp.route('/jokes')
def get_jokes():
    if len(jokes) == 0:
        _init_jokes()
    return jsonify(jokes)


if __name__ == "__main__":
    print(random.choice(joke_list))

from flask import Blueprint, render_template, request
from functions import search_post, read_json
import logging

logging.basicConfig(
    filename='logs',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    key_word = request.args.get('s', "")
    try:
        founded_posts = search_post(read_json(), key_word)
        logger.info(f"Поиск по запросу {key_word}")
        return render_template('post_list.html', key_word=key_word, founded_posts=founded_posts)
    except:
        return "Ошибка чтения файла"


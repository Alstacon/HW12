from functions import check_extension, json_writer
from flask import request, Blueprint, render_template
import logging

load_blueprint = Blueprint('load_blueprint', __name__, template_folder='templates')

logging.basicConfig(
    filename='logs',
    level=logging.ERROR
)
logger_loading = logging.getLogger(__name__)

logging.basicConfig(
    filename='logs',
    level=logging.INFO
)
logger_format = logging.getLogger(__name__)


@load_blueprint.route('/post', methods=['GET'])
def load_page():
    return render_template('post_form.html')


@load_blueprint.route('/post', methods=['POST'])
def load_post_page():
    picture = request.files.get("picture")
    if picture:
        if check_extension(picture):
            picture.save(f"./uploads/images/{picture.filename}")
            post = {'pic': f"uploads/images/{picture.filename}",
                    'content': request.form["content"]}
            try:
                json_writer(post)
                return render_template('post_uploaded.html', post=post, filename=picture.filename)
            except:
                return "Ошибка записи"
        else:
            extension = picture.filename.split('.')[-1]
            logger_format.exception("Загруженный файл неподдерживаемого формата")
            return f"Тип файлов {extension} не поддерживается"
    else:
        logger_loading.warning("Ошибка при загрузке")
        return "Ошибка загрузки"


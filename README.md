1. Склонировать репозиторий Git
git clone  https://github.com/HackathonBT/hackatron_tech_brain.git
2. Переходим в директорию
cd hackatron_tech_brain
2. Cоздаем вируальную среду
python -m venv venv
2. Активируем среду
./venv/Scripts/activate
3. устанавливаем зависимости проекта
pip install -r requirements.txt
4. Для работы системы необходимо скачать обученную нами модель и 
сохранить в директорию app\services\model_save70
по ссылке https://disk.yandex.ru/d/qxhq2iXidjSnCg
5. Запускам серевер
phyton run.py
6. Открываем в браузере http://127.0.0.1:8000/docs

можем тестировать решение через swagger интерфейс
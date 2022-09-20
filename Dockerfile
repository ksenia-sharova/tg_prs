FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY auth_data.py auth_data.py
COPY ex_wb.py ex_wb.py
COPY ex_wb_brend.py ex_wb_brend.py
COPY tg_bot_wb.py tg_bot_wb.py

CMD [ "python", "./tg_bot_wb.py" ]
FROM python:3.12.8
WORKDIR /bot
COPY requirements.txt /bot/
RUN pip install uv
RUN uv pip install -r requirements.txt
COPY . /bot
CMD python bot.py

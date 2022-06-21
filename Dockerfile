FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /home/app/webapp
RUN groupadd -r djangoRUN && useradd --no-log-init -r -g djangoRUN djangoRUN
# Install requirements
COPY --chown=djangoRUN:djangoRUN ./backend/requirements.txt /home/app/webapp/
RUN pip install -r /home/app/webapp/requirements.txt
# Entrypoint
COPY --chown=djangoRUN:djangoRUN ./entrypoint.sh /
RUN chmod +x /entrypoint.sh
USER djangoRUN
EXPOSE 8000
CMD /entrypoint.sh
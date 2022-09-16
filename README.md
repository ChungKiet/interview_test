- Use Docker

docker build -t python-send-email .

docker run python-send-email /path/to/template.json /path/to/customters.csv /path/to/output_folder /path/to/errors.csv

(Exp: docker run python-send-email ./template.json ./data.csv ./json_folder/ ./error.csv)

- No use docker

python send_email.py /path/to/template.json /path/to/customters.csv /path/to/output_folder /path/to/errors.csv
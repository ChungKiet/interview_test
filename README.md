# SEND EMAIL
## _Build and run code_

You can run code by setup the env for python or run it into docker.
You can use generate_data.py file to generate data. Just change the file path and num of records you want to generate file csv.
Note: When running code, it always check the input file is exists. Make sure the files is exists to avoid errors.

## Step

- *Step 1:* Load CSV file and email json template
- *Step 2:* Load json template for add or replace from email template
- *Step 3:* Add / Replace follow the template which you've defined
- *Step 4:* Write the result for each record from csv file, if the email is invalid then save this record into error file

## Run without Docker

Firstly, you must install python. Then, install the requirements dependencies which were write into requirements.txt file.

- *Step 1:* Install python (If you haven't install yet)
- *Step 2:* Install pip (If you haven't instal yet)
- *Step 3:* Cd into the project then run command in cmd ```pip install -r requirements.txt```
- *Step 4:* Run command ```python send_email.py /path/to/template.json /path/to/customters.csv /path/to/output_folder /path/to/errors.csv```
- **_Exp:_** ```python send_email.py /path/to/template.json /path/to/customters.csv /path/to/output_folder /path/to/errors.csv```
## Run with Docker

Note: You must install docker. While run code into docker, you can't get file from your desktop or export the output file into the folder in your local device. All file need to run code must be copy into docker. Therefore, you should copy file into the current directory and change the file path when run code.

The step to setup and run code with docker.
- *Step 1:* Install docker(If you haven't install yet)
- *Step 2:* As I've mentioned above, you must copy all file need to run code into the current directory.
- *Step 3:* Open the project and run command ```docker build -t python-send-email .``` _(There is must have the **DOT** at the end of cmd)_
- *Step 4:* Run command ```docker run python-send-email /path/to/template.json /path/to/customters.csv /path/to/output_folder /path/to/errors.csv```
- **_Exp:_** ```docker run python-send-email python send_email.py ./template.json ./data.csv ./json_folder/ ./error.csv```


## License

MIT
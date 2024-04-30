## Database connection
Update settings.py with correct database connection details

## Install required packages

```
pip install -r requirements.txt
```

## Running the Application

Create the DB tables first:
```
python3 manage.py migrate
```
Run the development web server:
```
python3  manage.py runserver 8080
```
Open the URL http://localhost:8080/ to access the application.


## AWS deployment
Install required packagees
```
sudo apt-get install python3-pip
apt install python3.10-venv
pip install -r requirements.txt
```

Create virtual environment and install required packages into it
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Use zappa tool to prepare for AWS deployment
```
zappa init
```

Add your correct AWS regtion to zappa_settings.json
"aws_region": "eu-central-1"
```
{
    "dev": {
        "django_settings": "DjangoRestApisPostgreSQL.settings",
        "profile_name": "default",
        "project_name": "django-rest-api",
        "runtime": "python3.10",
        "s3_bucket": "zappa-az2emsxq5",
        "aws_region": "eu-central-1"
    }
}
```
Do AWS deployment

```
zappa deploy dev
```

AWS deployment update in case of any changes
```
zappa update dev
```

Undeploy AWS deployment
```
zappa undeploye dev
```

Exit virtual environment
```
deactivate
```

## S3 bucket policy
```
{
   "Version": "2012-10-17",
   "Statement": [
      {
         "Sid": "PublicReadGetObject",
         "Effect": "Allow",
         "Principal": "*",
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::tukejaws/*"
      }
   ]
}
```
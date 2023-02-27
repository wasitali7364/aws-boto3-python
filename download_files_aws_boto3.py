import boto3
from pathlib import Path

data_folder = Path.cwd() / 'Data'
data_folder.mkdir(parents=True, exist_ok=True)

# create a session
s3 = boto3.resource(service_name = 's3')

for obj in s3.Bucket('bucket-name').objects.filter(Prefix='anime/latest/merged/2023'):
    if '/74/' in obj.key and 'merged_file' in obj.key:
        date = obj.key[27:37]
        file = date + '-' + obj.key[-24:]
        file_name = data_folder.joinpath(file)
        s3_key = obj.key
        s3.Bucket('c2foupload-inprod').download_file(Key = s3_key, Filename = str(file_name))

print("Download Successfull")

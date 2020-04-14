import boto3
import sagemaker as sage
from io import StringIO
from dotenv import load_dotenv
import os
import re
import time

load_dotenv()


def slugify(obj):
    # Remove special characters from object title
    filename = '_'.join(re.findall(r'\w+', obj.get('title', 'UNTITLED')))
    return filename


def summarize(event):

    # AWS Configs
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_REGION_NAME = os.getenv('AWS_REGION_NAME')
    SUMMARIZER_MODEL_NAME = os.getenv('SUMMARIZER_MODEL_NAME')

    # Clean Text Downloader
    key = slugify(event)
    bname = os.getenv('AWS_CLEAN_BUCKET_NAME')

    boto3_session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION_NAME
    )

    s3 = boto3_session.resource('s3')
    bucket = s3.Bucket(bname)
    file_object = key + '.txt'

    try:
        os.makedirs(os.getcwd() + '/data', exist_ok=True)
        download_obj = os.getcwd() + '/data/' + key + '.txt'
    except PermissionError as e:
        output_dir = '/tmp/'
        download_obj = output_dir + key + '.txt'
        print(e)

    # ! I can't be using time, I need to find another way to retry
    print("Pausing time for 5 seconds")
    time.sleep(5)
    bucket.download_file(file_object, download_obj)
    print('Downloading file {} ...'.format(file_object))

    content_type = 'text/plain'
    model_name = SUMMARIZER_MODEL_NAME
    sagemaker_session = sage.Session(boto_session=boto3_session)

    f = open(download_obj, mode='r')
    data = f.read().replace('\n', '. ')
    print("Starting Prediction")
    prediction = sage.predictor.RealTimePredictor(endpoint=model_name,
                                                  sagemaker_session=sagemaker_session,
                                                  content_type=content_type).predict(data)
    print("Prediction Complete")

    # Convert Predictions to JSON
    s = str(prediction, 'utf-8')
    data = StringIO(s).read()

    # Removing the annoying execution time string
    sep = "Execution time :"
    cleaned_data = s.split(sep, 1)[0]
    summary_data = {"data": cleaned_data}
    return summary_data

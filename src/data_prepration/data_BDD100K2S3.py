import boto3
import logging
import requests
import os
import zlib
from io import BytesIO
from zipfile import ZipFile
from utility.utils import timeit

# from boto.s3.key import Key

os.environ['AWS_PROFILE'] = "Anubhav_Insight_instance"
os.environ['AWS_DEFAULT_REGION'] = "us-west-2"

def stream_gzip_decompress(stream):
    """
    Function decompress the stream & creates a generator object.
    :param stream: uncompressed stream.
    """
    dec = zlib.decompressobj(32 + zlib.MAX_WBITS)  # offset 32 to skip the header
    for chunk in stream:
        rv = dec.decompress(chunk)
        if rv:
            yield rv

def create_s3_client():
    """
    Instantiation of s3.
    :return: an hook to s3.
    """
    # Create an S3 client
    s3 = boto3.client('s3')

    return s3


def buckets_available(hook):
    """
    display the number of buckets available.
    :param hook: instance of s3
    """
    # Call S3 to list current buckets
    response = hook.list_buckets()

    # Get a list of all bucket names from the response
    buckets = [bucket['Name'] for bucket in response['Buckets']]

    # Print out the bucket list
    print("Bucket List: %s" % buckets)
    pass

def create_bucket(hook, bucket_name):
    """
    Creates a new bucket
    :param hook: instance of s3
    :param bucket_name: desired bucket name, it's unique among all existing buckets.
    """
    hook.create_bucket(Bucket=bucket_name)
    pass

@timeit
def S3_bucket_to_ec2():
    pass


@timeit
def web_to_S3_bucket(hook, bucket_name, url, key):
    """
    Downlaod data directly from web to s3 bucket.
    :param hook: instance of s3
    :param bucket_name: desired bucket name
    :param url: Hyperlink to fetch data from web.
    :param key: Tag needed to find the uploaded data.
    """
    try:
        #bring the content from url
        response = requests.get(url, stream=True)

    except requests.exceptions.RequestException as e:
        print(e)

    try:
        # create a bucket instance
        bucket = boto3.resource('s3').Bucket(bucket_name)
    except botocore.exceptions.ClientError as e:
        print(e)

    # casted into Bytes format & opened it
    # byte_stream =

    for data in stream_gzip_decompress(response.content):
        # Uploads the given file using a managed uploader, which will split up large
        # files automatically and upload parts in parallel.
        bucket.upload_fileobj(data, key)



    pass

def main():
    """
    Starting point of the program.
    """
    s3hook =create_s3_client()

    buckets_available(s3hook)

    # create_bucket(s3hook,'bdd100k')
    # create_bucket(s3hook, 'cityscapes50cities')

    url = "http://dl.yf.io/bdd-data/v1/videos/samples-1k.zip"
        # url = "http://dl.yf.io/bdd-data/v1/videos/test.zip"
        # url = "http://dl.yf.io/bdd-data/v1/videos/train.zip"
        # url = "http://dl.yf.io/bdd-data/v1/videos/val.zip"

    upload_to_S3_bucket(s3hook, bucket_name='bdd100k', url=url, key = 'samples-1k')

if __name__ == "__main__":
    main()

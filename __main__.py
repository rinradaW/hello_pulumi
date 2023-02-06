"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

config = pulumi.Config()
stack = pulumi.get_stack()

owner = config.require('owner')

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket(f'hello-lady-{stack}', tags={'owner':owner})

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)

export BUCKET_NAME=dev-test-covid19-data
export STACK_NAME=s3-dev-test-covid19-data-stack
export CFT_FILE_NAME=create-bucket-cft.yaml
export AWS_CLI_PROFILE=devtest
export AWS_DEFAULT_REGION=ap-south-1

aws cloudformation validate-template --template-body file://$CFT_FILE_NAME \
  --profile $AWS_CLI_PROFILE \
  --region $AWS_DEFAULT_REGION

aws cloudformation deploy --stack-name $STACK_NAME \
  --template-file $CFT_FILE_NAME \
  --parameter-overrides BucketName=$BUCKET_NAME \
  --profile $AWS_CLI_PROFILE \
  --region $AWS_DEFAULT_REGION
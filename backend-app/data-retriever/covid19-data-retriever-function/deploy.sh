export STACK_NAME=lambda-covid19-data-retriever-function-stack
export S3_CLI_BUCKET_NAME=dev-test-sam-cli
export AWS_CLI_PROFILE=devtest
export AWS_DEFAULT_REGION=ap-south-1
sam build && sam validate --profile $AWS_CLI_PROFILE --region $AWS_DEFAULT_REGION && sam package --output-template-file packaged.yaml --s3-bucket $S3_CLI_BUCKET_NAME --profile $AWS_CLI_PROFILE  && sam deploy --template-file packaged.yaml --capabilities CAPABILITY_IAM --stack-name $STACK_NAME --profile $AWS_CLI_PROFILE --region $AWS_DEFAULT_REGION
# && aws cloudformation describe-stacks --stack-name $STACK_NAME --profile devtest

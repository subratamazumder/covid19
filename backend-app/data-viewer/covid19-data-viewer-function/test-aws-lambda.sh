export LAMBDA_FUNCTION_NAME=covid19-data-viewer-function
export AWS_CLI_PROFILE=devtest
export AWS_DEFAULT_REGION=ap-south-1
aws lambda invoke --profile $AWS_CLI_PROFILE --region $AWS_DEFAULT_REGION --function-name $LAMBDA_FUNCTION_NAME --payload file://lambda-payload.json out --log-type Tail \
--query 'LogResult' --output text | base64 -D
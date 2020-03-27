export TABLE_NAME=covid19-stats
export STACK_NAME=dynamo-covid19-stats-stack
export CFT_FILE_NAME=create-table-cft.yaml
export AWS_CLI_PROFILE=devtest
export AWS_DEFAULT_REGION=ap-south-1

aws cloudformation validate-template --template-body file://$CFT_FILE_NAME \
  --profile $AWS_CLI_PROFILE \
  --region $AWS_DEFAULT_REGION

aws cloudformation deploy --stack-name $STACK_NAME \
  --template-file $CFT_FILE_NAME \
  --parameter-overrides TableName=$TABLE_NAME \
  --profile $AWS_CLI_PROFILE \
  --region $AWS_DEFAULT_REGION
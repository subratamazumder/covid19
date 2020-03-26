export S3_CLI_BUCKET_NAME=dev-test-sam-cli
export AWS_CLI_PROFILE=devtest
export AWS_DEFAULT_REGION=ap-south-1
export LAYER_ZIP_NAME=python-request-layer.zip
export LAYER_NAME=request-layer-python
export LAYER_RUNTIME=python3.7
export PY_LIB=requests
rm -rf python LAYER_ZIP_NAME
pip3.7 install $PY_LIB -t ./python
zip -r $LAYER_ZIP_NAME ./python
aws s3 cp $LAYER_ZIP_NAME s3://$S3_CLI_BUCKET_NAME/$LAYER_ZIP_NAME \
  --profile $AWS_CLI_PROFILE \
  --region $AWS_DEFAULT_REGION

aws lambda publish-layer-version \
  --layer-name $LAYER_NAME \
  --compatible-runtimes $LAYER_RUNTIME \
  --content S3Bucket=$S3_CLI_BUCKET_NAME,S3Key=$LAYER_ZIP_NAME \
  --profile $AWS_CLI_PROFILE \
  --region $AWS_DEFAULT_REGION

# Run API Load Test

## Setup Test Scenarios
- Edit `data-viewer-load.yaml` update `config:target` with AWS API Gateway Host
- If needed, update `config:variables:country` to add more countries in your test

## Execute Test
```console
$ sudo npm install -g artillery

$ sudo npm install -g artillery-plugin-expect

$ cd covid19/backend-app/data-viewer/api-tests

$ ./run-load-test.sh <api-key> <duration> <arrivalRate>
```
`api-key` is must, if `duration` & `arrivalRate` is not supplied then gets defaulted by script as `1`.

A html report also gets generated on each run.

# Reference
https://artillery.io/docs/cli-reference/

https://artillery.io/docs/examples/

https://artillery.io/docs/plugin-expectations-assertions/


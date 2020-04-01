#usage : $./run-load-test.sh <api-key> <duration> <arrivalRate>
export API_KEY=$1
if [ -z "$1" ]
  then
    echo "No <api-key> supplied, skip running test"
    exit 1
fi
export DURATION=$2
if [ -z "$2" ]
  then
    echo "No <duration> supplied, defaulting to 1"
    export DURATION=1
fi
export ARRIVAL_RATE=$3
if [ -z "$3" ]
  then
    echo "No <arrivalRate> supplied, defaulting to 1"
    export ARRIVAL_RATE=1
fi
#export OVERRIDE_JSON_TEMPLATE='{"config": {"defaults": {"headers": {"x-api-key": "#API_KEY#"}}}}'
export OVERRIDE_JSON_TEMPLATE='{ "config": { "phases": [ { "duration": #DURATION#, "arrivalRate": #ARRIVAL_RATE# } ], "defaults": { "headers": { "x-api-key": "#API_KEY#", "Accept": "application/json" } } } }'
export OVERRIDE_JSON=${OVERRIDE_JSON_TEMPLATE//#API_KEY#/$API_KEY}
export OVERRIDE_JSON=${OVERRIDE_JSON//#DURATION#/$DURATION}
export OVERRIDE_JSON=${OVERRIDE_JSON//#ARRIVAL_RATE#/$ARRIVAL_RATE}
#echo $OVERRIDE_JSON
export LOAD_TEST_REPORT_DATA=report.json
export LOAD_TEST_REPORT=report
#DEBUG=http:request artillery run --overrides '{"config": {"phases": [{"duration": 2, "arrivalRate": 1}]}}' artillery-test/data-viewer-load.yaml
#DEBUG=http:response artillery run --overrides "$OVERRIDE_JSON" artillery-test/data-viewer-load.yaml
artillery run -o $LOAD_TEST_REPORT_DATA --overrides "$OVERRIDE_JSON" artillery-test/data-viewer-load.yaml
artillery report $LOAD_TEST_REPORT_DATA

export API_KEY=$1
export COUNTRY=$2
#export COUNTRY=$( printf "%s\n" "$2" | sed 's/ /%20/g' )
export API_ENDPOINT=https://azurns8496.execute-api.ap-south-1.amazonaws.com/test/covid19/countries/$COUNTRY/latest
curl -i -X GET -H "x-api-key: $API_KEY" -H "Accept: application/json" $API_ENDPOINT
# Table Name
# CSV Data Format
Province/State,Country/Region,Lat,Long,1/22/20,1/23/20
,India,21.0,78.0,0,1
## Partition Key
country_code or date ?
## Sort Key

## Attribute
total_hit (total_confirmed+total_death), total_confirmed, total_death, total_recovered,
## Sample Data Model
```json
{
    "country_code" : "India",
    "total_hit" : 700,
    "total_death" : 15,
    "total_confirmed" : 685,
    "total_recovered" : 50,
    "lat" : 21.0,
    "long" : 78.0


}
```
## Access Patterns
- Get total hit, confirmed, deaths, recovered for each country
- Get total hit, confirmed, deaths, recovered by country code
- Get total daily hit, confirmed, deaths, recovered by country code & by date
- Get total hit, confirmed, deaths, recovered today
- Get total hit, confirmed, deaths, recovered for a date

## Insertion Patterns
- Update total hit, confirmed, deaths, recovered for each country
- Update confirmed, deaths, recovered by date by country


import React from "react";
import { Row, Col, Button } from "react-bootstrap";
import { Dropdown } from "semantic-ui-react";
import Graph from "./graph";
import {
  API_METERING_ID,
  API_ENDPONIT_STAT_BY_COUNTRY,
  COUNTRY_MAP
} from "./config";
class Search extends React.Component {
  constructor(props) {
    console.log("COVID19 constructing");
    super(props);
    this.state = {
      options: COUNTRY_MAP,
      country: "",
      selected: null,
      covid19Stats: null,
      showGraph: false,
      totalInfected: 0,
      totalDeath: 0,
      totalRecovered: 0,
      lastUpdated: "",
      apiResponseCode: 0,
      showApiStatus: false,
      charCount: 0
    };
    this.handleInputChange = this.handleInputChange.bind(this);
    this.clearData = this.clearData.bind(this);
    this.onSearchChange = this.onSearchChange.bind(this);
    this.onChange = this.onChange.bind(this);
  }
  onSearchChange = (e, data) => {
    console.log("onSearchChange-", data.searchQuery);
    this.setState({ country: data.searchQuery });
  };
  onChange = (e, data) => {
    console.log("onChange data-", data.value);
    this.setState({ selected: data.value });
    this.setState({ country: data.value });
  };
  handleInputChange = event => {
    const target = event.target;
    const value = event.value;
    const name = target.name;
    console.log("name", name);
    console.log("value", value);
    this.setState({
      [name]: value
    });
  };

  clearData = event => {
    this.setState({
      country: "",
      covid19Stats: "",
      selected: "",
      showGraph: false,
      apiResponseCode: 0,
      showApiStatus: false,
      totalInfected: 0,
      totalDeath: 0,
      totalRecovered: 0,
      lastUpdated: "",
      charCount: 0
    });
  };
  searchByCountry = event => {
    console.log("Seraching with country -", this.state.country);
    const fetchUrl = API_ENDPONIT_STAT_BY_COUNTRY.replace(
      "{COUNTRY}",
      this.state.country
    );
    fetch(fetchUrl, {
      headers: {
        Accept: "application/json",
        "x-api-key": API_METERING_ID
      }
    })
      .then(res => {
        this.setState({ apiResponseCode: res.status, showApiStatus: true });
        if (res.ok) {
          return res.json();
        }
        console.log("API invokation is not successful ", res.status);
        throw new Error(
          "Network response was not ok: "
            .concat(res.status)
            .concat(res.statusText)
        );
      })
      .then(data => {
        console.log("Retrieved covid19 stats-");
        console.log(data);
        this.setState({ covid19Stats: JSON.stringify(data) });
        var jsonObj = JSON.parse(JSON.stringify(data));
        //extract data to state
        this.setState({
          totalInfected: jsonObj.total_confirmed,
          totalRecovered: jsonObj.total_recovered,
          totalDeath: jsonObj.total_deaths,
          lastUpdated: jsonObj.last_updated
        });
        //enable graphs
        console.log("Enbaling covid graph for-", this.state.country);
        this.setState({ showGraph: true });
      })
      .catch(console.log);
  };
  render() {
    return (
      <div id="search">
        {/* <Row>
          <Col cm>
            Seach COVID19 Stats by Country
          </Col>
        </Row> */}
        <Row>
          <Col sm>
            <Dropdown
              id="search-id"
              placeholder="Search or Select Country Here"
              fluid
              search
              selection
              options={this.state.options}
              text={this.country}
              name="country"
              value={this.state.selected}
              onChange={this.onChange}
              onSearchChange={this.onSearchChange}
            />
          </Col>
        </Row>
        <br />
        <Row>
          {this.state.showApiStatus && (
            <Col sm>
              <div className="text-center">
                API Response Code - {this.state.apiResponseCode}
              </div>
            </Col>
          )}
        </Row>
        <br />
        <Row>
          <Col sm>
            <div className="text-center">
              <Button
                variant="dark"
                type="submit"
                className="font-weight-bold"
                onClick={this.clearData}
              >
                Clear
              </Button>
              &nbsp;&nbsp;
              <Button
                variant="dark"
                type="submit"
                className="font-weight-bold"
                onClick={this.searchByCountry}
              >
                Search
              </Button>
            </div>
          </Col>
        </Row>
        <Row>
          <Col sm>
            <div
              className="text-center"
              sstyle={{ width: "100%", height: "100%" }}
            >
              {this.state.showGraph && (
                <Graph
                  country={this.state.selected}
                  totalInfected={this.state.totalInfected}
                  totalDeath={this.state.totalDeath}
                  totalRecovered={this.state.totalRecovered}
                  lastUpdated={this.state.lastUpdated}
                />
              )}
            </div>
          </Col>
        </Row>
      </div>
    );
  }
}
export default Search;

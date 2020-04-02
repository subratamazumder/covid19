import React from "react";
import { Row, Col, Button, Alert } from "react-bootstrap";
import Jumbotron from "react-bootstrap/Jumbotron";
import { Dropdown } from "semantic-ui-react";
import Plot from "react-plotly.js";
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
      showApiStatusSuccess: false,
      showApiStatusError: false,
      apiResponseTime: 0,
      charCount: 0,
      graphData: [],
      graphLayout: {},
      graphFrames: [],
      graphConfig: { displayModeBar: false, editable: false }
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
      showApiStatusSuccess: false,
      showApiStatusError: false,
      apiResponseTime: 0,
      totalInfected: 0,
      totalDeath: 0,
      totalRecovered: 0,
      lastUpdated: "",
      charCount: 0,
      graphData: [],
      graphLayout: {},
      graphFrames: [],
      graphConfig: { displayModeBar: false, editable: false, responsive: true }
    });
  };
  searchByCountry = event => {
    console.log("Seraching with country -", this.state.country);
    const fetchUrl = API_ENDPONIT_STAT_BY_COUNTRY.replace(
      "{COUNTRY}",
      this.state.country
    );
    const startTime = Date.now();
    fetch(fetchUrl, {
      headers: {
        Accept: "application/json",
        "x-api-key": API_METERING_ID
      }
    })
      .then(res => {
        this.setState({
          apiResponseCode: res.status,
          apiResponseTime: Date.now() - startTime
        });
        if (res.ok) {
          this.setState({
            showApiStatusSuccess: true,
            showApiStatusError: false
          });
          return res.json();
        }
        console.log("API invocation is not successful ", res.status);
        this.setState({
          showGraph: false,
          showApiStatusError: true,
          showApiStatusSuccess: false
        });
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
          lastUpdated: jsonObj.last_updated,
          graphData: [
            {
              x: [
                "Infected(".concat(jsonObj.total_confirmed).concat(")"),
                "Deaths(".concat(jsonObj.total_deaths).concat(")"),
                "Recovered(".concat(jsonObj.total_recovered).concat(")")
              ],
              y: [
                jsonObj.total_confirmed,
                jsonObj.total_deaths,
                jsonObj.total_recovered
              ],
              type: "bar",
              marker: {
                color: [
                  "rgba(30,144,255,1)",
                  "rgba(222,45,38,0.8)",
                  "rgba(50,205,50,1)"
                ],
                line: {
                  width: 2.5
                }
              }
            }
          ],
          graphLayout: {
            // width: 500,
            // height: 500,
            autosize: true,
            title: "COVID19 Stats For "
              .concat(this.state.country)
              .concat(" updated at ")
              .concat(jsonObj.last_updated)
              .concat(" UTC"),
            dragmode: false,
            font: { family: "Open Sans" },
            yaxis: { fixedrange: true },
            xaxis: { fixedrange: true }
          }
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
        <Row>
          <Col sm>
            <Jumbotron className="bg-white">
              <h3>
                <p className="text-center">
                  Seach COVID19 stats by country? try below!
                </p>
              </h3>
            </Jumbotron>
          </Col>
        </Row>
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
          {this.state.showApiStatusSuccess && (
            <Col sm>
              <div className="text-center">
                <Alert variant="success">
                  <Alert.Heading>Oh great :) You got the data</Alert.Heading>
                  <p>
                    API response code -{this.state.apiResponseCode}, Response
                    Time - {this.state.apiResponseTime} ms
                    <br />
                    Did you know, that you just consumed{" "}
                    <strong>AWS Serverless Components</strong>?
                  </p>
                </Alert>
              </div>
            </Col>
          )}
          {this.state.showApiStatusError && (
            <Col sm>
              <div className="text-center">
                <Alert
                  variant="danger"
                  onClose={() => this.setState({ showApiStatusError: false })}
                  dismissible
                >
                  <Alert.Heading>Oh snap! You got an error!</Alert.Heading>
                  <p>
                    API response code -{this.state.apiResponseCode}, Response
                    Time - {this.state.apiResponseTime} ms
                    <br />
                    Try with a different country or tap on{" "}
                    <strong>Clear</strong> button to reset
                  </p>
                </Alert>
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
                <Plot
                  data={this.state.graphData}
                  layout={this.state.graphLayout}
                  // frames={this.state.graphFrames}
                  config={this.state.graphConfig}
                  onInitialized={figure => this.setState(figure)}
                  onUpdate={figure => this.setState(figure)}
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

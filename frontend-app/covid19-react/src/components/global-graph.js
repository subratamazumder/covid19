import React from "react";
import Plot from "react-plotly.js";
import { API_METERING_ID, API_ENDPONIT_STAT_BY_COUNTRY } from "./config";
class GlobalGraph extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      totalInfected: 0,
      totalDeath: 0,
      totalRecovered: 0,
      country: "GLOBAL",
      lastUpdated: "",
      showGraph: false,
      graphData: [],
      graphLayout: {},
      graphFrames: [],
      graphConfig: {
        displayModeBar: false,
        editable: false,
        responsive: true
      }
    };
  }
  async componentDidMount() {
    console.log("Seraching Global Stats with country -", this.state.country);
    const fetchUrl = API_ENDPONIT_STAT_BY_COUNTRY.replace(
      "{COUNTRY}",
      this.state.country
    );
    await fetch(fetchUrl, {
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
        console.log("Retrieved covid19 global stats-");
        console.log(data);
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
            // autosize: true,
            title: "Global COVID19 Stats updated at "
              .concat(jsonObj.last_updated)
              .concat(" UTC"),
            dragmode: false,
            font: { family: "Open Sans" },
            yaxis: { fixedrange: true },
            xaxis: { fixedrange: true }
          }
        });
        //enable graphs
        console.log("Enbaling covid global graph for-", this.state.country);
        this.setState({ showGraph: true });
      })
      .catch(console.log);
  }
  render() {
    return (
      <div
        className="text-center"
        // sstyle={{ width: "100%", height: "100%" }}
        // disabled
      >
        {this.state.showGraph && (
          <Plot
            data={this.state.graphData}
            layout={this.state.graphLayout}
            frames={this.state.graphFrames}
            config={this.state.graphConfig}
            // onInitialized={figure => this.setState(figure)}
            // onUpdate={figure => this.setState(figure)}
            // useResizeHandler={true}
          />
        )}
      </div>
    );
  }
}
export default GlobalGraph;

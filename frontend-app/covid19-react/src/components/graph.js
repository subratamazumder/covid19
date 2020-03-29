import React from "react";
import Plot from "react-plotly.js";

class Graph extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      layout: {},
      frames: [],
      config: {}
    };
    this.state = {
      data: [
        {
          x: [
            "Infected(".concat(this.props.totalInfected).concat(")"),
            "Deaths(".concat(this.props.totalDeath).concat(")"),
            "Recovered(".concat(this.props.totalRecovered).concat(")")
          ],
          y: [
            this.props.totalInfected,
            this.props.totalDeath,
            this.props.totalRecovered
          ],
          type: "bar",
          marker: {
            color: [
              "rgba(30,144,255,1)",
              "rgba(222,45,38,0.8)",
              "rgba(50,205,50,1)"
            ]
          }
        }
      ],
      layout: {
        // width: 500,
        // height: 500,
        // xref:"container",
        // yref: "container",
        autosize: true,
        title: "COVID19 Stats For ".concat(this.props.country).concat(" updated at ").concat(this.props.lastUpdated)
      },
      useResizeHandler: true,
      style: { width: "100%", height: "100%" }
    };
  }
  render() {
    return (
      <Plot
        data={this.state.data}
        layout={this.state.layout}
        frames={this.state.frames}
        config={this.state.config}
        onInitialized={figure => this.setState(figure)}
        onUpdate={figure => this.setState(figure)}
      />
    );
  }
}
export default Graph;

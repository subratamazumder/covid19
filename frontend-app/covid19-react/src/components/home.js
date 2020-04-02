import React from "react";
import { Row, Col } from "react-bootstrap";
import GithubLogo from "../GitHub-Mark-Light-120px-plus.png";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import BrandLogo from "../dp-logo.png";
import Alert from "react-bootstrap/Alert";
import Image from "react-bootstrap/Image";
import Preface from "./preface";
import Search from "./search";
import GlobalGraph from "./global-graph";
class HomePage extends React.Component {
  render() {
    return (
      <div id="home">
        <Navbar bg="dark" variant="dark">
          <Navbar.Brand
            href="https://subrata.dev/"
            className="text-white font-weight-bold"
          >
            <img
              alt=""
              src={BrandLogo}
              width="30"
              height="30"
              className="d-inline-block align-top"
            />{" "}
            COVID19 Global Stats
          </Navbar.Brand>
          <Nav className="mr-auto"></Nav>
          <Nav></Nav>
          <Nav.Link href="https://github.com/subratamazumder/covid19">
            <Image
              src={GithubLogo}
              alt="Github"
              fluid
              rounded
              width="30"
              height="30"
            />
          </Nav.Link>
        </Navbar>
        <Row>
          <Col sm>
            <Preface></Preface>
          </Col>
        </Row>
        <Row>
          <Col sm>
            <GlobalGraph></GlobalGraph>
          </Col>
        </Row>
        <Row>
          <Col sm>
            <Search></Search>
          </Col>
        </Row>
        <Row>
          <br />
        </Row>
        <Row>
          <Col sm>
            <Alert variant="info" className="text-center">
              <h5>
                <i>
                  Disclaimer : <br />
                  Near realtime COVID19 Stats Data to this Application is
                  fetched from{" "}
                  <a href="https://github.com/CSSEGISandData/COVID-19">
                    public data
                  </a>{" "}
                  managed by{" "}
                  <a href="https://systems.jhu.edu/research/public-health/ncov/">
                    Johns Hopkins CSSE
                  </a>
                  <br/>
                  <br/>
                  Country flags are loaded from <a href="https://react.semantic-ui.com/elements/flag/">semantic-ui</a>, apologies if not appropriate!
                  <br/>
                  <br/>
                  It's an experimental application; for learning purpose only.
                </i>
              </h5>
            </Alert>
          </Col>
        </Row>
      </div>
    );
  }
}
export default HomePage;

import React from "react";
import Jumbotron from "react-bootstrap/Jumbotron";
import Covid19Logo from "../covid19-logo.svg";
function Preface() {
  return (
    <div id="about">
      <Jumbotron className="bg-white">
        <h5>
          <p className="text-center">
            <img
              alt=""
              src={Covid19Logo}
              width="100"
              height="100"
              className="d-inline-block align-top change-my-color"
            />
          </p>
          <i>
            <p>
              It is an unarmed war, where there is no sound of ammunition, no
              war to lose any country or nation, no chance to exploit any
              nuclear power. In this war human flesh will not be shot, no part
              of the body or the whole body will be burned ashore, or any strong
              winning party will not dominate the weak losing party.
            </p>
            <p>
              This is a silent war. A war of viruses with the immune system
              inherent in the human body. The virus that has entered the human
              body silently, has taken away numerous lives. Human life has
              suddenly come to a halt. Don’t know when this war will be over?
              Who will win?
            </p>
            <p>
              <strong>Hope the human race will definitely win ♛.</strong>
            </p>
            <p className="text-right">
              Author -{" "}
              <a href="https://www.facebook.com/profile.php?id=100009533527003">
                Rimpa Paul
              </a>
            </p>
          </i>
        </h5>
      </Jumbotron>
    </div>
  );
}

export default Preface;

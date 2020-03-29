import React from "react";
import CookieConsent from "react-cookie-consent";
function CookieNotification() {
  return (
    <div>
      <CookieConsent
        location="bottom"
        buttonText="I understand"
        cookieName="subrataSiteCookie"
        style={{ background: "#2B373B" }}
        buttonStyle={{ color: "#4e503b", fontSize: "13px" }}
        expires={150}
      >
        This website uses cookies to personalise content and ads, to provide
        social media features and to analyse our traffic. <br />
        <span style={{ fontSize: "10px" }}>
          Also share information about your use of our site with analytics
          partners who may combine it with other information that you’ve
          provided to them or that they’ve collected from your use of their
          services
        </span>
      </CookieConsent>
    </div>
  );
}

export default CookieNotification;

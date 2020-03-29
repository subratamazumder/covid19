import React from "react";
import "./App.css";
import Footer from "./components/footer";
import CookieNotification from "./components/cookie-notification";
import HomePage from "./components/home";
function App() {
  return (
    <div>
      <HomePage></HomePage>
      <Footer></Footer>
      <CookieNotification></CookieNotification>
    </div>
  );
}

export default App;

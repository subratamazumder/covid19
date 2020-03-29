import React from "react";
import { Row, Col, Button } from "react-bootstrap";
import { Dropdown } from "semantic-ui-react";
import Graph from "./graph";
class Search extends React.Component {
  constructor(props) {
    console.log("COVID19 constructing");
    super(props);
    this.state = {
      options: [
        { key: "af", value: "Afghanistan", flag: "af", text: "Afghanistan" },
        { key: "ax", value: "AlandIslands", flag: "ax", text: "Aland Islands" },
        { key: "al", value: "Albania", flag: "al", text: "Albania" },
        { key: "dz", value: "Algeria", flag: "dz", text: "Algeria" },
        {
          key: "as",
          value: "AmericanSamoa",
          flag: "as",
          text: "American Samoa"
        },
        { key: "ad", value: "Andorra", flag: "ad", text: "Andorra" },
        { key: "ao", value: "Angola", flag: "ao", text: "Angola" },
        { key: "ai", value: "Anguilla", flag: "ai", text: "Anguilla" },
        { key: "ag", value: "Antigua", flag: "ag", text: "Antigua" },
        { key: "ar", value: "Argentina", flag: "ar", text: "Argentina" },
        { key: "am", value: "Armenia", flag: "am", text: "Armenia" },
        { key: "aw", value: "Aruba", flag: "aw", text: "Aruba" },
        { key: "au", value: "Australia", flag: "au", text: "Australia" },
        { key: "at", value: "Austria", flag: "at", text: "Austria" },
        { key: "az", value: "Azerbaijan", flag: "az", text: "Azerbaijan" },
        { key: "bs", value: "Bahamas", flag: "bs", text: "Bahamas" },
        { key: "bh", value: "Bahrain", flag: "bh", text: "Bahrain" },
        { key: "bd", value: "Bangladesh", flag: "bd", text: "Bangladesh" },
        { key: "bb", value: "Barbados", flag: "bb", text: "Barbados" },
        { key: "by", value: "Belarus", flag: "by", text: "Belarus" },
        { key: "be", value: "Belgium", flag: "be", text: "Belgium" },
        { key: "bz", value: "Belize", flag: "bz", text: "Belize" },
        { key: "bj", value: "Benin", flag: "bj", text: "Benin" },
        { key: "bm", value: "Bermuda", flag: "bm", text: "Bermuda" },
        { key: "bt", value: "Bhutan", flag: "bt", text: "Bhutan" },
        { key: "bo", value: "Bolivia", flag: "bo", text: "Bolivia" },
        {
          key: "ba",
          value: "BosniaandHerzegovina",
          flag: "ba",
          text: "Bosnia and Herzegovina"
        },
        { key: "bw", value: "Botswana", flag: "bw", text: "Botswana" },
        { key: "bv", value: "BouvetIsland", flag: "bv", text: "Bouvet Island" },
        { key: "br", value: "Brazil", flag: "br", text: "Brazil" },
        {
          key: "vg",
          value: "BritishVirginIslands",
          flag: "vg",
          text: "British Virgin Islands"
        },
        { key: "bn", value: "Brunei", flag: "bn", text: "Brunei" },
        { key: "bg", value: "Bulgaria", flag: "bg", text: "Bulgaria" },
        { key: "bf", value: "BurkinaFaso", flag: "bf", text: "Burkina Faso" },
        { key: "mm", value: "Burma", flag: "mm", text: "Burma" },
        { key: "bi", value: "Burundi", flag: "bi", text: "Burundi" },
        {
          key: "tc",
          value: "CaicosIslands",
          flag: "tc",
          text: "Caicos Islands"
        },
        { key: "kh", value: "Cambodia", flag: "kh", text: "Cambodia" },
        { key: "cm", value: "Cameroon", flag: "cm", text: "Cameroon" },
        { key: "ca", value: "Canada", flag: "ca", text: "Canada" },
        { key: "cv", value: "CapeVerde", flag: "cv", text: "Cape Verde" },
        {
          key: "ky",
          value: "CaymanIslands",
          flag: "ky",
          text: "Cayman Islands"
        },
        {
          key: "cf",
          value: "CentralAfricanRepublic",
          flag: "cf",
          text: "Central African Republic"
        },
        { key: "td", value: "Chad", flag: "td", text: "Chad" },
        { key: "cl", value: "Chile", flag: "cl", text: "Chile" },
        { key: "cn", value: "China", flag: "cn", text: "China" },
        {
          key: "cx",
          value: "ChristmasIsland",
          flag: "cx",
          text: "Christmas Island"
        },
        { key: "cc", value: "CocosIslands", flag: "cc", text: "Cocos Islands" },
        { key: "co", value: "Colombia", flag: "co", text: "Colombia" },
        { key: "km", value: "Comoros", flag: "km", text: "Comoros" },
        {
          key: "cd",
          value: "Congo(Kinshasa)",
          flag: "cd",
          text: "Congo (Kinshasa)"
        },
        {
          key: "cg",
          value: "Congo(Brazzaville)",
          flag: "cg",
          text: "Congo Brazzaville"
        },
        { key: "ck", value: "CookIslands", flag: "ck", text: "Cook Islands" },
        { key: "cr", value: "CostaRica", flag: "cr", text: "Costa Rica" },
        { key: "ci", value: "Coted'Ivoire", flag: "ci", text: "Cote d'Ivoire" },
        { key: "hr", value: "Croatia", flag: "hr", text: "Croatia" },
        { key: "cu", value: "Cuba", flag: "cu", text: "Cuba" },
        { key: "cy", value: "Cyprus", flag: "cy", text: "Cyprus" },
        {
          key: "cz",
          value: "CzechRepublic",
          flag: "cz",
          text: "Czech Republic"
        },
        { key: "dk", value: "Denmark", flag: "dk", text: "Denmark" },
        { key: "dj", value: "Djibouti", flag: "dj", text: "Djibouti" },
        { key: "dm", value: "Dominica", flag: "dm", text: "Dominica" },
        {
          key: "do",
          value: "DominicanRepublic",
          flag: "do",
          text: "Dominican Republic"
        },
        { key: "ec", value: "Ecuador", flag: "ec", text: "Ecuador" },
        { key: "eg", value: "Egypt", flag: "eg", text: "Egypt" },
        { key: "sv", value: "ElSalvador", flag: "sv", text: "El Salvador" },
        {
          key: "gq",
          value: "EquatorialGuinea",
          flag: "gq",
          text: "Equatorial Guinea"
        },
        { key: "er", value: "Eritrea", flag: "er", text: "Eritrea" },
        { key: "ee", value: "Estonia", flag: "ee", text: "Estonia" },
        { key: "et", value: "Ethiopia", flag: "et", text: "Ethiopia" },
        {
          key: "eu",
          value: "Europeanunion",
          flag: "eu",
          text: "Europeanunion"
        },
        {
          key: "fk",
          value: "FalklandIslands",
          flag: "fk",
          text: "Falkland Islands"
        },
        { key: "fo", value: "FaroeIslands", flag: "fo", text: "Faroe Islands" },
        { key: "fj", value: "Fiji", flag: "fj", text: "Fiji" },
        { key: "fi", value: "Finland", flag: "fi", text: "Finland" },
        { key: "fr", value: "France", flag: "fr", text: "France" },
        { key: "gf", value: "FrenchGuiana", flag: "gf", text: "French Guiana" },
        {
          key: "pf",
          value: "FrenchPolynesia",
          flag: "pf",
          text: "French Polynesia"
        },
        {
          key: "tf",
          value: "FrenchTerritories",
          flag: "tf",
          text: "French Territories"
        },
        { key: "ga", value: "Gabon", flag: "ga", text: "Gabon" },
        { key: "gm", value: "Gambia", flag: "gm", text: "Gambia" },
        { key: "ge", value: "Georgia", flag: "ge", text: "Georgia" },
        { key: "de", value: "Germany", flag: "de", text: "Germany" },
        { key: "gh", value: "Ghana", flag: "gh", text: "Ghana" },
        { key: "gi", value: "Gibraltar", flag: "gi", text: "Gibraltar" },
        { key: "gr", value: "Greece", flag: "gr", text: "Greece" },
        { key: "gl", value: "Greenland", flag: "gl", text: "Greenland" },
        { key: "gd", value: "Grenada", flag: "gd", text: "Grenada" },
        { key: "gp", value: "Guadeloupe", flag: "gp", text: "Guadeloupe" },
        { key: "gu", value: "Guam", flag: "gu", text: "Guam" },
        { key: "gt", value: "Guatemala", flag: "gt", text: "Guatemala" },
        { key: "gn", value: "Guinea", flag: "gn", text: "Guinea" },
        {
          key: "gw",
          value: "Guinea-Bissau",
          flag: "gw",
          text: "Guinea-Bissau"
        },
        { key: "gy", value: "Guyana", flag: "gy", text: "Guyana" },
        { key: "ht", value: "Haiti", flag: "ht", text: "Haiti" },
        { key: "hm", value: "HeardIsland", flag: "hm", text: "Heard Island" },
        { key: "hn", value: "Honduras", flag: "hn", text: "Honduras" },
        { key: "hk", value: "HongKong", flag: "hk", text: "Hong Kong" },
        { key: "hu", value: "Hungary", flag: "hu", text: "Hungary" },
        { key: "is", value: "Iceland", flag: "is", text: "Iceland" },
        { key: "in", value: "India", flag: "in", text: "India" },
        {
          key: "io",
          value: "IndianOceanTerritory",
          flag: "io",
          text: "Indian Ocean Territory"
        },
        { key: "id", value: "Indonesia", flag: "id", text: "Indonesia" },
        { key: "ir", value: "Iran", flag: "ir", text: "Iran" },
        { key: "iq", value: "Iraq", flag: "iq", text: "Iraq" },
        { key: "ie", value: "Ireland", flag: "ie", text: "Ireland" },
        { key: "il", value: "Israel", flag: "il", text: "Israel" },
        { key: "it", value: "Italy", flag: "it", text: "Italy" },
        { key: "jm", value: "Jamaica", flag: "jm", text: "Jamaica" },
        { key: "sj", value: "JanMayen", flag: "sj", text: "Jan Mayen" },
        { key: "jp", value: "Japan", flag: "jp", text: "Japan" },
        { key: "jo", value: "Jordan", flag: "jo", text: "Jordan" },
        { key: "kz", value: "Kazakhstan", flag: "kz", text: "Kazakhstan" },
        { key: "ke", value: "Kenya", flag: "ke", text: "Kenya" },
        { key: "ki", value: "Kiribati", flag: "ki", text: "Kiribati" },
        { key: "kw", value: "Kuwait", flag: "kw", text: "Kuwait" },
        { key: "kg", value: "Kyrgyzstan", flag: "kg", text: "Kyrgyzstan" },
        { key: "la", value: "Laos", flag: "la", text: "Laos" },
        { key: "lv", value: "Latvia", flag: "lv", text: "Latvia" },
        { key: "lb", value: "Lebanon", flag: "lb", text: "Lebanon" },
        { key: "ls", value: "Lesotho", flag: "ls", text: "Lesotho" },
        { key: "lr", value: "Liberia", flag: "lr", text: "Liberia" },
        { key: "ly", value: "Libya", flag: "ly", text: "Libya" },
        {
          key: "li",
          value: "Liechtenstein",
          flag: "li",
          text: "Liechtenstein"
        },
        { key: "lt", value: "Lithuania", flag: "lt", text: "Lithuania" },
        { key: "lu", value: "Luxembourg", flag: "lu", text: "Luxembourg" },
        { key: "mo", value: "Macau", flag: "mo", text: "Macau" },
        { key: "mk", value: "North Macedonia", flag: "mk", text: "Macedonia" },
        { key: "mg", value: "Madagascar", flag: "mg", text: "Madagascar" },
        { key: "mw", value: "Malawi", flag: "mw", text: "Malawi" },
        { key: "my", value: "Malaysia", flag: "my", text: "Malaysia" },
        { key: "mv", value: "Maldives", flag: "mv", text: "Maldives" },
        { key: "ml", value: "Mali", flag: "ml", text: "Mali" },
        { key: "mt", value: "Malta", flag: "mt", text: "Malta" },
        {
          key: "mh",
          value: "MarshallIslands",
          flag: "mh",
          text: "Marshall Islands"
        },
        { key: "mq", value: "Martinique", flag: "mq", text: "Martinique" },
        { key: "mr", value: "Mauritania", flag: "mr", text: "Mauritania" },
        { key: "mu", value: "Mauritius", flag: "mu", text: "Mauritius" },
        { key: "yt", value: "Mayotte", flag: "yt", text: "Mayotte" },
        { key: "mx", value: "Mexico", flag: "mx", text: "Mexico" },
        { key: "fm", value: "Micronesia", flag: "fm", text: "Micronesia" },
        { key: "md", value: "Moldova", flag: "md", text: "Moldova" },
        { key: "mc", value: "Monaco", flag: "mc", text: "Monaco" },
        { key: "mn", value: "Mongolia", flag: "mn", text: "Mongolia" },
        { key: "me", value: "Montenegro", flag: "me", text: "Montenegro" },
        { key: "ms", value: "Montserrat", flag: "ms", text: "Montserrat" },
        { key: "ma", value: "Morocco", flag: "ma", text: "Morocco" },
        { key: "mz", value: "Mozambique", flag: "mz", text: "Mozambique" },
        { key: "na", value: "Namibia", flag: "na", text: "Namibia" },
        { key: "nr", value: "Nauru", flag: "nr", text: "Nauru" },
        { key: "np", value: "Nepal", flag: "np", text: "Nepal" },
        { key: "nl", value: "Netherlands", flag: "nl", text: "Netherlands" },
        {
          key: "an",
          value: "Netherlandsantilles",
          flag: "an",
          text: "Netherlandsantilles"
        },
        { key: "nc", value: "NewCaledonia", flag: "nc", text: "New Caledonia" },
        { key: "pg", value: "NewGuinea", flag: "pg", text: "New Guinea" },
        { key: "nz", value: "NewZealand", flag: "nz", text: "New Zealand" },
        { key: "ni", value: "Nicaragua", flag: "ni", text: "Nicaragua" },
        { key: "ne", value: "Niger", flag: "ne", text: "Niger" },
        { key: "ng", value: "Nigeria", flag: "ng", text: "Nigeria" },
        { key: "nu", value: "Niue", flag: "nu", text: "Niue" },
        {
          key: "nf",
          value: "NorfolkIsland",
          flag: "nf",
          text: "Norfolk Island"
        },
        { key: "kp", value: "NorthKorea", flag: "kp", text: "North Korea" },
        {
          key: "mp",
          value: "NorthernMarianaIslands",
          flag: "mp",
          text: "Northern Mariana Islands"
        },
        { key: "no", value: "Norway", flag: "no", text: "Norway" },
        { key: "om", value: "Oman", flag: "om", text: "Oman" },
        { key: "pk", value: "Pakistan", flag: "pk", text: "Pakistan" },
        { key: "pw", value: "Palau", flag: "pw", text: "Palau" },
        { key: "ps", value: "Palestine", flag: "ps", text: "Palestine" },
        { key: "pa", value: "Panama", flag: "pa", text: "Panama" },
        { key: "py", value: "Paraguay", flag: "py", text: "Paraguay" },
        { key: "pe", value: "Peru", flag: "pe", text: "Peru" },
        { key: "ph", value: "Philippines", flag: "ph", text: "Philippines" },
        {
          key: "pn",
          value: "PitcairnIslands",
          flag: "pn",
          text: "Pitcairn Islands"
        },
        { key: "pl", value: "Poland", flag: "pl", text: "Poland" },
        { key: "pt", value: "Portugal", flag: "pt", text: "Portugal" },
        { key: "pr", value: "PuertoRico", flag: "pr", text: "Puerto Rico" },
        { key: "qa", value: "Qatar", flag: "qa", text: "Qatar" },
        { key: "re", value: "Reunion", flag: "re", text: "Reunion" },
        { key: "ro", value: "Romania", flag: "ro", text: "Romania" },
        { key: "ru", value: "Russia", flag: "ru", text: "Russia" },
        { key: "rw", value: "Rwanda", flag: "rw", text: "Rwanda" },
        { key: "sh", value: "SaintHelena", flag: "sh", text: "Saint Helena" },
        {
          key: "kn",
          value: "SaintKittsandNevis",
          flag: "kn",
          text: "Saint Kitts and Nevis"
        },
        { key: "lc", value: "SaintLucia", flag: "lc", text: "Saint Lucia" },
        { key: "pm", value: "SaintPierre", flag: "pm", text: "Saint Pierre" },
        {
          key: "vc",
          value: "SaintVincentandtheGrenadines",
          flag: "vc",
          text: "Saint Vincent"
        },
        { key: "ws", value: "Samoa", flag: "ws", text: "Samoa" },
        { key: "sm", value: "SanMarino", flag: "sm", text: "San Marino" },
        {
          key: "gs",
          value: "SandwichIslands",
          flag: "gs",
          text: "Sandwich Islands"
        },
        { key: "st", value: "SaoTome", flag: "st", text: "Sao Tome" },
        { key: "sa", value: "SaudiArabia", flag: "sa", text: "Saudi Arabia" },
        { key: "gb sct", value: "Scotland", flag: "gb sct", text: "Scotland" },
        { key: "sn", value: "Senegal", flag: "sn", text: "Senegal" },
        { key: "cs", value: "Serbia", flag: "cs", text: "Serbia" },
        { key: "rs", value: "Serbia", flag: "rs", text: "Serbia" },
        { key: "sc", value: "Seychelles", flag: "sc", text: "Seychelles" },
        { key: "sl", value: "SierraLeone", flag: "sl", text: "Sierra Leone" },
        { key: "sg", value: "Singapore", flag: "sg", text: "Singapore" },
        { key: "sk", value: "Slovakia", flag: "sk", text: "Slovakia" },
        { key: "si", value: "Slovenia", flag: "si", text: "Slovenia" },
        {
          key: "sb",
          value: "SolomonIslands",
          flag: "sb",
          text: "Solomon Islands"
        },
        { key: "so", value: "Somalia", flag: "so", text: "Somalia" },
        { key: "za", value: "SouthAfrica", flag: "za", text: "South Africa" },
        { key: "kr", value: "Korea,South", flag: "kr", text: "South Korea" },
        { key: "es", value: "Spain", flag: "es", text: "Spain" },
        { key: "lk", value: "SriLanka", flag: "lk", text: "Sri Lanka" },
        { key: "sd", value: "Sudan", flag: "sd", text: "Sudan" },
        { key: "sr", value: "Suriname", flag: "sr", text: "Suriname" },
        { key: "sz", value: "Swaziland", flag: "sz", text: "Swaziland" },
        { key: "se", value: "Sweden", flag: "se", text: "Sweden" },
        { key: "ch", value: "Switzerland", flag: "ch", text: "Switzerland" },
        { key: "sy", value: "Syria", flag: "sy", text: "Syria" },
        { key: "tw", value: "Taiwan", flag: "tw", text: "Taiwan" },
        { key: "tj", value: "Tajikistan", flag: "tj", text: "Tajikistan" },
        { key: "tz", value: "Tanzania", flag: "tz", text: "Tanzania" },
        { key: "th", value: "Thailand", flag: "th", text: "Thailand" },
        { key: "tl", value: "Timorleste", flag: "tl", text: "Timorleste" },
        { key: "tg", value: "Togo", flag: "tg", text: "Togo" },
        { key: "tk", value: "Tokelau", flag: "tk", text: "Tokelau" },
        { key: "to", value: "Tonga", flag: "to", text: "Tonga" },
        {
          key: "tt",
          value: "TrinidadandTobago",
          flag: "tt",
          text: "Trinidad and Tobago"
        },
        { key: "tn", value: "Tunisia", flag: "tn", text: "Tunisia" },
        { key: "tr", value: "Turkey", flag: "tr", text: "Turkey" },
        { key: "tm", value: "Turkmenistan", flag: "tm", text: "Turkmenistan" },
        { key: "tv", value: "Tuvalu", flag: "tv", text: "Tuvalu" },
        { key: "ae", value: "UnitedArabEmirates", flag: "ae", text: "U.A.E." },
        { key: "ug", value: "Uganda", flag: "ug", text: "Uganda" },
        { key: "ua", value: "Ukraine", flag: "ua", text: "Ukraine" },
        {
          key: "gb",
          value: "UnitedKingdom",
          flag: "gb",
          text: "United Kingdom"
        },
        { key: "us", value: "US", flag: "us", text: "United States (USA)" },
        { key: "uy", value: "Uruguay", flag: "uy", text: "Uruguay" },
        {
          key: "um",
          value: "USMinorIslands",
          flag: "um",
          text: "US Minor Islands"
        },
        {
          key: "vi",
          value: "USVirginIslands",
          flag: "vi",
          text: "US Virgin Islands"
        },
        { key: "uz", value: "Uzbekistan", flag: "uz", text: "Uzbekistan" },
        { key: "vu", value: "Vanuatu", flag: "vu", text: "Vanuatu" },
        { key: "va", value: "VaticanCity", flag: "va", text: "Vatican City" },
        { key: "ve", value: "Venezuela", flag: "ve", text: "Venezuela" },
        { key: "vn", value: "Vietnam", flag: "vn", text: "Vietnam" },
        { key: "gb wls", value: "Wales", flag: "gb wls", text: "Wales" },
        {
          key: "wf",
          value: "WallisandFutuna",
          flag: "wf",
          text: "Wallis and Futuna"
        },
        {
          key: "eh",
          value: "WesternSahara",
          flag: "eh",
          text: "Western Sahara"
        },
        { key: "ye", value: "Yemen", flag: "ye", text: "Yemen" },
        { key: "zm", value: "Zambia", flag: "zm", text: "Zambia" },
        { key: "zw", value: "Zimbabwe", flag: "zw", text: "Zimbabwe" },
        //No flags are available for these countries
        {
          key: "dp",
          value: "DiamondPrincess",
          flag: "",
          text: "Diamond Princess"
        },
        {
          key: "png",
          value: "PapuaNewGuinea",
          flag: "",
          text: "Papua New Guinea"
        },
        {
          key: "wbg",
          value: "WestBankandGaza",
          flag: "",
          text: "West Bank and Gaza"
        }
      ],
      country: "",
      selected: null,
      covid19Stats: null,
      showGraph: false,
      totalInfected: 0,
      totalDeath: 0,
      totalRecovered: 0,
      apiResponseCode: 0,
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
      charCount: 0
    });
  };
  searchByCountry = event => {
    console.log("seraching ", this.state.country);
    const fetchUrl = "https://azurns8496.execute-api.ap-south-1.amazonaws.com/test/covid19/countries/"
      .concat(this.state.country)
      .concat("/latest");
    fetch(fetchUrl, {
      // method: "GET",
      headers: {
        Accept: "application/json",
        "x-api-key": "x5sO3SIPMOa4sMIimIWcehlmZYtVqY4472ZuXpXf"
      }
    })
      .then(res => {
        if (res.ok) {
          this.setState({ apiResponseCode: res.status});
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
          totalDeath: jsonObj.total_deaths
        });
        //enable graphs
        this.setState({ showGraph: true });
      })
      .catch(console.log);
  };
  render() {
    return (
      <div id="search">
        <Row>
          <Col sm>
            <Dropdown
              id="search-id"
              placeholder="Select Country"
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
          <Col sm>
            <div className="text-center">
              API Response Code - {this.state.apiResponseCode}
            </div>
          </Col>
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
            <div className="text-center" sstyle={{width : "100%", height: "100%"}}>
              {this.state.showGraph && (
                <Graph
                  country={this.state.selected}
                  totalInfected={this.state.totalInfected}
                  totalDeath={this.state.totalDeath}
                  totalRecovered={this.state.totalRecovered}
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

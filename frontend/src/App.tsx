import React from "react";
import logo from "./logo.svg";
import "./App.css";
import { Helmet } from "react-helmet";

function App() {
  const navLinks = [
    {
      label: "New Arrivals",
      href: "/new-arrivals",
    },
    {
      label: "Tops",
      href: "/tops",
    },
    {
      label: "Bottoms",
      href: "/bottoms",
    },
    {
      label: "Shoes",
      href: "/shoes",
    },
    {
      label: "Sale",
      href: "/sale",
    },
  ];
  return (
    <div className="App">
      <nav id="sub-nav">
        <ul>
          <li>Register</li>
          <li>Free Shipping on Orders Over US$ 100</li>
          <li>Login</li>
        </ul>
      </nav>
      <nav id="main-nav">
        <ul>
          {navLinks.map(link =>(<li key={link.label}>{link.label}</li>))}
        </ul>
      </nav>
    </div>
  );
}

export default App;

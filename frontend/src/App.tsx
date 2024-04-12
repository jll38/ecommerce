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
          {navLinks.map((link) => (
            <li key={link.label}>{link.label}</li>
          ))}
        </ul>
      </nav>
      <main>
        <section id="product-info" className="flex gap-[3rem] justify-evenly">
          <aside className="w-full max-w-[600px] h-[600px]">img here</aside>
          <section
            id="purchase-info"
            className="w-full max-w-[400px] h-[600px] pt-2 px-0 flex flex-col gap-4"
          >
            <div className="flex flex-col gap-2">
              <h2 className="text-2xl font-semibold">Product Name</h2>
              <h3 className="text-xl">$69.99</h3>
              <p className="text-sm text-black/70">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua.
              </p>
            </div>
            <hr></hr>
            <div className="flex flex-col gap-2">
              <h4 className="text-sm text-black/70">Color:</h4>
              <button>Test</button>
            </div>
            <hr></hr>
            <div className="flex flex-col gap-2">
              <h4 className="text-sm text-black/70">Size:</h4>
              <button>Test</button>
            </div>
            <hr></hr>
            <div className="flex flex-col gap-2">
              <button>Add to Bag</button>
            </div>
            <hr></hr>
            <div className="flex flex-col gap-2">
              <h4 className="text-md">Description</h4>
              <p className="text-sm text-black/70">
                Ut enim ad minim veniam, quis nostrud exercitation ullamco
                laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure
                dolor in reprehenderit in voluptate velit esse cillum dolore eu
                fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
                proident, sunt in culpa qui officia deserunt mollit anim id est
                laborum.
              </p>
            </div>
          </section>
        </section>
      </main>
    </div>
  );
}

export default App;

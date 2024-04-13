import React from "react";
import logo from "./logo.svg";
import "./App.css";
import { Helmet } from "react-helmet";

import Navigation from "./components/shared/navigation/Navigation";
import { BrowserRouter, Routes, Route } from "react-router-dom";

//Page Imports
import ProductPage from './pages/product/ProductPage';

function App() {
  return (
    <div className="App">
      <Navigation />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<></>}></Route>
          <Route path="/products/:productID/" element={<ProductPage/>}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;

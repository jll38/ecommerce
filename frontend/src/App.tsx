import React from "react";
import logo from "./logo.svg";
import "./App.css";

import Navigation from "./components/shared/navigation/Navigation";
import { BrowserRouter, Routes, Route } from "react-router-dom";

//Page Imports
import ProductPage from "./pages/product/ProductPage";
import Login from "./pages/auth/Login";
import Register from "./pages/auth/Register";

function App() {
  return (
    <div className="App">
      <Navigation />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<></>}></Route>
          <Route path="/register" element={<Register/>}></Route>
          <Route path="/login" element={<Login />}></Route>
          <Route path="/products/:productID/" element={<ProductPage />}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;

import React, { useState, createContext } from "react";
import logo from "./logo.svg";
import "./App.css";

import Navigation from "./components/shared/navigation/Navigation";
import { BrowserRouter, Routes, Route } from "react-router-dom";

//Page Imports
import Products from "./pages/product/Products";
import ProductPage from "./pages/product/ProductPage";
import Login from "./pages/auth/Login";
import Register from "./pages/auth/Register";
import { ICartContext, ICartItem } from './types/CartTypes';

export const CartContext = createContext<ICartContext>({
  cart: [],
  setCart: () => {}  // Placeholder function
});

function App() {
  const [cart, setCart] = useState<ICartItem[]>([]);
  return (
    <div className="App">
      <CartContext.Provider value={{cart, setCart}}>
        <Navigation />
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<></>}></Route>
            <Route path="/register" element={<Register />}></Route>
            <Route path="/login" element={<Login />}></Route>
            <Route path="/products" element={<Products />}></Route>
            <Route
              path="/products/:productID/"
              element={<ProductPage />}
            ></Route>
          </Routes>
        </BrowserRouter>
      </CartContext.Provider>
    </div>
  );
}

export default App;

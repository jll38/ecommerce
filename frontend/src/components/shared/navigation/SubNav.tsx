import React from "react";
import Cart from "../cart/Cart";
import SideDrawer from "../modal/SideDrawer/SideDrawer";
export default function SubNav() {
  return (
    <nav id="sub-nav">
      <ul>
        <li>Register</li>
        <li>Free Shipping on Orders Over US$ 100</li>
        <div className="flex gap-4">
          <li>Login</li>
          <Cart/>
        </div>
      </ul>
    </nav>
  );
}

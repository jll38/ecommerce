import React, { useContext, useState } from "react";
import { Button } from "@mui/material";
import { styled } from "@mui/material/styles";
import { ICartContext, ICartItem } from "../../../../types/CartTypes";
import { CartContext } from "../../../../App";
import { Product } from "../../../../types/types";

interface IAddToCart {
  product: Product;
  size: string;
  color: string;
}
export default function AddToCart({ product, size, color }: IAddToCart) {
  const { cart, setCart } = useContext(CartContext);

  function addToCart() {
    // Check if the cart already has the exact same item with matching size and color
    const existingCartItemIndex = cart.findIndex(
      (item) =>
        item.product.product_id === product.product_id &&
        item.size === size &&
        item.color === color
    );

    if (existingCartItemIndex >= 0) {
      // If item exists with same size and color, increase its quantity
      const newCart = [...cart];
      newCart[existingCartItemIndex].quantity += 1;
      setCart(newCart);
    } else {
      // If item does not exist or differs in size/color, add it as a new item to the cart
      const newCartItem = {
        product,
        quantity: 1,
        size,
        color,
      };
      setCart([...cart, newCartItem]);
    }
  }

  return (
    <>
      {product ? (
        <Button variant="contained" onClick={addToCart}>
          Add To Cart
        </Button>
      ) : (
        <Button variant="contained">Out of Stock</Button>
      )}
    </>
  );
}

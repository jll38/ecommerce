import React, {
  createContext,
  useState,
  useContext,
  Dispatch,
  SetStateAction,
} from "react";
import { Product } from "./types";

// Define the type for the cart
export interface ICartItem {
  product: Product;
  quantity: number;
  size: string;
  color: string;
}

// Define the type for the context state
export interface ICartContext {
  cart: ICartItem[];
  setCart: Dispatch<SetStateAction<ICartItem[]>>;
}

export class CartItem implements ICartItem {
  product: Product;
  quantity: number;
  size: string;
  color: string;

  constructor(
    product: Product,
    quantity: number,
    size: string,
    color: string
  ) {
    this.product = product;
    this.quantity = quantity;
    this.size = size;
    this.color = color;
  }
}

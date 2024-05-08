import React, { createContext, useState, useContext, Dispatch, SetStateAction } from 'react';
import { IProduct } from './types';

// Define the type for the cart
export interface ICartItem {
  id: number;
  product: IProduct;
  quantity: number;
  size: string;
  color: string;
}

// Define the type for the context state
export interface ICartContext {
  cart: ICartItem[];
  setCart: Dispatch<SetStateAction<ICartItem[]>>;
}
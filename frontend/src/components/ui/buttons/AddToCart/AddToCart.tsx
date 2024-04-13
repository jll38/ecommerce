import React from "react";
import { Button } from "@mui/material";
import { styled } from '@mui/material/styles';

interface IAddToCart {
  route?: string;
}
export default function AddToCart({ route }: IAddToCart) {
  return (
    <>
      {route ? (
        <Button variant="contained">Add To Cart</Button>
      ) : (
        <Button variant="contained">Out of Stock</Button>
      )}
    </>
  );
}

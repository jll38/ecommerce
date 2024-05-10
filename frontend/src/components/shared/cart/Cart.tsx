import React, { useEffect, useContext, useState } from "react";
import ShoppingBagOutlinedIcon from "@mui/icons-material/ShoppingBagOutlined";
import SideDrawer from "../modal/SideDrawer/SideDrawer";
import { Typography, Box, Button } from "@mui/material";
import Divider from "@mui/material/Divider";
import { AWS_S3_BASE_URL } from "../../../constants";
import { CartContext } from "../../../App";

import DeleteIcon from "@mui/icons-material/Delete";
export default function Cart() {
  const [open, setOpen] = useState(false);
  const { cart, setCart } = useContext(CartContext);
  const [subTotal, setSubTotal] = useState<Number>(0);
  const [tax, setTax] = useState<Number>(0);
  const [total, setTotal] = useState<Number>(0);
  useEffect(() => {
    const newSubTotal = cart.reduce((accumulator, cartItem) => {
      const price = cartItem.product.sale_price || cartItem.product.price;
      return accumulator + price * cartItem.quantity;
    }, 0);
    setSubTotal(newSubTotal);
    console.log(total);
  }, [cart]);

  useEffect(() => {
    setTax(0.07 * Number(subTotal));
  }, [subTotal]);

  useEffect(() => {
    setTotal(Number(tax) + Number(subTotal));
  }, [tax]);
  return (
    <>
      <button
        className="hover:opacity-70"
        onClick={() => {
          setOpen(!open);
        }}
      >
        <ShoppingBagOutlinedIcon />
      </button>
      <SideDrawer open={open} setOpen={setOpen} title="Your Cart">
        {cart.map((cartItem, i) => (
          <div className="border p-2 flex items-center gap-2">
            <aside>
              <figure>
                <img
                  width={100}
                  src={AWS_S3_BASE_URL + cartItem.product.image_url}
                />
              </figure>
            </aside>
            <div>
              <Typography>{cartItem.product.product_name}</Typography>
              <Typography color={"gray"}>
                {cartItem.color} | {cartItem.size}
              </Typography>
              <Typography fontWeight={600} fontSize={14}>
                Qty: {cartItem.quantity}
              </Typography>
              <Typography fontWeight={600} fontSize={14}>
                $
                {cartItem.product.sale_price
                  ? cartItem.product.sale_price
                  : cartItem.product.price}
              </Typography>
            </div>
          </div>
        ))}
        <Box
          sx={{
            padding: 4,
            position: "absolute",
            bottom: 0,
            left: 0,
            width: "100%",
          }}
        >
          <Box>
            <Typography variant="h6">
              Subtotal: ${subTotal.toFixed(2)}{" "}
            </Typography>
            <Typography>Tax: ${tax.toFixed(2)} </Typography>
            <Typography variant="h5">Total: ${total.toFixed(2)} </Typography>
          </Box>
          <Divider />
          <Button>Checkout</Button>
        </Box>
      </SideDrawer>
    </>
  );
}

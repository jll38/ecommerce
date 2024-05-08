import React, { useContext, useState } from "react";
import ShoppingBagOutlinedIcon from "@mui/icons-material/ShoppingBagOutlined";
import SideDrawer from "../modal/SideDrawer/SideDrawer";
import { Typography, Box, Button } from "@mui/material";
import Divider from "@mui/material/Divider";

import { CartContext } from "../../../App";
export default function Cart() {
  const [open, setOpen] = useState(false);
  const { cart, setCart } = useContext(CartContext);
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
        <Typography>Blah Blah Blah</Typography>
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
            <Typography variant="h6">Subtotal: </Typography>
            <Typography>Tax: </Typography>
            <Typography variant="h5">Total: </Typography>
          </Box>
          <Divider />
          <Button>Checkout</Button>
        </Box>
      </SideDrawer>
    </>
  );
}

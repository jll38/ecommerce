import React from "react";
import ShoppingBagOutlinedIcon from "@mui/icons-material/ShoppingBagOutlined";
import SideDrawer from "../modal/SideDrawer/SideDrawer";
export default function Cart() {
  const [open, setOpen] = React.useState(false);
  return (
    <>
      <button className="hover:opacity-70" onClick={() => {setOpen(!open)}}>
        <ShoppingBagOutlinedIcon />
      </button>
      <SideDrawer open={open} setOpen={setOpen}>
        
      </SideDrawer>
    </>
  );
}

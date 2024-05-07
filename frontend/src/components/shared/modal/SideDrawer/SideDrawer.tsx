import * as React from "react";
import Box from "@mui/material/Box";
import Drawer from "@mui/material/Drawer";
import Button from "@mui/material/Button";
import List from "@mui/material/List";
import Divider from "@mui/material/Divider";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import InboxIcon from "@mui/icons-material/MoveToInbox";
import MailIcon from "@mui/icons-material/Mail";
import CloseIcon from "@mui/icons-material/Close";

import { Typography } from "@mui/material";

type Anchor = "right";

export default function SideDrawer({ open, setOpen, children }: any) {
  const toggleDrawer =
    (open: boolean) => (event: React.KeyboardEvent | React.MouseEvent) => {
      if (
        event.type === "keydown" &&
        ((event as React.KeyboardEvent).key === "Tab" ||
          (event as React.KeyboardEvent).key === "Shift")
      ) {
        return;
      }

      setOpen(open);
    };

  const list = (anchor: Anchor) => (
    <Box sx={{ width: 500 }} role="presentation">
      <div style={{ height: 50, padding: 10, display: "flex", justifyContent: "end" }}>
        <button onClick={toggleDrawer(false)}>
          <CloseIcon />
        </button>
      </div>
      <Box>
        {children}
      </Box>
    </Box>
  );

  return (
    <div>
      <Drawer anchor={"right"} open={open} onClose={toggleDrawer(false)}>
        {list("right")}
      </Drawer>
    </div>
  );
}

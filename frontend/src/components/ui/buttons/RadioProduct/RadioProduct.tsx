import React from "react";

import ToggleButton from "@mui/material/ToggleButton";
import ToggleButtonGroup from "@mui/material/ToggleButtonGroup";
export default function RadioProduct({ value, setState }: any) {
  const [assigned, setAssigned] = React.useState(value[0]);
  //@ts-ignore
  const handleChange = (event, newAssigned) => {
    setAssigned(newAssigned);
    setState(newAssigned);
  };
  if (!value) return <></>;
  return (
    <ToggleButtonGroup
      exclusive
      value={assigned}
      onChange={handleChange}
      aria-label="text alignment"
    >
      {value.map((val: any) => (
        <ToggleButton value={val} aria-label={val}>
          {val}
        </ToggleButton>
      ))}
    </ToggleButtonGroup>
  );
}

import React from "react";

import Box from "@mui/material/Box";
import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";

type Props = {
  children: string | JSX.Element | JSX.Element[];
};
export default function AuthPage({ children }: Props) {
  return (
    <main>
      <section
        id="authentication-section"
        className="w-full max-w-[400px] h-[600px] pt-2 px-0 flex justify-center items-center"
      >
        <Card className="w-full max-w-[500px] flex flex-col items-start">
          <CardContent>{children}</CardContent>
        </Card>
      </section>
    </main>
  );
}

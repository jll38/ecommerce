import React, { useState } from "react";
import { Typography, TextField, Button, Box, Container } from "@mui/material";
import AuthPage from "./AuthPage";
import qs from "qs";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  //@ts-ignore
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const credentials = new URLSearchParams();
      credentials.append("username", email);
      credentials.append("password", password);

      const response = await fetch("/token", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: credentials,
      });

      if (!response.ok) {
        throw new Error("Login failed");
      }

      const data = await response.json();
      localStorage.setItem("accessToken", data.access_token);
      // Handle successful login
      console.log("Login successful", data);
    } catch (error) {
      // Handle login error
      console.error("Login error", error);
    }
  };

  return (
    <AuthPage>
      <Container maxWidth="xs">
        <Box
          sx={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            mt: 4,
          }}
        >
          <Typography component="h1" variant="h5">
            Login
          </Typography>
          <Box component="form" onSubmit={handleSubmit} sx={{ mt: 1 }}>
            <TextField
              margin="normal"
              required
              fullWidth
              id="email"
              label="Email Address"
              name="email"
              autoComplete="email"
              autoFocus
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="password"
              label="Password"
              type="password"
              id="password"
              autoComplete="current-password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Login
            </Button>
          </Box>
        </Box>
      </Container>
    </AuthPage>
  );
}

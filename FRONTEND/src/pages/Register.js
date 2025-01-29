import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { registerUser } from "../utils/api";
import { Box, Button, Container, Paper, TextField, Typography } from "@mui/material";
import registerBg from "../statics/register.png"; // Background image

const Register = () => {
  const [formData, setFormData] = useState({ username: "", email: "", password: "" });
  const navigate = useNavigate();

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      await registerUser(formData);
      alert("User registered successfully.");
      navigate("/"); // Redirect to login after registration
    } catch (error) {
      alert("Registration failed.");
    }
  };

  return (
    <Box
      sx={{
        display: "flex",
        height: "100vh",
      }}
    >
      {/* Background image section */}
      <Box
        sx={{
          flex: 1,
          backgroundImage: `url(${registerBg})`,
          backgroundSize: "cover",
          backgroundPosition: "center",
        }}
      />

      {/* Registration form section */}
      <Container
        maxWidth="xs"
        sx={{
          flex: 1,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <Paper elevation={3} sx={{ padding: 3, textAlign: "center", borderRadius: 2 }}>
          
          {/* "REGISTER" Title */}
          <Typography variant="h4" gutterBottom sx={{ fontWeight: 'bold' }}>
            REGISTER
          </Typography>

          <form onSubmit={handleRegister}>
            <TextField
              label="Username"
              variant="outlined"
              fullWidth
              margin="normal"
              value={formData.username}
              onChange={(e) => setFormData({ ...formData, username: e.target.value })}
              required
            />
            <TextField
              label="Email"
              variant="outlined"
              fullWidth
              margin="normal"
              type="email"
              value={formData.email}
              onChange={(e) => setFormData({ ...formData, email: e.target.value })}
              required
            />
            <TextField
              label="Password"
              type="password"
              variant="outlined"
              fullWidth
              margin="normal"
              value={formData.password}
              onChange={(e) => setFormData({ ...formData, password: e.target.value })}
              required
            />
            <Button type="submit" variant="contained" color="primary" fullWidth sx={{ mt: 2 }}>
              Sign Up
            </Button>
          </form>
          <Box mt={2}>
            <Typography variant="body2">
              Already have an account?{" "}
              <a href="/" style={{ color: "#1976d2", textDecoration: "none" }}>
                Log in here
              </a>
            </Typography>
          </Box>
        </Paper>
      </Container>
    </Box>
  );
};

export default Register;

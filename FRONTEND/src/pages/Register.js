import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { registerUser } from "../utils/api";
import { Box, Button, Container, Paper, TextField, Typography } from "@mui/material";
import loginBg from "../statics/register.png"; // Imagen de fondo

const Register = () => {
  const [formData, setFormData] = useState({ username: "", email: "", password: "" });
  const navigate = useNavigate();

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      await registerUser(formData);
      alert("Usuario registrado exitosamente.");
      navigate("/"); // Redirigir al login después del registro
    } catch (error) {
      alert("Error en el registro.");
    }
  };

  return (
    <Box
      sx={{
        display: "flex",
        height: "100vh",
      }}
    >
      {/* Sección de la imagen de fondo */}
      <Box
        sx={{
          flex: 1,
          backgroundImage: `url(${loginBg})`,
          backgroundSize: "cover",
          backgroundPosition: "center",
        }}
      />

      {/* Sección del formulario */}
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
          <Typography variant="h5" gutterBottom>
            Registro
          </Typography>
          <form onSubmit={handleRegister}>
            <TextField
              label="Usuario"
              variant="outlined"
              fullWidth
              margin="normal"
              value={formData.username}
              onChange={(e) => setFormData({ ...formData, username: e.target.value })}
              required
            />
            <TextField
              label="Correo"
              variant="outlined"
              fullWidth
              margin="normal"
              type="email"
              value={formData.email}
              onChange={(e) => setFormData({ ...formData, email: e.target.value })}
              required
            />
            <TextField
              label="Contraseña"
              type="password"
              variant="outlined"
              fullWidth
              margin="normal"
              value={formData.password}
              onChange={(e) => setFormData({ ...formData, password: e.target.value })}
              required
            />
            <Button type="submit" variant="contained" color="primary" fullWidth sx={{ mt: 2 }}>
              Registrarse
            </Button>
          </form>
          <Box mt={2}>
            <Typography variant="body2">
              ¿Ya tienes cuenta?{" "}
              <a href="/" style={{ color: "#1976d2", textDecoration: "none" }}>
                Inicia sesión aquí
              </a>
            </Typography>
          </Box>
        </Paper>
      </Container>
    </Box>
  );
};

export default Register;

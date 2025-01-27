import React, { useState } from "react";
import { registerUser } from "../utils/api";

const Register = () => {
  const [formData, setFormData] = useState({ username: "", email: "", password: "" });

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      await registerUser(formData); // Usa la función específica
      alert("Usuario registrado exitosamente.");
    } catch (error) {
      alert("Error en el registro.");
    }
  };

  return (
    <form onSubmit={handleRegister}>
      <h1>Registro</h1>
      <input
        type="text"
        placeholder="Usuario"
        value={formData.username}
        onChange={(e) => setFormData({ ...formData, username: e.target.value })}
        required
      />
      <input
        type="email"
        placeholder="Correo"
        value={formData.email}
        onChange={(e) => setFormData({ ...formData, email: e.target.value })}
        required
      />
      <input
        type="password"
        placeholder="Contraseña"
        value={formData.password}
        onChange={(e) => setFormData({ ...formData, password: e.target.value })}
        required
      />
      <button type="submit">Registrar</button>
    </form>
  );
};

export default Register;

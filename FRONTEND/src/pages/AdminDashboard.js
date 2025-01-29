import React, { useState } from "react";
import { Button, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Typography } from "@mui/material";

const AdminDashboard = () => {
    // Datos simulados de usuarios
    const [users, setUsers] = useState([
        { id: 1, firstName: "Ramesh", lastName: "Fadatare", email: "ram@gmail.com" },
        { id: 2, firstName: "John", lastName: "Cena", email: "john@gmail.com" },
        { id: 3, firstName: "Tom", lastName: "Cruise", email: "tom@gmail.com" },
        { id: 4, firstName: "Admin", lastName: "admin", email: "admin@gmail.com" },
    ]);

    // Función para ver detalles de usuario
    const handleView = (id) => {
        alert(`Viewing details of user ID: ${id}`);
    };

    // Función para editar usuario
    const handleEdit = (id) => {
        alert(`Editing user ID: ${id}`);
    };

    // Función para eliminar usuario
    const handleDelete = (id) => {
        const confirmDelete = window.confirm("¿Estás seguro de eliminar este usuario?");
        if (confirmDelete) {
            setUsers(users.filter(user => user.id !== id));
        }
    };

    return (
        <div style={{ padding: "20px" }}>
            <Typography variant="h4" gutterBottom style={{ textAlign: "center", fontWeight: "bold" }}>
                Lista de Usuarios
            </Typography>
            <Button variant="contained" color="primary" style={{ marginBottom: "20px" }}>
                Agregar Usuario
            </Button>

            <TableContainer component={Paper}>
                <Table>
                    <TableHead style={{ backgroundColor: "#1976d2" }}>
                        <TableRow>
                            <TableCell style={{ color: "white", fontWeight: "bold" }}>Nombre</TableCell>
                            <TableCell style={{ color: "white", fontWeight: "bold" }}>Apellido</TableCell>
                            <TableCell style={{ color: "white", fontWeight: "bold" }}>Email</TableCell>
                            <TableCell style={{ color: "white", fontWeight: "bold" }}>Acciones</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {users.map((user) => (
                            <TableRow key={user.id}>
                                <TableCell>{user.firstName}</TableCell>
                                <TableCell>{user.lastName}</TableCell>
                                <TableCell>{user.email}</TableCell>
                                <TableCell>
                                    <Button 
                                        variant="contained" 
                                        color="info" 
                                        size="small" 
                                        onClick={() => handleView(user.id)} 
                                        style={{ marginRight: "8px" }}
                                    >
                                        Ver
                                    </Button>
                                    <Button 
                                        variant="contained" 
                                        color="success" 
                                        size="small" 
                                        onClick={() => handleEdit(user.id)} 
                                        style={{ marginRight: "8px" }}
                                    >
                                        Editar
                                    </Button>
                                    <Button 
                                        variant="contained" 
                                        color="error" 
                                        size="small" 
                                        onClick={() => handleDelete(user.id)}
                                    >
                                        Eliminar
                                    </Button>
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </div>
    );
};

export default AdminDashboard;

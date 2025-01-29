import React, { useState } from "react";
import { Button, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Typography } from "@mui/material";

const DoctorDashboard = () => {
    // Datos simulados de servicios médicos
    const [services, setServices] = useState([
        { id: 1, name: "Consulta General", price: "$50", duration: "30 min" },
        { id: 2, name: "Chequeo Cardiológico", price: "$120", duration: "45 min" },
        { id: 3, name: "Examen de Sangre", price: "$80", duration: "20 min" },
    ]);

    // Función para agregar un nuevo servicio
    const handleCreate = () => {
        const newService = { id: Date.now(), name: "Nuevo Servicio", price: "$100", duration: "30 min" };
        setServices([...services, newService]);
    };

    // Función para ver detalles de un servicio
    const handleRead = (id) => {
        alert(`Viendo detalles del servicio ID: ${id}`);
    };

    // Función para actualizar un servicio
    const handleUpdate = (id) => {
        alert(`Editando servicio ID: ${id}`);
    };

    // Función para eliminar un servicio
    const handleDelete = (id) => {
        const confirmDelete = window.confirm("¿Estás seguro de eliminar este servicio?");
        if (confirmDelete) {
            setServices(services.filter(service => service.id !== id));
        }
    };

    return (
        <div style={{ padding: "20px" }}>
            <Typography variant="h4" gutterBottom style={{ textAlign: "center", fontWeight: "bold" }}>
                Servicios Médicos
            </Typography>
            <Button 
                variant="contained" 
                color="primary" 
                onClick={handleCreate} 
                style={{ marginBottom: "20px" }}
            >
                Crear Servicio
            </Button>

            <TableContainer component={Paper}>
                <Table>
                    <TableHead style={{ backgroundColor: "#1976d2" }}>
                        <TableRow>
                            <TableCell style={{ color: "white", fontWeight: "bold" }}>Nombre del Servicio</TableCell>
                            <TableCell style={{ color: "white", fontWeight: "bold" }}>Precio</TableCell>
                            <TableCell style={{ color: "white", fontWeight: "bold" }}>Duración</TableCell>
                            <TableCell style={{ color: "white", fontWeight: "bold" }}>Acciones</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {services.map((service) => (
                            <TableRow key={service.id}>
                                <TableCell>{service.name}</TableCell>
                                <TableCell>{service.price}</TableCell>
                                <TableCell>{service.duration}</TableCell>
                                <TableCell>
                                    <Button 
                                        variant="contained" 
                                        color="info" 
                                        size="small" 
                                        onClick={() => handleRead(service.id)} 
                                        style={{ marginRight: "8px" }}
                                    >
                                        Ver
                                    </Button>
                                    <Button 
                                        variant="contained" 
                                        color="success" 
                                        size="small" 
                                        onClick={() => handleUpdate(service.id)} 
                                        style={{ marginRight: "8px" }}
                                    >
                                        Editar
                                    </Button>
                                    <Button 
                                        variant="contained" 
                                        color="error" 
                                        size="small" 
                                        onClick={() => handleDelete(service.id)}
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

export default DoctorDashboard;

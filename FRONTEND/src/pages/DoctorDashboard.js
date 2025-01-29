import React, { useState } from "react";
import { Button, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Typography } from "@mui/material";

const DoctorDashboard = () => {
    // Simulated medical services data
    const [services, setServices] = useState([
        { id: 1, name: "General Consultation", price: "$50", duration: "30 min" },
        { id: 2, name: "Cardiological Checkup", price: "$120", duration: "45 min" },
        { id: 3, name: "Blood Test", price: "$80", duration: "20 min" },
    ]);

    // Function to add a new service
    const handleCreate = () => {
        const newService = { id: Date.now(), name: "New Service", price: "$100", duration: "30 min" };
        setServices([...services, newService]);
    };

    // Function to view service details
    const handleRead = (id) => {
        alert(`Viewing details of service ID: ${id}`);
    };

    // Function to update a service
    const handleUpdate = (id) => {
        alert(`Editing service ID: ${id}`);
    };

    // Function to delete a service
    const handleDelete = (id) => {
        const confirmDelete = window.confirm("Are you sure you want to delete this service?");
        if (confirmDelete) {
            setServices(services.filter(service => service.id !== id));
        }
    };

    return (
        <div style={{ padding: "20px" }}>
            <Typography variant="h4" gutterBottom style={{ textAlign: "center", fontWeight: "bold" }}>
                Medical Services
            </Typography>
            <Button 
                variant="contained" 
                color="primary" 
                onClick={handleCreate} 
                style={{ marginBottom: "20px" }}
            >
                Create Service
            </Button>

            <TableContainer component={Paper}>
                <Table>
                    <TableHead style={{ backgroundColor: "#1976d2" }}>
                        <TableRow>
                            <TableCell style={{ color: "white", fontWeight: "bold" }}>Service Name</TableCell>
                            <TableCell style={{ color: "white", fontWeight: "bold" }}>Price</TableCell>
                            <TableCell style={{ color: "white", fontWeight: "bold" }}>Duration</TableCell>
                            <TableCell style={{ color: "white", fontWeight: "bold" }}>Actions</TableCell>
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
                                        View
                                    </Button>
                                    <Button 
                                        variant="contained" 
                                        color="success" 
                                        size="small" 
                                        onClick={() => handleUpdate(service.id)} 
                                        style={{ marginRight: "8px" }}
                                    >
                                        Edit
                                    </Button>
                                    <Button 
                                        variant="contained" 
                                        color="error" 
                                        size="small" 
                                        onClick={() => handleDelete(service.id)}
                                    >
                                        Delete
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

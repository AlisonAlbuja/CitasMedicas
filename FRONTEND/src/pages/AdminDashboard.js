import React, { useState } from "react";
import { Button, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Typography } from "@mui/material";

const AdminDashboard = () => {
    // Simulated user data
    const [users, setUsers] = useState([
        { id: 1, firstName: "Ramesh", lastName: "Fadatare", email: "ram@gmail.com" },
        { id: 2, firstName: "John", lastName: "Cena", email: "john@gmail.com" },
        { id: 3, firstName: "Tom", lastName: "Cruise", email: "tom@gmail.com" },
        { id: 4, firstName: "Admin", lastName: "admin", email: "admin@gmail.com" },
    ]);

    // Function to view user details
    const handleView = (id) => {
        alert(`Viewing details of user ID: ${id}`);
    };

    // Function to edit user
    const handleEdit = (id) => {
        alert(`Editing user ID: ${id}`);
    };

    // Function to delete user
    const handleDelete = (id) => {
        const confirmDelete = window.confirm("Are you sure you want to delete this user?");
        if (confirmDelete) {
            setUsers(users.filter(user => user.id !== id));
        }
    };

    return (
        <div style={{ padding: "20px" }}>
            <Typography variant="h4" gutterBottom style={{ textAlign: "center", fontWeight: "bold" }}>
                User List
            </Typography>
            <Button variant="contained" color="primary" style={{ marginBottom: "20px" }}>
                Add User
            </Button>

            <TableContainer component={Paper}>
                <Table>
                    <TableHead style={{ backgroundColor: "#1976d2" }}>
                        <TableRow>
                            <TableCell style={{ color: "white", fontWeight: "bold" }}>First Name</TableCell>
                            <TableCell style={{ color: "white", fontWeight: "bold" }}>Last Name</TableCell>
                            <TableCell style={{ color: "white", fontWeight: "bold" }}>Email</TableCell>
                            <TableCell style={{ color: "white", fontWeight: "bold" }}>Actions</TableCell>
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
                                        View
                                    </Button>
                                    <Button 
                                        variant="contained" 
                                        color="success" 
                                        size="small" 
                                        onClick={() => handleEdit(user.id)} 
                                        style={{ marginRight: "8px" }}
                                    >
                                        Edit
                                    </Button>
                                    <Button 
                                        variant="contained" 
                                        color="error" 
                                        size="small" 
                                        onClick={() => handleDelete(user.id)}
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

export default AdminDashboard;

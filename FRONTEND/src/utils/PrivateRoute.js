import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';

const PrivateRoute = ({ allowedRoles }) => {
    const userRole = parseInt(localStorage.getItem('role'), 10); // Obtiene el rol del usuario desde el localStorage

    return allowedRoles.includes(userRole) ? <Outlet /> : <Navigate to="/" />;
};

export default PrivateRoute;

import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';

const PrivateRoute = ({ allowedRoles }) => {
    const userRole = parseInt(localStorage.getItem('role'), 10); // Get the user's role from localStorage

    return allowedRoles.includes(userRole) ? <Outlet /> : <Navigate to="/" />; // If the user's role is allowed, render the Outlet; otherwise, redirect to the homepage
};

export default PrivateRoute;

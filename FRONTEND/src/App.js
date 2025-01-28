import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './pages/Login';
import Register from './pages/Register';
import AdminDashboard from './pages/AdminDashboard';
import DoctorDashboard from './pages/DoctorDashboard';
import PatientDashboard from './pages/PatientDashboard';
import PrivateRoute from './utils/PrivateRoute';

const App = () => {
    return (
        <Router>
            <Routes>
                {/* Rutas públicas */}
                <Route path="/" element={<Login />} />
                <Route path="/register" element={<Register />} />

                {/* Rutas privadas */}
                <Route path="/admin" element={<PrivateRoute allowedRoles={[1]} />}>
                    <Route path="" element={<AdminDashboard />} />
                </Route>
                <Route path="/doctor" element={<PrivateRoute allowedRoles={[2]} />}>
                    <Route path="" element={<DoctorDashboard />} />
                </Route>
                <Route path="/patient" element={<PrivateRoute allowedRoles={[3]} />}>
                    <Route path="" element={<PatientDashboard />} />
                </Route>
            </Routes>
        </Router>
    );
};

export default App;

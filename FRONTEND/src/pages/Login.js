import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { loginUser } from '../utils/api';
import { jwtDecode } from 'jwt-decode'; // Cambiar a importación nombrada

const Login = () => {
    const [credentials, setCredentials] = useState({ username: '', password: '' });
    const navigate = useNavigate();

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const data = await loginUser(credentials); // Llama al endpoint de login
            const token = data.access_token; // Obtén el token del backend
            localStorage.setItem('token', token); // Guarda el token en localStorage

            // Decodificar el token para obtener el role_id
            const decodedToken = jwtDecode(token); // Decodifica el token
            const roleId = decodedToken.role_id; // Extrae el role_id del token
            localStorage.setItem('role', roleId); // Guarda el role_id en localStorage

            // Redirige según el rol del usuario
            if (roleId === 1) navigate('/admin'); // Administrador
            else if (roleId === 2) navigate('/doctor'); // Doctor
            else if (roleId === 3) navigate('/patient'); // Paciente
            else throw new Error('Rol desconocido');
        } catch (error) {
            console.error('Error al iniciar sesión:', error);
            alert('Error al iniciar sesión. Verifique sus credenciales.');
        }
    };

    return (
        <form onSubmit={handleLogin}>
            <h1>Inicio de Sesión</h1>
            <input
                type="text"
                placeholder="Usuario"
                value={credentials.username}
                onChange={(e) => setCredentials({ ...credentials, username: e.target.value })}
                required
            />
            <input
                type="password"
                placeholder="Contraseña"
                value={credentials.password}
                onChange={(e) => setCredentials({ ...credentials, password: e.target.value })}
                required
            />
            <button type="submit">Iniciar Sesión</button>
        </form>
    );
};

export default Login;

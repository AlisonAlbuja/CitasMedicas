import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { loginUser } from '../utils/api';
import { jwtDecode } from 'jwt-decode';
import { Box, Button, Container, Paper, TextField, Typography } from '@mui/material';
import loginBg from '../statics/login.webp'; // ✅ Background image

const Login = () => {
    const [credentials, setCredentials] = useState({ username: '', password: '' });
    const navigate = useNavigate();

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const data = await loginUser(credentials);
            const token = data.access_token;
            localStorage.setItem('token', token);

            const decodedToken = jwtDecode(token);
            const roleId = decodedToken.role_id;
            localStorage.setItem('role', roleId);

            if (roleId === 1) navigate('/admin');
            else if (roleId === 2) navigate('/doctor');
            else if (roleId === 3) navigate('/patient');
            else throw new Error('Unknown role');
        } catch (error) {
            console.error('Login error:', error);
            alert('Login failed. Please check your credentials.');
        }
    };

    return (
        <Box 
            sx={{ 
                display: 'flex', 
                height: '100vh',
                width: '100vw'
            }}
        >
            {/* Image section */}
            <Box
                sx={{
                    flex: 1,
                    backgroundImage: `url(${loginBg})`, // Use background image
                    backgroundSize: 'cover',
                    backgroundPosition: 'center'
                }}
            />

            {/* Login form section */}
            <Box
                sx={{
                    flex: 1,
                    display: 'flex',
                    justifyContent: 'center',
                    alignItems: 'center',
                    backgroundColor: '#2c2c2c', // Dark background
                    padding: 3
                }}
            >
                <Paper elevation={3} sx={{ padding: 3, textAlign: 'center', borderRadius: 2, width: '100%', maxWidth: 400 }}>
                    
                    {/* "LOGIN" Title */}
                    <Typography variant="h4" gutterBottom sx={{ fontWeight: 'bold' }}>
                        LOGIN
                    </Typography>

                    <form onSubmit={handleLogin}>
                        <TextField
                            label="Username"
                            variant="outlined"
                            fullWidth
                            margin="normal"
                            value={credentials.username}
                            onChange={(e) => setCredentials({ ...credentials, username: e.target.value })}
                            required
                            sx={{ backgroundColor: 'white', borderRadius: 1 }}
                        />
                        <TextField
                            label="Password"
                            type="password"
                            variant="outlined"
                            fullWidth
                            margin="normal"
                            value={credentials.password}
                            onChange={(e) => setCredentials({ ...credentials, password: e.target.value })}
                            required
                            sx={{ backgroundColor: 'white', borderRadius: 1 }}
                        />
                        <Button 
                            type="submit" 
                            variant="contained" 
                            color="primary" 
                            fullWidth 
                            sx={{ mt: 2 }}
                        >
                            Log In
                        </Button>
                    </form>
                    <Box mt={2}>
                        <Typography variant="body2" sx={{ color: '#fff' }}>
                            Don't have an account?{' '}
                            <a href="/register" style={{ color: '#1976d2', textDecoration: 'none' }}>
                                Register here
                            </a>
                        </Typography>
                    </Box>
                </Paper>
            </Box>
        </Box>
    );
};

export default Login;

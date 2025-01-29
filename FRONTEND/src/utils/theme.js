import { createTheme } from '@mui/material/styles';

const theme = createTheme({
    palette: {
        primary: {
            main: '#1976d2', // Azul por defecto
        },
        secondary: {
            main: '#dc004e', // Rojo por defecto
        },
        background: {
            default: '#e3f2fd' // Celeste claro para el fondo global
        }
    },
    typography: {
        fontFamily: 'Arial, sans-serif',
    },
    components: {
        MuiButton: {
            styleOverrides: {
                root: {
                    borderRadius: '8px',
                    textTransform: 'none',
                    fontWeight: 'bold',
                },
            },
        },
    },
});

export default theme;

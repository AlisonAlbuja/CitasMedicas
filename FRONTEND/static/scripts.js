
async function deleteUser(userId, username) {
    const token = localStorage.getItem('authToken'); 
    if (!token) {
        alert('No estás autenticado. Por favor, inicia sesión.');
        return;
    }

    try {
        const response = await fetch(`/users/${userId}`, {
            method: 'DELETE',
            headers: {
                'Authorization': `Bearer ${token}`, 
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username }) 
        });

        const data = await response.json();
        if (response.ok) {
            alert(data.message); 
        } else {
            alert(data.detail || 'Error desconocido'); 
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Hubo un problema al eliminar el usuario.');
    }
}


document.querySelector('#deleteForm').addEventListener('submit', function (e) {
    e.preventDefault(); 
    const userId = document.querySelector('#userId').value;
    const username = document.querySelector('#username').value; 
    deleteUser(userId, username); 
});

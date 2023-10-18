// main.js

document.addEventListener('DOMContentLoaded', (event) => {
    // Code to run after the DOM is fully loaded
});

// Function to handle form submission
function handleFormSubmit(formId, url) {
    const form = document.getElementById(formId);
    form.addEventListener('submit', (event) => {
        event.preventDefault();
        const formData = new FormData(form);
        fetch(url, {
            method: 'POST',
            body: formData
        }).then(response => response.json())
          .then(data => {
            if (data.success) {
                window.location.reload();
            } else {
                alert('Error: ' + data.error);
            }
        }).catch(error => {
            console.error('Error:', error);
        });
    });
}

// Function to handle logout
function handleLogout(logoutButtonId, url) {
    const logoutButton = document.getElementById(logoutButtonId);
    logoutButton.addEventListener('click', (event) => {
        event.preventDefault();
        fetch(url, {
            method: 'POST'
        }).then(response => {
            if (response.ok) {
                window.location.href = '/login';
            } else {
                alert('Error: Could not log out');
            }
        }).catch(error => {
            console.error('Error:', error);
        });
    });
}

// Call functions
handleFormSubmit('productionForm', '/production/submit');
handleFormSubmit('qualityForm', '/quality/submit');
handleFormSubmit('warehouseForm', '/warehouse/submit');
handleLogout('logoutButton', '/logout');
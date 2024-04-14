function submitForm() {
    var email = document.getElementById('Email').value;
    var password = document.getElementById('Passwrod').value;

    var data = {
        email: email,
        password: password
    };

    fetch('http://localhost:8000/sign_in', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
            console.log('Login successful');
        } else {
            console.error('Login failed');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
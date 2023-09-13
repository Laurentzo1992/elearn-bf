
    document.addEventListener('DOMContentLoaded', function () {
        const loginForm = document.getElementById('login-form');
        const loginResponse = document.getElementById('login-response');

        loginForm.addEventListener('htmx:response', function (event) {
            const response = event.detail.xhr.response;
            if (response.message === 'Logged in successfully.') {
                loginResponse.innerHTML = 'Connexion réussie.';
                // Redirigez l'utilisateur vers une page appropriée après la connexion si nécessaire.
                window.location.href = '/page_apres_connexion';
            } else {
                loginResponse.innerHTML = 'Identifiants invalides.';
            }
        });
    });


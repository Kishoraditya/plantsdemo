const plantForm = document.getElementById('plant-form');

plantForm.addEventListener('submit', function(event) {
    event.preventDefault();

    var formData = new FormData();
    formData.append('plant-name', document.getElementById('plant-name').value);
    formData.append('plant-description', document.getElementById('plant-description').value);
    formData.append('plant-location', document.getElementById('plant-location').value);
    formData.append('plant-image', document.getElementById('plant-image').files[0]);

    // Get the CSRF token
    var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch('/landing_page/', {
        method: 'POST',
        headers: {
            // Include the CSRF token in the request headers
            'X-CSRFToken': csrftoken
        },
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            console.log(response);
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log(data.message);
        // Reset the form or display a success message
    })
    .catch(error => {
        console.error('Error:', error);
        // Display an error message
    });
});

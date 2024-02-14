// JavaScript
document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('signup-modal');
    const closeButton = document.querySelector('.close');
    const cancelButton = document.getElementById('cancel-button');
    const subscribeForm = document.getElementById('signup-form');
    const thankYouMessage = document.getElementById('thank-you-message');
    const shopButton = document.getElementById('shop-button');

    // Show modal when the page loads
    modal.style.display = 'block';

    // Close modal when close button is clicked
    closeButton.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    // Close modal when cancel button is clicked
    cancelButton.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    // Close modal when user clicks outside the modal
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });

    // Handle form submission
    subscribeForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission behavior

        // Display thank you message and shop button
        thankYouMessage.style.display = 'block';
        shopButton.style.display = 'block';

        // Hide the form
        subscribeForm.style.display = 'none';
    });

    // Handle shop button click
    shopButton.addEventListener('click', function() {
        // Redirect user to products.html
        window.location.href = '/products/';
    });


});


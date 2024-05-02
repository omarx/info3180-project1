document.addEventListener('DOMContentLoaded', function() {
    // Select all elements with the class 'card-price'
    const prices = document.querySelectorAll('.card-price');

    prices.forEach(function(elem) {
        // Get the price from the data attribute
        let price = parseFloat(elem.dataset.price);

        // Format the price as currency
        elem.textContent = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(price);
    });
     document.querySelectorAll('.view-property').forEach(button => {
        button.addEventListener('click', function() {
            const propertyId = this.getAttribute('data-id');
            window.location.href = '/properties/' + propertyId;
        });
    });
});

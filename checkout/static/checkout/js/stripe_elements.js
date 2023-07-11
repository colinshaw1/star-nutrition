/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/
// get strip public key
var stripe_public_key = €('#id_stripe_public_key').text().slice(1, -1);
// get stripe client key
var client_secret = €('#id_client_secret').text().slice(1, -1);
// use js in base.html file
var stripe = Stripe(stripe_public_key);
// create instance of stipe elements
var elements = stripe.elements();
// styles from stripe js docs
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    // eventlistener to add to the card erros div
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>€{event.error.message}</span>
        `;
        €(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});
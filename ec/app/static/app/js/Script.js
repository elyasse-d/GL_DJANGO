// Fonction pour envoyer une requête AJAX pour ajouter un produit au panier
function addToCart(productId) {
    // Envoyer une requête AJAX au serveur pour ajouter le produit au panier
    $.ajax({
        url: '/add-to-cart',
        type: 'POST',
        data: { prod_id: productId },
        success: function(response) {
            // Mettre à jour l'affichage du panier avec les informations du panier
            updateCartDisplay(response.cart);
        },
        error: function(xhr, status, error) {
            console.error(error);
        }
    });
}

// Fonction pour mettre à jour l'affichage du panier
function updateCartDisplay(cartData) {
    // Effacer le contenu précédent du panier
    $('#cart-content').empty();
    
    // Ajouter chaque produit du panier à l'affichage
    cartData.forEach(function(item) {
        $('#cart-content').append('<div>' + item.title + ' - ' + item.price + '</div>');
    });
}

// Attacher un gestionnaire d'événements au clic sur le bouton "Ajouter au panier"
$('.add-to-cart-btn').click(function() {
    var productId = $(this).data('product-id');
    addToCart(productId);
});

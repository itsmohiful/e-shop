//add to cart
const cartButtons = Array.from(document.querySelectorAll('.add-cart'));

function handleProduct(){
    // const id = this.dataset.id;
    // const action = this.dataset.action;
    const {id,action } = this.dataset;
    addToCart(id,action)
}

async function addToCart(id,action){
    try{
        fetch('add-to-cart',{
            method : "POST",
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrf_token
            },
            body: JSON.stringify({id,action})
        })
        location.reload()
    }catch(err){
        console.log(err);
    }
    
}

cartButtons.forEach((button) => button.addEventListener('click', handleProduct))

//console.log(cartButtons)
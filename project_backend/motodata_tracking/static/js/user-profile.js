function toggleEditForm() {
    const infoView = document.querySelector('.info-view');
    const infoForm = document.querySelector('.info-form');
    console.log("toggled")
    
    if (infoForm.style.display === 'none') {
        infoView.style.display = 'none';
        infoForm.style.display = 'block';
    } else {
        infoView.style.display = 'block';
        infoForm.style.display = 'none';
    }
}

function saveChanges(event) {
    event.preventDefault(); // Prevent form from refreshing the page
    
    const fullName = document.getElementById('full-name').value;
    const email = document.getElementById('email').value;
    
    console.log('Saved Changes:', { fullName, email });
    
    // TODO: Make an AJAX request to update the backend or redirect the user
    toggleEditForm(); // Switch back to the display view
}

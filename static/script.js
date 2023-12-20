function displaySelectedImage(event) {
    const selectedImage = document.getElementById("selectedImage");
    const fileInput = event.target;

    if (fileInput.files && fileInput.files[0]) {
        const reader = new FileReader();

        reader.onload = function(e) {
            selectedImage.src = e.target.result;
        };

        reader.readAsDataURL(fileInput.files[0]);
    }
}

function showSending() {
  const button= document.getElementById("btnSubmit");
  button.value = 'Sending to Inky..';
}

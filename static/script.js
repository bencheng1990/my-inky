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

function showSending(elementId) {
  const button= document.getElementById(elementId);
  button.value = 'Sending to Inky..';
}

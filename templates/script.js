document.addEventListener("DOMContentLoaded", function() {
    const fileInput = document.getElementById("fileInput");
    const fileLabel = document.getElementById("fileLabel");
    const fileInputLabel = document.getElementById("fileInputLabel");

    fileInput.addEventListener("change", function() {
        if (fileInput.files.length > 0) {
            const fileName = fileInput.files[0].name;
            fileLabel.textContent = fileName;
        } else {
            fileLabel.textContent = "No file chosen";
        }
    });

    // When the form is submitted, reset the file input and label
    const uploadForm = document.getElementById("upload-form");
    uploadForm.addEventListener("submit", function() {
        fileInput.value = "";
        fileLabel.textContent = "No file chosen";
    });
});

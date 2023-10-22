document.addEventListener("DOMContentLoaded", function () {
    const editButton = document.querySelector("#editButton");
    const editFields = document.querySelectorAll(".edit-field");
    const viewFields = document.querySelectorAll(".view-field");

    editButton.addEventListener("click", function () {
        if (editButton.textContent === "Editar") {
            // Alternar para campos de edição
            editFields.forEach((field) => {
                field.style.display = "block";
            });

            // Ocultar campos de visualização
            viewFields.forEach((field) => {
                field.style.display = "none";
            });

            editButton.textContent = "Salvar";
        } else if (editButton.textContent === "Salvar") {
            // Alternar para campos de visualização
            viewFields.forEach((field) => {
                field.style.display = "block";
            });

            // Ocultar campos de edição
            editFields.forEach((field) => {
                field.style.display = "none";
            });

            editButton.textContent = "Editar";
        }
    });
});

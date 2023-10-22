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
            editButton.style.backgroundColor = "var(--green-base)";
            editButton.style.color = "var(--background-white)"
            editButton.style.border = "none";
            editButton.style.fontWeight = "500";
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
            editButton.style = ""; // retorna ao padrao

        }
    });
});

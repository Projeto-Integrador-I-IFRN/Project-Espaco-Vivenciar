document.addEventListener("DOMContentLoaded", function () {
    const editButton = document.querySelector("#editButton");
    const editFields = document.querySelectorAll(".edit-field");
    const viewFields = document.querySelectorAll(".view-field");
    const imagePacient = document.querySelector(".image-paciente");
    const firstSection = document.querySelector(".first-section");
    const newPacient = document.querySelector('.cadastrar-paciente-button');
    const cardPacientes = document.querySelector(".pacientes-detalhados");
    const buttonExcluir = document.querySelector('#button-excluir');
    const pacientList = document.querySelectorAll('.card-paciente');

    newPacient.addEventListener("click", function () {
        editButton.textContent = "Salvar";
            editButton.style.backgroundColor = "var(--green-base)";
            editButton.style.color = "var(--background-white)";
            editButton.style.border = "none";
            editButton.style.fontWeight = "500";
            imagePacient.style.display = "none";
            firstSection.style.gap = "100px";
        cardPacientes.style = "";
        editFields.forEach((field) => {
            field.style.display = "block";
            if (field.tagName === "SELECT") {
                // Mantém o valor do campo de gênero
                field.value = "Masculino";
            } else {
                field.value = '';
            }
        });

        viewFields.forEach((field) => {
            field.style.display = "none";
        });

        imagePacient.style.display = "none";
        firstSection.style.gap = "100px";
    });

    buttonExcluir.addEventListener("click", function () {
        cardPacientes.style.visibility = "hidden";
    });

    pacientList.forEach(function (pacient) {
        pacient.addEventListener("click", function () {
            cardPacientes.style = "";
            editFields.forEach((field) => {
                field.style.display = "none";
            });
    
            viewFields.forEach((field) => {
                field.style.display = "block";
            });
    
            editButton.textContent = "Editar";
            editButton.removeAttribute("style");
            imagePacient.style.display = "block";
            firstSection.style.removeProperty("gap");
        });
    });

    editButton.addEventListener("click", function () {
        
        if (editButton.textContent === "Editar") {
            editFields.forEach((field) => {
                field.style.display = "block";
            });

            viewFields.forEach((field) => {
                field.style.display = "none";
            });

            editButton.textContent = "Salvar";
            editButton.style.backgroundColor = "var(--green-base)";
            editButton.style.color = "var(--background-white)";
            editButton.style.border = "none";
            editButton.style.fontWeight = "500";
            imagePacient.style.display = "none";
            firstSection.style.gap = "100px";
        } else if (editButton.textContent === "Salvar") {
            viewFields.forEach((field) => {
                field.style.display = "block";
            });

            editFields.forEach((field) => {
                field.style.display = "none";
            });

            editButton.textContent = "Editar";
            editButton.removeAttribute("style");
            imagePacient.style.display = "block";
            firstSection.style.removeProperty("gap");
        }
    });
});

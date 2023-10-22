document.addEventListener("DOMContentLoaded", function () {
    const editButton = document.querySelector("#editButton");
    const editFields = document.querySelectorAll(".edit-field");
    const viewFields = document.querySelectorAll(".view-field");
    const addServiceButton = document.getElementById("add-service");
    const listaServicos = document.getElementById("lista-servicos");
    const novoServicoInput = document.getElementById("novo-servico");

    function toggleServiceElementsVisibility(isEditing) {
        if (isEditing) {
            // Mostrar os campos de adição de serviço
            novoServicoInput.style.display = "block";
            addServiceButton.style.display = "block";

            // Mostrar os botões "X" para remover serviços existentes
            const deleteServiceButtons = document.querySelectorAll(".delete-service");
            deleteServiceButtons.forEach((button) => {
                button.style.display = "block";
            });
        } else {
            // Ocultar os campos de adição de serviço
            novoServicoInput.style.display = "none";
            addServiceButton.style.display = "none";

            // Ocultar os botões "X" para remover serviços existentes
            const deleteServiceButtons = document.querySelectorAll(".delete-service");
            deleteServiceButtons.forEach((button) => {
                button.style.display = "none";
            });
        }
    }

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
            editButton.style.color = "var(--background-white)";
            editButton.style.border = "none";
            editButton.style.fontWeight = "500";

            toggleServiceElementsVisibility(true);
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
            editButton.style = ""; // retorna ao padrão

            toggleServiceElementsVisibility(false);
        }
    });

    // Função para adicionar um novo serviço a partir do campo de input
    function addNewService() {
        const newService = novoServicoInput.value.trim(); // Pega o valor do campo de input

        if (newService) {
            const li = document.createElement("li");
            li.innerHTML = `${newService} <button class="delete-service" style="display: block;">x</button>`;
            listaServicos.appendChild(li);
            novoServicoInput.value = ""; // Limpa o campo de input após adicionar
            addDeleteServiceEvent(li.querySelector(".delete-service"));
        }
    }

    // Função para adicionar evento de clique aos botões "X" para excluir serviços
    function addDeleteServiceEvent(button) {
        button.addEventListener("click", function () {
            if (confirm("Tem certeza de que deseja excluir este serviço?")) {
                button.parentElement.remove(); // Remove o serviço
            }
        });
    }

    addServiceButton.addEventListener("click", addNewService);
});

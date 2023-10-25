document.addEventListener("DOMContentLoaded", function () {
    const addServiceButton = document.getElementById("add-service");
    const listaServicos = document.getElementById("lista-servicos");
    const novoServicoInput = document.getElementById("novo-servico");

   
    // Função para adicionar um novo serviço a partir do campo de input
    function addNewService() {
        const newService = novoServicoInput.value.trim(); // Get the value from the input field
    
        if (newService) {
            const li = document.createElement("li");
            li.innerHTML = `${newService} <button class="delete-service" style="display: block;">x</button>`;
            listaServicos.appendChild(li);
            novoServicoInput.value = ""; // Clear the input field after adding
            addDeleteServiceEvent(li.querySelector(".delete-service"));
        }
    }    

    function addDeleteServiceEvent(button) {
        button.addEventListener("click", function () {
            if (confirm("Tem certeza de que deseja excluir este serviço?")) {
                button.parentElement.remove(); // Remove o serviço
            }
        });
    }

    addServiceButton.addEventListener("click", addNewService);
});

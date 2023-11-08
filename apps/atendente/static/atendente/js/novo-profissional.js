document.addEventListener("DOMContentLoaded", function () {
    const addServiceButton = document.querySelector(".btn-confirm");
    const listaServicos = document.getElementById("lista-servicos");
    const novoServicoInput = document.getElementById("novo-servico");

    // Função para adicionar um novo serviço a partir do campo de input
    function addNewService(event) {
        event.preventDefault(); // Impede a submissão do formulário padrão

        const newService = novoServicoInput.value.trim(); // Obtém o valor do campo de input

        if (newService) {
            const li = document.createElement("li");
            li.innerHTML = `${newService} <button class="delete-service" style="display: block;">x</button>`;
            listaServicos.appendChild(li);
            novoServicoInput.value = ""; // Limpa o campo de input após adicionar
            addDeleteServiceEvent(li);
        }
    }

    function addDeleteServiceEvent(li) {
        const deleteButton = li.querySelector(".delete-service");
        deleteButton.addEventListener("click", function () {
            if (confirm("Tem certeza de que deseja excluir este serviço?")) {
                li.remove(); // Remove o serviço
            }
        });
    }

    addServiceButton.addEventListener("click", addNewService);

    // Adiciona eventos de exclusão para os serviços preexistentes
    const preexistentServices = listaServicos.querySelectorAll("li");
    preexistentServices.forEach(function (li) {
        addDeleteServiceEvent(li);
    });
});

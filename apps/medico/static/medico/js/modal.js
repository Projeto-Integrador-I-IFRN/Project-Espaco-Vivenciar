document.addEventListener("DOMContentLoaded", function () {
    const openModal = document.getElementById("abrirModal");
    const modal = document.getElementById("myModal");

        openModal.addEventListener("click", () => {
            console.log("open!!");
            modal.showModal();
        });
        // Adicione um ouvinte de eventos para o botão "Cancelar" dentro do conteúdo
        modal.addEventListener("click", (event) => {
            if (event.target.classList.contains("fecharModal")){
                modal.close();
            }
        });
});


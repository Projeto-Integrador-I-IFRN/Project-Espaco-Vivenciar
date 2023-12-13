// Dentro do seu arquivo medico/js/modal.js
document.addEventListener("DOMContentLoaded", function () {
    const abrirModal = document.getElementById("abrirModal");
    const abrirModal2 = document.getElementById("abrirModal2");
    const modal = document.getElementById("myModal");
    const modal2 = document.getElementById("myModal2");

    abrirModal.addEventListener("click", () => abrirModalHandler(modal));
    abrirModal2.addEventListener("click", () => abrirModalHandler(modal2));

    function abrirModalHandler(modal) {
        console.log(`Abrir Modal ${modal.id}!!`);

        modal.showModal();

        modal.addEventListener("click", (event) => {
            if (event.target.classList.contains("fecharModal")) {
                modal.close();
            }
        });
    }
});

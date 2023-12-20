document.addEventListener("DOMContentLoaded", function () {
    const abrirModal = document.getElementById("abrirModal");
    const abrirModal2 = document.getElementById("abrirModal2");
    const abrirModal3Elements = document.getElementsByClassName("abrirModal3");
    const modal = document.getElementById("myModal");
    const modal2 = document.getElementById("myModal2");
    const modal3 = document.getElementsByClassName("myModal3")[0]; // Selecting the first element

    // abrirModal.addEventListener("click", () => abrirModalHandler(modal));
    // abrirModal2.addEventListener("click", () => abrirModalHandler(modal2));

    for (const abrirModal3 of abrirModal3Elements) {
        abrirModal3.addEventListener("click", () => abrirModalHandler(modal3));
    }

    console.log('AAAA')

    function abrirModalHandler(modal) {
        if (typeof modal.showModal === 'function') {
            console.log(`Abrir Modal ${modal.id}!!`);

            modal.showModal();

            modal.addEventListener("click", (event) => {
                if (event.target.classList.contains("fecharModal")) {
                    modal.close();
                }
            });
        } else {
            console.error('Modal does not support the showModal method.');
        }
    }
});

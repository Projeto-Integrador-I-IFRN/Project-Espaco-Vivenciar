document.addEventListener("DOMContentLoaded", function () {
    const abrirModal = document.getElementById("abrirModal");
    const abrirModal4 = document.getElementById("abrirModal4");
    const abrirModal2Elements = document.getElementsByClassName("abrirModal2");
    const abrirModal3Elements = document.getElementsByClassName("abrirModal3");
    const modal = document.getElementById("myModal");
    const modal4 = document.getElementById("myModal4");
    const modal2 = document.getElementsByClassName("myModal2")[0];
    const modal3 = document.getElementsByClassName("myModal3")[0];


    if (abrirModal) {
        abrirModal.addEventListener("click", () => abrirModalHandler(modal));
    }

    if (abrirModal2Elements.length > 0) {
        for (const abrirModal2 of abrirModal2Elements) {
            abrirModal2.addEventListener("click", () => abrirModalHandler(modal2));
        }
    }

    if (abrirModal3Elements.length > 0) {
        for (const abrirModal3 of abrirModal3Elements) {
            abrirModal3.addEventListener("click", () => abrirModalHandler(modal3));
        }
    }

    if (abrirModal4) {
        abrirModal4.addEventListener("click", () => abrirModalHandler(modal4));
    }
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

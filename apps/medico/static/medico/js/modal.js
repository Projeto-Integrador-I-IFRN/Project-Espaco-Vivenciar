document.addEventListener("DOMContentLoaded", function () {
    const abrirModal = document.getElementById("abrirModal");
    const abrirModal4 = document.getElementById("abrirModal4");
    const abrirModal2Elements = document.getElementsByClassName("abrirModal2");
    const abrirModal3Elements = document.getElementsByClassName("abrirModal3");
    const abrirModal5Elements = document.getElementsByClassName("abrirModal5");
    const abrirModal6Elements = document.getElementsByClassName("abrirModal6");
    const abrirModal7Elements = document.getElementsByClassName("abrirModal7");

    const modal = document.getElementById("myModal");
    const modal4 = document.getElementById("myModal4");
    const modal2 = document.getElementsByClassName("myModal2")[0];
    const modal3 = document.getElementsByClassName("myModal3")[0];
    const modal5 = document.getElementsByClassName("myModal5")[0];
    const modal6 = document.getElementsByClassName("myModal6")[0];
    const modal7 = document.getElementsByClassName("myModal7")[0];


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

    if (abrirModal5Elements.length > 0) {
        for (const abrirModal5 of abrirModal5Elements) {
            abrirModal5.addEventListener("click", () => abrirModalHandler(modal5));
        }
    }

    if (abrirModal6Elements.length > 0) {
        for (const abrirModal6 of abrirModal6Elements) {
            abrirModal6.addEventListener("click", () => abrirModalHandler(modal6));
        }
    }

    if (abrirModal7Elements.length > 0) {
        for (const abrirModal7 of abrirModal7Elements) {
            abrirModal7.addEventListener("click", () => abrirModalHandler(modal7));
        }
        document.addEventListener('DOMContentLoaded', function () {

            const avatars = document.querySelectorAll('.circle-avatar');

            if (avatars.length > 0) {
                avatars.forEach((avatar, index) => {

                    const firstLetter = avatar.textContent.charAt(0);
                    const colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6'];

                    const colorIndex = firstLetter.charCodeAt(0) % colors.length;
                    avatar.style.backgroundColor = colors[colorIndex];
                });
            }
            console.log(`Porra`)
        });

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

$(document).ready(function () {
    // Função para obter as agendas do mês e atualizar a exibição
    function atualizarAgendas(mes) {
        // Você pode ajustar a URL conforme necessário
        var url = "/listar_agenda/" + mes + "/";
        
        // Use Ajax para buscar os dados do servidor
        $.ajax({
            url: url,
            type: "GET",
            success: function (data) {
                // Atualize a exibição com os dados retornados
                // (pode ser necessário ajustar dependendo da resposta do servidor)
                $("#conteudo-agendas").html(data);
            },
            error: function (error) {
                console.log("Erro ao obter as agendas: ", error);
            }
        });
    }

    // Inicialmente, atualize as agendas para o mês atual
    var mesAtual = new Date().getMonth() + 1; // +1 porque os meses são baseados em zero no JavaScript
    atualizarAgendas(mesAtual);

    // Lidar com os cliques nos botões de navegação
    $("#mes-anterior").click(function () {
        mesAtual--;
        if (mesAtual < 1) mesAtual = 12;
        atualizarAgendas(mesAtual);
        atualizarNomeMes();
    });

    $("#mes-posterior").click(function () {
        mesAtual++;
        if (mesAtual > 12) mesAtual = 1;
        atualizarAgendas(mesAtual);
        atualizarNomeMes();
    });

    // Função para atualizar o nome do mês exibido
    function atualizarNomeMes() {
        var nomeMeses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];
        $("#nome-mes").text(nomeMeses[mesAtual - 1]); // -1 porque os meses são baseados em zero no JavaScript
    }
});


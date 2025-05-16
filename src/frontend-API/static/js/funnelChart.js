(() => {
  let chartFunnel = null;
  let valores;
  let dataSalva;
  let labels;
  const mesesNomes = [
    "",
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro",
  ];

  document.addEventListener("DOMContentLoaded", () => {
    const canvas = document.getElementById("funnelChart");
    if (!canvas) {
      console.error('Canvas com id "funnelChart" não encontrado.');
      return;
    }

    const ctx = canvas.getContext("2d");
    chartFunnel = new Chart(ctx, {
      type: "bar",
      data: {
        labels: [],
        datasets: [
          {
            label: "Valor Agregado",
            data: [],
            backgroundColor: [
              "#043873",
              "#054285",
              "#065097",
              "#0760A9",
              "#0870BB",
            ],
            borderColor: "#043873",
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            title: { display: true, text: "Produtos", color: "#043873" },
            ticks: { color: "#043873" },
          },
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: "Valor agregado",
              color: "#043873",
            },
            ticks: { color: "#043873" },
          },
        },
        plugins: { legend: { display: false } },
      },
    });

    const button = document.getElementById("buttonSubmitFunnel");
    if (button) {
      button.addEventListener("click", function (event) {
        event.preventDefault();
        document.getElementById("loading").style.display = "flex";
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 180000);
        const formData = {
          tipo: document.getElementById("funnel-tipo").value,
          ano: document.getElementById("funnel-ano").value,
          mes: document.getElementById("funnel-mes").value,
          pais: document.getElementById("funnel-pais").value,
          municipio: document.getElementById("funnel-municipio").value,
        };

        fetch("http://127.0.0.1:5000/filtros_funil", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(formData),
          signal: controller.signal,
        })
          .then((response) => response.json())
          .then((receivedData) => {
            console.log("Dados recebidos:", receivedData);
            if (Array.isArray(receivedData)) {
              dataSalva = receivedData;
            } else if (receivedData && typeof receivedData === "object") {
              dataSalva = [receivedData];
            } else {
              console.error("Formato dos dados inesperado:", receivedData);
              return;
            }
            labels = dataSalva.map((d) => d.nome_produto || "Produto desconhecido");
            atualizarGrafico();
          })
          .catch((error) => {
            console.error("Erro ao enviar os dados:", error);
          })
          .finally(() => {
            document.getElementById("loading").style.display = "none";
            clearTimeout(timeoutId);
          });
      });
    }
  });

  function atualizarGrafico() {
    if (!dataSalva || !Array.isArray(dataSalva)) {
      console.error("Dados inválidos para atualizar o gráfico:", dataSalva);
      return;
    }
    valores = dataSalva.map((d) => d.total_valor_agregado);
    chartFunnel.data.datasets[0].label = "Valor agregado";
    chartFunnel.data.labels = labels;
    chartFunnel.data.datasets[0].data = valores;
    chartFunnel.update();
    console.log(
      "Gráfico atualizado com labels:",
      labels,
      "e valores:",
      valores
    );
  }
})();

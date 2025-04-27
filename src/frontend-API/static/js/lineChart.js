let chartLine = null; // gráfico global

const mesesNomes = [
  "", // índice 0 ignorado (mês começa no 1)
  "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
  "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
];
function filtosNomes() {
  const valor = document.querySelector('[name="metrica"]').value;
  return valor == 'valor_FOB' ? "Valor Fob" :
         valor == "total_registros" ? "Total Registros" :
         valor == "total_kg_liquido" ? "Total Kg Liquido" :
         "Valor Agregado";
}


document.addEventListener('DOMContentLoaded', () => {
  const canvas = document.getElementById('lineChart');
  const ctx = canvas.getContext('2d');

  chartLine = new Chart(ctx, {
    type: 'line',
    data: {
      labels: [], // atualizado dinamicamente
      datasets: [{
        label: 'Valor FOB',
        data: [],
        fill: false,
        borderColor: '#043873',
        backgroundColor: '#043873',
        tension: 0.3,
        pointRadius: 5,
        pointHoverRadius: 7
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: {
          title: {
            display: true,
            text: 'Mês ou Ano',
            color: '#043873'
          },
          ticks: { color: '#043873' }
        },
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: filtosNomes(),
            color: '#043873'
          },
          ticks: { color: '#043873' }
        }
      }
    }
  });

  const button = document.getElementById('buttonSubmitLine');
  if (button) {
    button.addEventListener('click', function(event) {
      event.preventDefault();

      document.getElementById('loading').style.display = 'flex';
      chartLine.options.scales.y.title.text= filtosNomes()
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 120000); // 2 min

      const formData = {
        tipo: document.querySelector('[name="tipo"]').value,
        ano: document.querySelector('[name="ano"]').value,
        mes: "todos",
        pais: document.querySelector('[name="pais"]').value,
        municipio: document.querySelector('[name="municipio"]').value
      };

      if (document.querySelector('[name="ncm"]').value != "") {
        formData["ncm"] = document.querySelector('[name="ncm"]').value;
      }

      console.log(formData)

      fetch('http://127.0.0.1:5000/filtros', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData),
        signal: controller.signal
      })
      .then(response => response.json())
      .then(data => {
        console.log('Dados recebidos:', data);
      
        const labels = data.map(d => {
          return d.mes ? mesesNomes[d.mes] : d.ano;
        });
        
        let valores = null;
        const metricaSelecionada = document.querySelector('[name="metrica"]').value;
        if(metricaSelecionada == 'valor_FOB'){
          valores = data.map(d => d.total_valor_fob);
          chartLine.data.datasets[0].label = 'Valor FOB';
       }else if(metricaSelecionada == 'total_registros'){
          valores = data.map(d => d.total_registros);
          chartLine.data.datasets[0].label = 'Total Registros';
       }else if(metricaSelecionada == 'total_kg_liquido'){
         valores = data.map(d => d.total_kg_liquido);
         chartLine.data.datasets[0].label = 'Total Kg Líquido'; 
       }else{
          valores = data.map(d => d.total_valor_agregado);
          chartLine.data.datasets[0].label = 'Valor Agregado';
       }
       
       
       chartLine.data.labels = labels;
       chartLine.data.datasets[0].data = valores;
       chartLine.update();
      })
      .catch(error => {
        console.error('Erro ao enviar os dados:', error);
      })
      .finally(() => {
        document.getElementById('loading').style.display = 'none';
        clearTimeout(timeoutId);
      });
    });
  }
});
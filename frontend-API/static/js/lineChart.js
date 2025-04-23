async function getData(data) {
  const url = "http://localhost:5000/filtros";
    fetch({
      method : "POST",
      body : data
    }).then( resposta => {
      console.log(resposta)
      return resposta.json()
    }).catch(error, ()=>{
      console.log(error)
    })
  }

document.querySelector('#buttonSubmitLine').addEventListener('submit', function(event) {
    event.preventDefault(); 
  
    const formData = {
      ano: document.querySelector('[name="ano"]').value,
      mes: document.querySelector('[name="mes"]').value,
      pais: document.querySelector('[name="pais"]').value,
      municipio: document.querySelector('[name="municipio"]').value,
      ncm: document.querySelector('[name="ncm"]').value
    };
  
    fetch('/filtros', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'  
      },
      body: JSON.stringify(formData)  
    })
    .then(response => response.json())
    .then(data => {
      console.log('Dados enviados com sucesso:', data);
    })
    .catch(error => {
      console.error('Erro ao enviar os dados:', error);
    });
  });



document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('lineChart')
    ctx = canvas.getContext('2d');
  
    const data = {
      labels: ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
      datasets: [{
        label: 'Exportações (em milhões USD)',
        data: [500, 520, 480, 510, 530, 600, 590, 560, 620, 650, 700],
        fill: false,
        borderColor: '#043873',
        backgroundColor: '#043873',
        tension: 0.3,
        pointRadius: 5,
        pointHoverRadius: 7
      }]
    };
  
    const options = {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: {
          title: {
            display: true,
            text: 'Ano',
            color: '#043873'
          },
          ticks: {
            color: '#043873'
          }
        },
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: 'Valor Exportado (USD)',
            color: '#043873'
          },
          ticks: {
            color: '#043873'
          }
        }
      },
    };
  
    new Chart(ctx, {
      type: 'line',
      data: data,
      options: options
    });

  });



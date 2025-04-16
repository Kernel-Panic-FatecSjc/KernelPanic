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
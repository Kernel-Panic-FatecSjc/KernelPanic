document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('funnelChart')
    ctx = canvas.getContext('2d');
  
    const data = {
      labels: ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
      datasets: [{
        label: 'Exportações (em milhões USD)',
        data: [500, 520, 480, 510, 530, 600, 590, 560, 620, 650, 700],
        backgroundColor: [
          '#043872', 
          '#1A4C8C', 
          '#3367A8', 
          '#5A8CC4', 
          '#8BB1E0',
          '#043872',
          '#1A4C8C',
          '#3367A8',
          '#5A8CC4',
          '#8BB1E0',
          '#043872'
        ],
        borderWidth: 0
      }]
    };
  
    const options = {
      responsive: true,
      maintainAspectRatio: false,
      indexAxis: 'y',
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
          title: {
            display: true,
            text: 'Ano',
            color: '#043873'
          },
          ticks: {
            color: '#043873'
          }
        }
      },
    };
  
    new Chart(ctx, {
      type: 'bar',
      data: data,
      options: options
    });
  });

  
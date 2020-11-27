function initialize_js_properties(globalJsProperties) {
    constructNoteLineChart(globalJsProperties.notes_monthly_count)
}

function constructNoteLineChart(notesMonthlyCount) {
    var ctx = document.getElementById('myChart').getContext('2d');

    var labels = [];
    notesMonthlyCount.forEach(element => labels.push(element.month_name));

    var data = [];
    notesMonthlyCount.forEach(element => data.push(element.notes_count));

    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            labels: labels,
            datasets: [{
                label: 'My First dataset',
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: data
            }]
        },

        // Configuration options go here
        options: {}
    });
}


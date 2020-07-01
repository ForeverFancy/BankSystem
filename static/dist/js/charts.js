// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

function get_data(build_chart) {
    $.ajax({
        url: '/api/statisticaldata/',
        dataType: 'json',
        type: 'GET',
        success: function (data) {
            // console.log(data);
            build_chart(data);
            // return data;
        },
        error: function () {
            console.log("error");
        }
    });
}

function build_chart(data) {
    console.log(data);
    for (let index = 0; index <= 6; index++) {
        var years = [];
        var years_saving_amount = [];
        var years_loan_amount = [];
        var years_customer_amount = [];
        
        // console.log(data['month_data'][index]);
        for (const prop in data['year_data'][index]) {
            years.push(`${prop}`.toString());
            years_saving_amount.push(`${data['year_data'][index][prop][0]}`);
            years_loan_amount.push(`${data['year_data'][index][prop][1]}`);
            years_customer_amount.push(`${data['year_data'][index][prop][2]}`);
            // console.log(`${prop}, ${data['year_data'][index][prop]}`);
        }
        var ctx = document.getElementById("myAreaChart" + (index + 1) + "_1");
        var myLineChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: years,
                datasets: [{
                    label: "Overall Savings Amount",
                    lineTension: 0.3,
                    pointRadius: 2,
                    pointHoverRadius: 2,
                    borderColor: "#3e95cd",
                    pointHitRadius: 50,
                    pointBorderWidth: 2,
                    fill: false,
                    data: years_saving_amount,
                }, {
                    label: "Overall Loan Amount",
                    lineTension: 0.3,
                    borderColor: "#c45850",
                    pointRadius: 2,
                    pointHoverRadius: 2,
                    pointHitRadius: 50,
                    pointBorderWidth: 2,
                    fill: false,
                    data: years_loan_amount,
                    }, {
                        label: "Overall Customer Amount",
                        lineTension: 0.3,
                        borderColor: "#8e5ea2",
                        pointRadius: 2,
                        pointHoverRadius: 2,
                        pointHitRadius: 50,
                        pointBorderWidth: 2,
                        fill: false,
                        data: years_customer_amount,
                    }],
            },
            options: {
                scales: {
                    xAxes: [{
                        time: {
                            unit: 'date'
                        },
                        gridLines: {
                            display: false
                        },
                        ticks: {
                            maxTicksLimit: 2
                        }
                    }],
                    yAxes: [{
                        ticks: {
                            min: 0,
                            max: Math.max(Math.max.apply(Math, years_customer_amount), Math.max.apply(Math, years_loan_amount), Math.max.apply(Math, years_saving_amount)) + 16,
                            maxTicksLimit: 5
                        },
                        gridLines: {
                            color: "rgba(0, 0, 0, .125)",
                        }
                    }],
                },
                title: {
                    display: true,
                    text: 'Year statistical data'
                },
                legend: {
                    display: false
                }
            }
        });

        var quarters = [];
        var quarters_saving_amount = [];
        var quarters_loan_amount = [];
        var quarters_customer_amount = [];

        // console.log(data['month_data'][index]);
        for (const prop in data['quarter_data'][index]) {
            quarters.push(`${prop}`.toString());
            quarters_saving_amount.push(`${data['quarter_data'][index][prop][0]}`);
            quarters_loan_amount.push(`${data['quarter_data'][index][prop][1]}`);
            quarters_customer_amount.push(`${data['quarter_data'][index][prop][2]}`);
            // console.log(`${prop}, ${data['quarter_data'][index][prop]}`);
        }
        var ctx = document.getElementById("myAreaChart" + (index + 1) + "_2");
        var myLineChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: quarters,
                datasets: [{
                    label: "Overall Savings Amount",
                    lineTension: 0.3,
                    pointRadius: 2,
                    pointHoverRadius: 2,
                    borderColor: "#3e95cd",
                    pointHitRadius: 50,
                    pointBorderWidth: 2,
                    fill: false,
                    data: quarters_saving_amount,
                }, {
                    label: "Overall Loan Amount",
                    lineTension: 0.3,
                    borderColor: "#c45850",
                    pointRadius: 2,
                    pointHoverRadius: 2,
                    pointHitRadius: 50,
                    pointBorderWidth: 2,
                    fill: false,
                    data: quarters_loan_amount,
                }, {
                    label: "Overall Customer Amount",
                    lineTension: 0.3,
                    borderColor: "#8e5ea2",
                    pointRadius: 2,
                    pointHoverRadius: 2,
                    pointHitRadius: 50,
                    pointBorderWidth: 2,
                    fill: false,
                    data: quarters_customer_amount,
                }],
            },
            options: {
                scales: {
                    xAxes: [{
                        time: {
                            unit: 'date'
                        },
                        gridLines: {
                            display: false
                        },
                        ticks: {
                            maxTicksLimit: 2
                        }
                    }],
                    yAxes: [{
                        ticks: {
                            min: 0,
                            max: Math.max(Math.max.apply(Math, quarters_customer_amount), Math.max.apply(Math, quarters_loan_amount), Math.max.apply(Math, quarters_saving_amount)) + 16,
                            maxTicksLimit: 5
                        },
                        gridLines: {
                            color: "rgba(0, 0, 0, .125)",
                        }
                    }],
                },
                title: {
                    display: true,
                    text: 'Quarter statistical data'
                },
                legend: {
                    display: false
                }
            }
        });

        var months = [];
        var months_saving_amount = [];
        var months_loan_amount = [];
        var months_customer_amount = [];

        // console.log(data['month_data'][index]);
        for (const prop in data['month_data'][index]) {
            months.push(`${prop}`.toString());
            months_saving_amount.push(`${data['month_data'][index][prop][0]}`);
            months_loan_amount.push(`${data['month_data'][index][prop][1]}`);
            months_customer_amount.push(`${data['month_data'][index][prop][2]}`);
            // console.log(`${prop}, ${data['month_data'][index][prop]}`);
        }
        var ctx = document.getElementById("myAreaChart" + (index + 1) + "_3");
        var myLineChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: months,
                datasets: [{
                    label: "Overall Savings Amount",
                    lineTension: 0.3,
                    pointRadius: 2,
                    pointHoverRadius: 2,
                    borderColor: "#3e95cd",
                    pointHitRadius: 50,
                    pointBorderWidth: 2,
                    fill: false,
                    data: months_saving_amount,
                }, {
                    label: "Overall Loan Amount",
                    lineTension: 0.3,
                    borderColor: "#c45850",
                    pointRadius: 2,
                    pointHoverRadius: 2,
                    pointHitRadius: 50,
                    pointBorderWidth: 2,
                    fill: false,
                    data: months_loan_amount,
                }, {
                    label: "Overall Customer Amount",
                    lineTension: 0.3,
                    borderColor: "#8e5ea2",
                    pointRadius: 2,
                    pointHoverRadius: 2,
                    pointHitRadius: 50,
                    pointBorderWidth: 2,
                    fill: false,
                    data: months_customer_amount,
                }],
            },
            options: {
                scales: {
                    xAxes: [{
                        time: {
                            unit: 'date'
                        },
                        gridLines: {
                            display: false
                        },
                        ticks: {
                            maxTicksLimit: 7
                        }
                    }],
                    yAxes: [{
                        ticks: {
                            min: 0,
                            max: Math.max(Math.max.apply(Math, years_customer_amount), Math.max.apply(Math, years_loan_amount), Math.max.apply(Math, years_saving_amount)) + 16,
                            maxTicksLimit: 5
                        },
                        gridLines: {
                            color: "rgba(0, 0, 0, .125)"
                        }
                    }],
                },
                title: {
                    display: true,
                    text: 'Month statistical data'
                },
                legend: {
                    display: false
                }
            }
        });
    }
}

get_data(build_chart);

// Area Chart Example



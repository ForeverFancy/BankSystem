/*!
    * Start Bootstrap - SB Admin v6.0.1 (https://startbootstrap.com/templates/sb-admin)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
(function ($) {
    "use strict";

    // Add active state to sidbar nav links
    var path = window.location.href; // because the 'href' property of the DOM element is the absolute path
    $("#layoutSidenav_nav .sb-sidenav a.nav-link").each(function () {
        if (this.href === path) {
            $(this).addClass("active");
        }
    });

    // Toggle the side navigation
    $("#sidebarToggle").on("click", function (e) {
        e.preventDefault();
        $("body").toggleClass("sb-sidenav-toggled");
    });

    function get_data(build_table) {
        $.ajax({
            url: '/api/statisticaldata/',
            dataType: 'json',
            type: 'GET',
            success: function (data) {
                // console.log(data);
                build_table(data);
                // return data;
            },
            error: function () {
                console.log("error");
            }
        });
    }

    function build_table(data) {
        console.log(data);
        for (let index = 0; index <= 6; index++) {
            var bk_data = [];
            // console.log(data['month_data'][index]);
            for (const prop in data['year_data'][index]) {
                bk_data.push({ Date: `${prop}`, Overall_Savings_Amount: `${data['year_data'][index][prop]}`, Overall_Loan_Amount: 0, Overall_Customer_Amount: 0 });
                // console.log(`${prop}, ${data['month_data'][index][prop]}`);
            }
            for (const prop in data['quarter_data'][index]) {
                bk_data.push({ Date: `${prop}`, Overall_Savings_Amount: `${data['quarter_data'][index][prop]}`, Overall_Loan_Amount: 0, Overall_Customer_Amount: 0 });
                // console.log(`${prop}, ${data['month_data'][index][prop]}`);
            }
            for (const prop in data['month_data'][index]) {
                bk_data.push({ Date: `${prop}`, Overall_Savings_Amount: `${data['month_data'][index][prop]}`, Overall_Loan_Amount: 0, Overall_Customer_Amount: 0});
                // console.log(`${prop}, ${data['month_data'][index][prop]}`);
            }
            console.log(bk_data);
            $('#myTable'+(index+1)).dataTable({
                "aaData": bk_data,
                "columns": [

                    { "data": "Date" },
                    { "data": "Overall_Savings_Amount" },
                    { "data": "Overall_Loan_Amount" },
                    { "data": "Overall_Customer_Amount" }

                ]
            })
            
        }
    }

    get_data(build_table);

    // $(document).ready(function () {
    //     $.ajax({
    //         'url': '/api/banks/',
    //         'dataType': "json",
    //         'type': "GET",
    //     }).done(function (data) {
    //         console.log(JSON.parse(JSON.stringify(data)));
            
    //     })
    // })

})(jQuery);

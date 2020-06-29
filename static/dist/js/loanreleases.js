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

    $(document).ready(function () {
        $.ajax({
            'url': '/api/loanreleases/',
            'dataType': "json",
            'type': "GET",
        }).done(function (data) {
            console.log(JSON.parse(JSON.stringify(data)));
            $('#myTable').dataTable({
                "aaData": data,
                "columns": [

                    { "data": "Loan_Release_ID" },
                    { "data": "Loan_Release_Date" },
                    { "data": "Loan_Release_Amount" },
                    { "data": "Loan_ID" }

                ]
            })
        })
    })

})(jQuery);

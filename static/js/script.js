$(document).ready(function() {
    $('.carousel').carousel({
        interval: 8000
    })

    $("#search-field").autocomplete({
        source: function(request, response) {
            $.ajax({
                type: "get",
                data: {
                    query: $("#search-field").val()
                },
                url: "/products/search_products",
                success: function(ajaxData) {
                    response($.map(ajaxData, function (item) {
                        return {
                            value: item.name,
                            data: item.id
                        }
                    }));
                }
            }); 
        } 
    });
    $("#contact-form").submit(function(event) {
        name = $("#fullname").val();
        email = $("#emailaddress").val();
        message = $("#question_request").val();
        emailjs.send("gmail", "hb_questions", {
            "from_name": name,
            "from_email": email,
            "question_request": message
        },"user_dsCSw90ZDaXXXvAJiHBcR")
        .then(
            function(response) {
                $("#fullname").val("");
                $("#emailaddress").val("");
                $("#question_request").val("");
                $(".alert").removeClass('hide').addClass('show')
                console.log("SUCCESS", response);
            },
            function(error) {
                console.log("FAILED", error);
            }
        );
        return false;
    });

    $("#reset-password").submit(function(event) {
        email = $("input[name='email'").val();
        resetUrl = $("input[name='reset_url'").val();
        console.log(email);
        console.log(resetUrl);
        emailjs.send("gmail", "password_reset_request", {
            "from_email": email,
            "reset_url": resetUrl
        },"user_r7tdLbadZRBs7vClusXBr")
        .then(
            function(response) {
                $("#emailaddress").val("");
                $(".alert").removeClass('hide').addClass('show')
                document.location = "/"
                console.log("SUCCESS", response);
            },
            function(error) {
                console.log("FAILED", error);
            }
        );
        return false;
    });
});


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
});


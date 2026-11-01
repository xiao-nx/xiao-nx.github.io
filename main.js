$(initDropDown);

var currentDropDown = null;

$(document).on("click", function() {
    $(".menu-items").hide();
    currentDropDown = null;
});

function initDropDown() {
    $(".menu-drop-down").click(function(e) {
        var t = $(this).find(".menu-items");
        if (t.is(":hidden")) {
            t.show();
            if (currentDropDown != null && currentDropDown != t) {
                currentDropDown.hide();
            }
            currentDropDown = t;
            e.stopPropagation();
        }
    });

    $(".menu-items > div, .nav-button").click(function (e) {
        var href = $(this).attr("href");
        if (href) {
            console.log(href, );
            var url = window.location.href;
            var t = url.split("/");
            console.log(t);
            t[t.length - 1] = href + ".html";
            url = t.join("/");
            window.location = url;
        }
    });
}
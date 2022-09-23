$(document).ready(function () {
            $("#animation").bind("click", function (event) {
                $(event.target).parent().css("center");
                $(event.target).animate({
                    width: $(event.target).width() * 2,
                    height: $(event.target).height() * 2,
                }, 2000);

            $(event.target).animate({
                    width: $(event.target).width(),
                    height: $(event.target).height(),
                }, 2000);
            });
        });
$(document).ready(function() {

    var csrftoken = $.cookie('csrftoken');

    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $(".vote-up").click(function(){
        var postId = $(this).closest('.post').attr('id');
        var downVoteElement = $(this).closest('.vote-section').find('.vote-down')
        var isUpClicked = $(this).hasClass('clicked');
        var isDownClicked = downVoteElement.hasClass('clicked');
        var pointElement = $(this).closest('.post').children('.ribbon')
        var points = parseInt(pointElement.text());
        var diff = 0;
        if (isUpClicked) {
            pointElement.text(points - 1);
            diff = -1;
        } else if (isDownClicked) {
            pointElement.text(points + 2);
            downVoteElement.removeClass('clicked');
            diff = 2;
        } else {
            pointElement.text(points + 1);
            diff = 1;
        };

      // TODO: AJAX CALL TO UPDATE POINTS
        $(this).toggleClass('clicked');
        $.ajax({
            type: 'POST',
            url: 'vote/',
            data: {
                'diff': diff,
                'postId': postId,
                'isDownClicked': false,
                'isUpClicked': $(this).hasClass('clicked')
            },
        });
    });

    $(".vote-down").click(function(){
        var postId = $(this).closest('.post').attr('id');
        var upVoteElement = $(this).closest('.vote-section').find('.vote-up')
        var isDownClicked = $(this).hasClass('clicked');
        var isUpClicked = upVoteElement.hasClass('clicked');
        var pointElement = $(this).closest('.post').children('.ribbon')
        var points = parseInt(pointElement.text());
        var diff = 0;
        if (isDownClicked) {
            pointElement.text(points + 1);
            diff = 1;
        } else if (isUpClicked) {
            pointElement.text(points - 2);
            upVoteElement.removeClass('clicked');
            diff = -2;
        } else {
            pointElement.text(points - 1);
            diff = -1;
        };
        $(this).toggleClass('clicked');
        $.ajax({
            type: 'POST',
            url: 'vote/',
            data: {
                'diff': diff,
                'postId': postId,
                'isDownClicked': $(this).hasClass('clicked'),
                'isUpClicked': false
            },
        });
    });

    $("#bp-wrapper").mouseover(function() {
        $("#bp-logo").addClass("rotate");
    }).mouseout(function() {
        $("#bp-logo").removeClass("rotate");
    });

    (function($) {
        $.fn.extend( {
            limiter: function(limit, elem) {
                $(this).on("keyup focus", function() {
                    setCount(this, elem);
                });
                function setCount(src, elem) {
                    var chars = src.value.length;
                    if (chars > limit) {
                        src.value = src.value.substr(0, limit);
                        chars = limit;
                    }
                    elem.html( limit - chars );
                }
                setCount($(this)[0], elem);
            }
        });
    })(jQuery);

    var elem = $("#char-length");
    $("#message").limiter(100, elem);

    $('#submit').attr('disabled',true);
    $('#message').keyup(function(){
        if ($.trim($(this).val()).length != 0) {
            $('#submit').attr('disabled', false);
        }
        else {
            $('#submit').attr('disabled', true);
        }
    });
});

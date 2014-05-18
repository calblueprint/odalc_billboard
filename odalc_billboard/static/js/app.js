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
        var downVoteElement = $(this).closest('.vote-buttons').find('.vote-down')
        var isUpClicked = $(this).hasClass('clicked');
        var isDownClicked = downVoteElement.hasClass('clicked');
        var pointElement = $(this).closest('.points-section').children('.points')
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
        $.ajax({
            type: 'POST',
            url: 'vote/',
            data: {
                'diff': diff,
                'postId': postId
            },
        });
        $(this).toggleClass('clicked');
    });

    $(".vote-down").click(function(){
        var postId = $(this).closest('.post').attr('id');
        var upVoteElement = $(this).closest('.vote-buttons').find('.vote-up')
        var isDownClicked = $(this).hasClass('clicked');
        var isUpClicked = upVoteElement.hasClass('clicked');
        var pointElement = $(this).closest('.points-section').children('.points')
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
        $.ajax({
            type: 'POST',
            url: 'vote/',
            data: {
                'diff': diff,
                'postId': postId
            },
        });
        $(this).toggleClass('clicked');
    });
});

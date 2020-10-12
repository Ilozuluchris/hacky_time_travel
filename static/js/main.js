 $(document).ready(function(){
              $('.owl-carousel').owlCarousel({
                  'nav': true,
                  'items':1,
                  'navText':['<button id="prev_btn" onclick="time_jump(this)" style="background-color: #e44c65" class="btn">Jump Backward</button>', '&ensp;&ensp;<button id="next_btn" onclick="time_jump(this)" style="background-color: #e44c65;" class="btn float-right">Jump Forward</button>'],
                  'onTranslate':handle_time_jump_btns,
                  'onInitialized':intit
              });
 });

function intit() {
            $("#prev_btn").prop("disabled", true);
}

function  handle_time_jump_btns(event) {
    var item      = event.item.index;     // Position of the current item
    (item === 0) ? $("#prev_btn").prop("disabled", true) : $("#prev_btn").prop("disabled", false);
    (item === event.item.count-1) ? $("#next_btn").prop("disabled", true) : $("#next_btn").prop("disabled", false);
}

function time_jump(event) {
    //todo: does this download everytime
    var myAudioElement = document.getElementById('time_jump_sound');

    myAudioElement.play();

    myAudioElement.addEventListener('play', (event) => {
        $("#main").hide();
        $(".mesh-loader").show();
    });

    myAudioElement.addEventListener('ended', (event) => {
        $(".mesh-loader").fadeOut();
        $("#main").fadeIn();

    })

}

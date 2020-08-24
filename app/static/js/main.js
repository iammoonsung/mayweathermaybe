$(".categories").click(function(e){
    e.preventDefault();
});

$(".gobacks").click(function(e){
    e.preventDefault();
});

$(".category0").click(function(){
    $(".products0").animate({width:"toggle"},300);
});

$(".goback0").click(function(){
    $(".products0").animate({width:"toggle"},300);
})

$(".category1").click(function(){
    $(".products1").animate({width:"toggle"},300);
});

$(".goback1").click(function(){
    $(".products1").animate({width:"toggle"},300);
})

$(".category2").click(function(){
    $(".products2").animate({width:"toggle"},300);
});

$(".goback2").click(function(){
    $(".products2").animate({width:"toggle"},300);
})

$(".category3").click(function(){
    $(".products3").animate({width:"toggle"},300);
});

$(".goback3").click(function(){
    $(".products3").animate({width:"toggle"},300);
})

$(".category4").click(function(){
    $(".products4").animate({width:"toggle"},300);
});

$(".goback4").click(function(){
    $(".products4").animate({width:"toggle"},300);
})

function doChild() {
    var here = document.querySelector("#here");
    here.innerHTML = "";
    var cnt = document.getElementById("childNum").value;
    var i = 0;
    for (i=0; i<cnt; i++) {
        here.innerHTML += $("#childbox"+i).html();
    }
}

var lastScrollTop = 0;
var delta = 5;
var navbarHeight = $('.nav_index').outerHeight();

var didScroll;
$(window).scroll(function(event){
    didScroll = true;
});

setInterval(function() {
    if (didScroll) {
        hasScrolled();
        didScroll = false;
    }
}, 250);

function hasScrolled() {
    var st = $(this).scrollTop();
    if (Math.abs(lastScrollTop - st) <= delta)
        return;
    if (st > lastScrollTop && st > navbarHeight) {
        $('.nav_index').removeClass('nav-down').addClass('nav-up');
    } else {
        if (st + $(window).height() < $(document).height()) {
            $('.nav_index').removeClass('nav-up').addClass('nav-down');
        }
    }
    lastScrollTop = st;
}
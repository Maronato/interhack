var header = document.getElementById("main-header");
var menu = document.getElementById("main-menu");
var faded = false;
document.onscroll = function() {
    var headerHeight = header.offsetHeight;
    if (document.body.scrollTop > headerHeight) {
        if (!faded) {
            menu.style.background = "rgba(0, 0, 0, 0.74)";
            faded = true;
        }
    } else if (faded) {
        menu.style.background = "rgba(0, 0, 0, 0)";
        faded = false;
    }
}

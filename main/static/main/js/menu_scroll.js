var expanded = false;
var menuitems = document.getElementsByClassName("menu-item");
var menucontrol = document.getElementsByClassName("menu-control")[0];
var i = 0;
function toggleMenu() {
    if (expanded) {
        for (i = 0; i < menuitems.length; i++) {
            var item = menuitems[i];
            item.style.height = "0px";
            item.style.opacity = "0";
        }
        menucontrol.style.transform = "rotate(0deg)";
        menucontrol.style.textAlign = "left";
        menucontrol.style.marginBottom = "0px";
        expanded = false;
    } else {
        for (i = 0; i < menuitems.length; i++) {
            var item = menuitems[i];
            item.style.height = "55px";
            item.style.opacity = "1";
        }
        menucontrol.style.transform = "rotate(180deg)";
        menucontrol.style.textAlign = "right";
        menucontrol.style.marginBottom = "20px";
        expanded = true;
    }
}

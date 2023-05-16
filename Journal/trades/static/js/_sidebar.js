const sidebar = document.getElementsByClassName("sidebar")[0];
const full_page = document.getElementById("full_page");


function myFunction() {
    console.log(sidebar);
    if (sidebar.style.display == "none") {
        sidebar.style.display = "block"
        full_page.style.gridTemplateColumns = "3fr 1fr 21fr";
    }
    else {
        sidebar.style.display = "none"
        full_page.style.gridTemplateColumns = " 1fr 13fr"
    }


}
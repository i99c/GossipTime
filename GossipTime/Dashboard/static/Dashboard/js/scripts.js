let hamburgerBtn = document.querySelector('.hamburger-btn')
let sideBar = document.querySelector('.side-bar')

hamburgerBtn.addEventListener('click', sidebarToggle);
function sidebarToggle() {
    sideBar.classList.toggle('active');
}
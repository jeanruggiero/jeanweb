function showMenu() {
    let navList = document.getElementById('nav-list');
    let menuBar = document.getElementById('show-menu-div');
    let menuIcon = document.getElementById('menu-icon');

    if (navList.style.display === 'block') {
        navList.style.display = 'none';
        menuBar.style.backgroundColor = '#FFFFFF';
        menuBar.style.paddingBottom = '0';
        menuIcon.src = '/static/icons/menu_icon.svg';
    } else {
        navList.style.display = 'block';
        menuBar.style.backgroundColor = '#333333';
        menuBar.style.paddingBottom = '20px';
        menuIcon.src = '/static/icons/menu_icon_white.svg';

    }
}


window.addEventListener('resize', function() {
    let navList = document.getElementById('nav-list');

    if (window.innerWidth >= 630) {
        navList.style.display = 'block';
    } else {
        navList.style.display = 'none';
    }
}, false);
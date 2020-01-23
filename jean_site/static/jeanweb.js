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
    let menuBar = document.getElementById('show-menu-div');
    let menuIcon = document.getElementById('menu-icon');

    menuBar.style.backgroundColor = '#FFFFFF';
    menuBar.style.paddingBottom = '0';
    menuIcon.src = '/static/icons/menu_icon.svg';

    if (window.innerWidth >= 630) {
        navList.style.display = 'block';
    } else {
        navList.style.display = 'none';
    }
}, false);

//
// function filterProjects() {
//     let codeProjects = document.getElementsByClassName('code');
//     let designProjects = document.getElementsByClassName('design');
//     let engineeringProjects = document.getElementsByClassName('engineering');
//
//     let codeBox = document.getElementById('code-box');
//     let designBox = document.getElementById('design-box');
//     let engineeringBox = document.getElementById('engineering-box');
//
//     if (!codeBox.checked) {
//         for (let project of codeProjects) {
//             project.style.display = 'none';
//         }
//     } else {
//         for (let project of codeProjects) {
//             project.style.display = 'block';
//         }
//     }
//
//     if (!designBox.checked) {
//         for (let project of designProjects) {
//             project.style.display = 'none';
//         }
//     } else {
//         for (let project of designProjects) {
//             project.style.display = 'block';
//         }
//     }
//
//     if (!engineeringBox.checked) {
//         for (let project of engineeringProjects) {
//             project.style.display = 'none';
//         }
//     } else {
//         for (let project of engineeringProjects) {
//             project.style.display = 'block';
//         }
//     }
// }
//
//
// window.onload = function() {
//     document.getElementById('code-box').addEventListener('change', filterProjects);
//     document.getElementById('design-box').addEventListener('change', filterProjects);
//     document.getElementById('engineering-box').addEventListener('chang', filterProjects);
// };
//


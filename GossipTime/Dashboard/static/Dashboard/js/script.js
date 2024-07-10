let hamburgerBtn = document.querySelector('.hamburger-btn')
let sideBar = document.querySelector('.side-bar')

hamburgerBtn.addEventListener('click', sidebarToggle);
function sidebarToggle() {
    sideBar.classList.toggle('active');
}

function previewImage(event) {
    const reader = new FileReader();
    reader.onload = function () {
        const output = document.getElementById('author-image');
        output.src = reader.result;
    };
    reader.readAsDataURL(event.target.files[0]);
}

function editAuthorDetails() {
    const authorBody = document.querySelector('.author-body');
    const subtitle = authorBody.querySelector('.subtitle').textContent;
    const title = authorBody.querySelector('.title').textContent;
    const bio = authorBody.querySelector('.author-inner-text').textContent;

    authorBody.innerHTML = `
        <div class="edit-container">
            <input type="text" class="subtitle-input" value="" />
            <i class="fas fa-save save-icon" onclick="saveAuthorDetails()"></i>
        </div>
        <input type="text" class="title-input" value="${title}" />
        <textarea rows='2' class="bio-input">${bio}</textarea>
        <div class="social-share-author-2">
            <a href="#"><i class="fab fa-instagram"></i></a>
            <a href="#"><i class="fab fa-twitter"></i></a>
        </div>
    `;
}

function saveAuthorDetails() {
    const authorBody = document.querySelector('.author-body');
    const subtitle = authorBody.querySelector('.subtitle-input').value;
    const title = authorBody.querySelector('.title-input').value;
    const bio = authorBody.querySelector('.bio-input').value;

    authorBody.innerHTML = `
        <div class="edit-container">
            <span class="subtitle">${subtitle}</span>
            <i class="fas fa-edit edit-icon" onclick="editAuthorDetails()"></i>
        </div>
        <h5 class="title">${title}</h5>
        <p class="author-inner-text">${bio}</p>
        <div class="social-share-author">
            <a href="#"><i class="fab fa-instagram"></i></a>
            <a href="#"><i class="fab fa-twitter"></i></a>
        </div>
    `;
}



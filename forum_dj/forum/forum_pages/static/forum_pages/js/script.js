const textContainers = document.querySelectorAll('.side__panel-text');

textContainers.forEach(textContainer => {
  if (textContainer.textContent.length > 100) {
    textContainer.textContent = textContainer.textContent.slice(0, 100) + '...';
  }
});
// Отримуємо всі елементи dropdown на сторінці
var dropdowns = document.getElementsByClassName("dropdown");

// Додаємо обробник події для закриття відкритого dropdown при кліку на вільне місце на сторінці
document.addEventListener("click", function(event) {
    for (var i = 0; i < dropdowns.length; i++) {
        var dropdown = dropdowns[i];
        var content = dropdown.getElementsByClassName("dropdown-content")[0];
        
        // Перевіряємо, чи користувач клікнув поза dropdown
        if (content.style.display === "block" && !dropdown.contains(event.target)) {
            content.style.display = "none";
        }
    }
});

// Додаємо обробник події для відкривання і закриття dropdown при кліку на кнопку
for (var i = 0; i < dropdowns.length; i++) {
    var dropdown = dropdowns[i];
    var button = dropdown.getElementsByClassName("dropdown-button")[0];
    var content = dropdown.getElementsByClassName("dropdown-content")[0];

    button.addEventListener("click", function(event) {
        event.stopPropagation(); // Зупиняємо подальше розповсюдження події кліку, щоб вона не спрацювала на document
        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
}
window.addEventListener('DOMContentLoaded', () => {
    const menu = document.querySelector('.header__links'),
        menuItem = document.querySelectorAll('.header__link'),
        logoItem = document.querySelector('.header__logo'),
        hamburger = document.querySelector('.hamburger'),
        dropdownMenu = document.querySelector('.dropdown__menu'),
        authBlock = document.querySelector('.header__auth');

    // Функція для перевірки розширення вікна та обробки блоку .header__auth
    const handleAuthBlock = () => {
        if (authBlock) {
            if (window.innerWidth <= 768) {
                menu.appendChild(authBlock);
                authBlock.style.display = 'none';
            } else {
                document.querySelector('.container').appendChild(authBlock);
                authBlock.style.display = 'flex';
            }
        }
    };

    // Викликаємо функцію при завантаженні сторінки
    handleAuthBlock();

    // Додаємо обробник для реагування на зміну розміру вікна
    window.addEventListener('resize', () => {
        handleAuthBlock();
    });

    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('_active');
        menu.classList.toggle('_active');

        // Додаємо видалення _active та переміщення елементів для .header__auth
        if (authBlock) {
            if (hamburger.classList.contains('_active')) {
                menu.appendChild(authBlock);
                authBlock.style.display = 'flex';
            } else {
                document.querySelector('.container').appendChild(authBlock);
                authBlock.style.display = 'none';
            }
        }

        // Перевіряємо, чи dropdownMenu не є null перед роботою з ним
        if (dropdownMenu) {
            // Додаємо видалення _active та переміщення елементів для .dropdown__menu
            if (hamburger.classList.contains('_active')) {
                menu.appendChild(dropdownMenu);
                dropdownMenu.style.display = 'block';
            } else {
                document.querySelector('.container').appendChild(dropdownMenu);
                dropdownMenu.style.display = 'none';
            }
        }
    });

    menuItem.forEach(item => {
        item.addEventListener('click', () => {
            hamburger.classList.toggle('_active');
            menu.classList.toggle('_active');

            if (authBlock) {
                authBlock.classList.remove('_active');
                document.querySelector('.container').appendChild(authBlock);
                authBlock.style.display = 'none';
            }

            if (dropdownMenu) {
                dropdownMenu.style.display = 'none';
            }
        });
    });
});


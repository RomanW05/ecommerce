function toggleNav() {
    const nav = document.querySelector('.nav-links');
    nav.classList.toggle('nav-active');
  }

function toggleScrollButton() {
    const scrollButton = document.querySelector('.scroll-to-top');
    if (document.documentElement.scrollTop > 100) {
      scrollButton.style.display = 'block';
    } else {
      scrollButton.style.display = 'none';
    }
  }
  
  window.addEventListener('scroll', toggleScrollButton);

  
function validateForm(event) {
    const form = event.target;
    const name = form.querySelector('#name').value;
    const email = form.querySelector('#email').value;
    const message = form.querySelector('#message').value;
  
    if (!name || !email || !message) {
      alert('Please fill out all fields before submitting the form.');
      event.preventDefault();
    }
  }
  
const form = document.querySelector('form');
form.addEventListener('submit', validateForm);

  
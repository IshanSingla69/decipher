const toggleButton = document.querySelector('.dark-light');
const colors = document.querySelectorAll('.color');
// window.onload = function() {
//   document.body.classList.toggle('dark-mode');
// };
document.body.classList.toggle('dark-mode');
colors.forEach(color => {
  color.addEventListener('click', e => {
    colors.forEach(c => c.classList.remove('selected'));
    const theme = color.getAttribute('data-color');
    document.body.setAttribute('data-theme', theme);
    color.classList.add('selected');
  });
});

toggleButton.addEventListener('click', () => {
  document.body.classList.toggle('dark-mode');
});



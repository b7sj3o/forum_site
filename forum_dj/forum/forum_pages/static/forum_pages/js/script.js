const textContainers = document.querySelectorAll('.side__panel-text');

textContainers.forEach(textContainer => {
  if (textContainer.textContent.length > 100) {
    textContainer.textContent = textContainer.textContent.slice(0, 100) + '...';
  }
});
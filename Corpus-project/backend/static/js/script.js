// Text Form
document.getElementById('text-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const language = document.getElementById('language').value;
  const text = document.getElementById('text').value;

  const response = await fetch('/text/submit', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ language, text })
  });

  const result = await response.json();
  document.getElementById('message').innerText = result.message || result.error;

  // Clear inputs
  document.getElementById('language').value = '';
  document.getElementById('text').value = '';

  // Refresh the page (optional)
  // setTimeout(() => location.reload(), 1000);
});

// Audio Form
document.getElementById('audio-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(document.getElementById('audio-form'));
  const response = await fetch('/audio/submit', { method: 'POST', body: formData });
  const result = await response.json();
  document.getElementById('message').innerText = result.message || result.error;

  document.getElementById('audio-language').value = '';
  document.getElementById('audio').value = '';
});

// Image Form
document.getElementById('image-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(document.getElementById('image-form'));
  const response = await fetch('/image/submit', { method: 'POST', body: formData });
  const result = await response.json();
  document.getElementById('message').innerText = result.message || result.error;

  document.getElementById('image-language').value = '';
  document.getElementById('caption').value = '';
  document.getElementById('image').value = '';
});

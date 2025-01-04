const feedbackButton = document.querySelector('.feedback-button');
  const feedbackModal = document.getElementById('feedbackModal');
  const closeModal = document.getElementById('closeModal');

  feedbackButton.addEventListener('click', () => {
    feedbackModal.classList.remove('hidden');
  });

  closeModal.addEventListener('click', () => {
    feedbackModal.classList.add('hidden');
  });

  document.getElementById('sendFeedback').addEventListener('click', () => {
    const feedback = document.getElementById('feedbackInput').value;
    if (feedback.trim()) {
      alert('Thank you for your feedback: ' + feedback);
      document.getElementById('feedbackInput').value = '';
      feedbackModal.classList.add('hidden');
    } else {
      alert('Please enter your feedback before sending.');
    }
  });
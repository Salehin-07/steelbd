// Search functionality
document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.getElementById('searchInput');
  searchInput.addEventListener('input', filterMessages);

  // Update unchecked count
  updateUncheckedCount();
});

function filterMessages() {
  const searchTerm = document.getElementById('searchInput').value.toLowerCase();
  const messageCards = document.querySelectorAll('.message-card');

  messageCards.forEach(card => {
    const name = card.querySelector('.sender-info h3').textContent.toLowerCase();
    const email = card.querySelector('.sender-info .email').textContent.toLowerCase();
    const subject = card.querySelector('.message-subject h4').textContent.toLowerCase();
    const description = card.querySelector('.message-content p').textContent.toLowerCase();

    const matchesSearch = name.includes(searchTerm) ||
    email.includes(searchTerm) ||
    subject.includes(searchTerm) ||
    description.includes(searchTerm);

    if (matchesSearch) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
}

function viewFullMessage(id, name, email, subject, description) {
  const modal = document.getElementById('messageModal');
  document.getElementById('modalName').textContent = name;
  document.getElementById('modalEmail').textContent = email;
  document.getElementById('modalSubject').textContent = subject;
  document.getElementById('modalDescription').textContent = description;
  modal.style.display = 'block';
}

function markAsChecked(id) {
  // Get CSRF token
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]') ?
  document.querySelector('[name=csrfmiddlewaretoken]').value:
  getCookie('csrftoken');

  fetch(`/toggle-message-status/${id}/`,
    {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrfToken,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        'status': 'checked'
      })
    })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      // Remove the message card from the page with animation
      const messageCard = document.querySelector(`[data-id="${id}"]`);
      if (messageCard) {
        messageCard.style.transition = 'all 0.5s ease';
        messageCard.style.transform = 'translateX(100%)';
        messageCard.style.opacity = '0';

        setTimeout(() => {
          messageCard.remove();
          updateUncheckedCount();
          checkForNoMessages();
        }, 500);
      }
    } else {
      alert('Error updating message status: ' + (data.error || 'Unknown error'));
    }
  })
  .catch(error => {
    console.error('Error:', error);
    alert('Error updating message status. Please try again.');
  });
}

function updateUncheckedCount() {
  const uncheckedMessages = document.querySelectorAll('.message-card[data-status="unchecked"]');
  const visibleUnchecked = Array.from(uncheckedMessages).filter(card =>
    card.style.display !== 'none'
  );
  document.getElementById('unchecked-count').textContent = visibleUnchecked.length;
}

function checkForNoMessages() {
  const messageCards = document.querySelectorAll('.message-card');
  const messagesGrid = document.getElementById('messagesGrid');

  if (messageCards.length === 0) {
    messagesGrid.innerHTML = `
    <div class="no-messages">
    <i class="fas fa-check-circle" style="color: #4caf50;"></i>
    <h3>All Messages Checked!</h3>
    <p>Great job! You've reviewed all contact messages.</p>
    </div>
    `;
  }
}

// Function to get CSRF token from cookies
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Modal functionality
document.addEventListener('DOMContentLoaded', function() {
  const modal = document.getElementById('messageModal');
  const closeBtn = document.querySelector('.close');

  closeBtn.addEventListener('click', function() {
    modal.style.display = 'none';
  });

  window.addEventListener('click', function(event) {
    if (event.target === modal) {
      modal.style.display = 'none';
    }
  });
});
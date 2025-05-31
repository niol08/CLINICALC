function redirectToDetailPage(element) {
  const slug = element.getAttribute('data-slug');
  window.location.href = `/card/${slug}`;
}

document.addEventListener('DOMContentLoaded', function () {
  const yearSpan = document.getElementById('current-year');
  const currentYear = new Date().getFullYear();
  yearSpan.textContent = currentYear;
});

document.addEventListener('DOMContentLoaded', function () {
  const input = document.getElementById('search-input');
  const resultsDiv = document.getElementById('live-search-results');

  if (!input || !resultsDiv) return;

  input.addEventListener('input', function () {
    const query = input.value.trim();
    if (query.length === 0) {
      resultsDiv.innerHTML = '';
      return;
    }
    fetch(`/search_api?query=${encodeURIComponent(query)}`)
      .then((response) => response.json())
      .then((results) => {
        if (results.length === 0) {
          resultsDiv.innerHTML = '<p>No results found.</p>';
        } else {
          resultsDiv.innerHTML =
            '<ul>' +
            results
              .map(
                (card) =>
                  `<li>
  <a href="/search?query=${encodeURIComponent(card.name)}">${card.name}</a>
  <p>${card.description}</p>
</li>`
              )
              .join('') +
            '</ul>';
        }
      });
  });

  document.addEventListener('click', function (e) {
    if (!resultsDiv.contains(e.target) && e.target !== input) {
      resultsDiv.innerHTML = '';
    }
  });
});

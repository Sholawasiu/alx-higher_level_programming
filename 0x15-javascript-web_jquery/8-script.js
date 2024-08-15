$('document').ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (res) {
      const movies = res.results;

      for (const movie of movies) {
        $('#list_movies').append(`<li>${movie.title}</li>`);
      }
    }
  });
});

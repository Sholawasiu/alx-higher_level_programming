$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (res) {
      $('#hello').text(res.hello);
    }
  });
});

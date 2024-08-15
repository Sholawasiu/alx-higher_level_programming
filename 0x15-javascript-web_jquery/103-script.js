$(document).ready(() => {
  const URL = 'https://hellosalut.stefanbohacek.dev/';

  $('#btn_translate, #language_code').on('click keydown', (event) => {
    if (event.type === 'click' || (event.type === 'keydown' && event.key === 'Enter')) {
      const lang = $('#language_code').val();

      $.ajax({
        url: `${URL}?lang=${lang}`,
        success: (res) => {
          $('#hello').text(res.hello);
        }
      });

      $('#language_code').val('');
    }
  });
});

// $(document).ready(function () {
//   $('#btn_translate, #language_code').on('click keydown', function (event) {
//     if (event.type === 'click' || (event.type === 'keydown' && event.key === 'Enter')) {
//       const langCode = $('#language_code').val();
//       const url = `https://www.fourtonfish.com/hellosalut/?lang=${langCode}`;
//       $.get(url, function (data) {
//         $('#hello').text(data.hello);
//       });
//     }
//   });
// });

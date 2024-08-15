$(document).ready(function () {
  $('#add_item').click(() => {
    $('.my_list').append('<li>Item</li>');
  });

  $('#remove_item').click(() => {
    const items = $('.my_list li');
    console.log(items);
    items.length > 0 ? items[items.length - 1].remove() : console.log(items);
  });

  $('#clear_list').click(() => {
    $('.my_list').empty();
  });
});

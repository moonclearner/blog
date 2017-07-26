/**
 * Particleground demo
 * @author Jonathan Nicol - @mrjnicol
 */

$(document).ready(function() {
  $('#particles').particleground({
    dotColor: '#FF9999',
    lineColor: '#FF9999'
  });
  $('.intro').css({
    'margin-top': -($('.intro').height() / 2)
  });
});

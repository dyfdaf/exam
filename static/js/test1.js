$(function(){
   $('#btn').click(function(event){


var res1 = $('#1').val();
var res2 = $('#2').val();
var res3 = $('#3').val();
var res4 = $('#4').val();
var res5 = $('#5').val();

var sco = 0;
if (res1 == "1 2 3 6 6 4 5")
{sco += 20}
if (res2 == "6 5 4 3 18 360 2 20 720 1 21 720")
{sco += 20}
if (res3 == "3 3 3 5 15 8 2 30 10 4 1 6")
{sco += 20}
if (res4 == "3 3 3 1 3 4 6 2 36 12 4 144 16 5 720 21")
{sco += 20}
if (res5 == "1 1 1 6 6 7 5 30 12 2 4 18 240 3 21 720")
{sco += 20}

      $.ajax({
         url: '/testing/score_submit/',
         type: 'post',
         data: {score:sco, test:"test 1"}
              
      })
      .done(function()
      {
         alert("Ответы отправлены успешно.");
      })
      .fail(function(){
         alert("Жизнь даётся человеку только один раз.");
      })
   })
})

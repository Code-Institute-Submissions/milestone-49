for(var i=1; i<=99; i++){
    var select = document.getElementById("quantity");
    var option = document.createElement("OPTION");
    select.options.add(option);
    option.text = i;
    option.value = i;
    };

$('#fulldescription_switch').click(function(){ 
    $(this).text(function(i,old){
        return old=='Read More ...' ?  'Read Less ...' : 'Read More ...';
    });
});

$('#id_university').on('change', function() {
    console.log(this.value);

    if (this.value == 'OUTRA') {
        console.log(this.value);
        marker = $('<span />').insertBefore('#id_other');
        $('#id_other').detach().attr('type', 'text').insertAfter(marker);
        marker.remove();
        $( "#id_other" ).show();
        $( "#other_label" ).show();
        $("#id_other").prop('required',true);
    }
    else {
        $( "#id_other" ).hide();
        $( "#other_label" ).hide();
        $("#id_other").prop('required',false);
    }
})

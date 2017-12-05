// function that hides/shows field_four based upon field_three value
function check_field_value(new_val) {
    if(new_val != 'Sim') {
        // #id_field_four should be actually the id of the HTML element
        // that surrounds everything you want to hide.  Since you did
        // not post your HTML I can't finish this part for you.
        $('#field_four').removeClass('hidden');
    } else {
        $('#field_four').addClass('hidden');
    }
}
// this is executed once when the page loads
$(document).ready(function() {
    // set things up so my function will be called when field_three changes
    $('#check_empresa').change( function() {
        check_field_value(this.value);
    });
});
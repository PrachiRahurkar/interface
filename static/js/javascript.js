
(function($){ // create scope and pass specific aliased variables
    $(document).ready(function() {
    // $('#predict').prop('disabled',false);
        console.log("Out Here")

        $('.save').click(function(event) {
            console.log("Here")

            event.preventDefault();
            $('#result p').text('Submitting...')
            var form_data = new FormData($('#formId')[0]);
            $.ajax({
                type: 'POST',
                url: '/submit',
                data: form_data,
                contentType: false,
                cache: false,
                processData: false,
                success: function(data)
                {
                    console.log(data);
                    $('#result p').text('Submitted');
                    // $('#predict').prop('disabled',true);
                }
            })
        });


        $('#predict').click(function(event) {
            console.log("Here")

            event.preventDefault();
            $('#result p').text('Please wait...')
            var form_data = new FormData($('#formId')[0]);
            $.ajax({
                type: 'POST',
                url: '/predict',
                data: form_data,
                contentType: false,
                cache: false,
                processData: false,
                success: function(data)
                {
                    console.log(data);
                    $('#result p').text(data);
                    // $('#predict').prop('disabled',true);
                }
            })
        });

        
    });

})(jQuery);
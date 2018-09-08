var dhi = dhi || {};
dhi.efc = dhi.efc || {};
dhi.efc.newsletter = (function() {
    'use strict';

    var form = $('#newsletter-signup-form'),
        errValidation = $('#error-validation'),
        errSubmit = $('#error-submit'),
        confirmation = $('#signup-confirmation'),
        button = form.find('[type=submit]');

    function showError(div, shouldShow) {
        if (shouldShow) {
            div.removeClass('hidden')
        } else {
            div.addClass('hidden');
        }
    }

    function trackEvent() {
        if (!window.dataLayer) {
            console.error('GTM is not initialized.  Cannot track subscribe event');
            return;
        }
        var data = {
            'event': 'newsletter subscription',
            'action': 'Subscribed',
            'category': 'Newsletter',
            'label': 'Hippo CMS Newsletter Component',
            'pageType': form.data('dl-pagetype'),
            'contentID': form.data('dl-contentid'),
            'widgetType': 'Hippo CMS Newsletter Component'
        };
        window.dataLayer.push(data);
    }

    function disableButton(disabled) {
        button.prop('disabled', disabled);
    }

    function submitSuccess() {
        trackEvent();
        form.find('.newsletter-signup').addClass('hidden');
        confirmation.removeClass('hidden');
    }

    function submitFailure(jqXHR, textStatus, errorThrown) {
        console.error('submitFailure', jqXHR.status, jqXHR);
        console.dir && console.dir(jqXHR);
        showError(errSubmit, true);
        disableButton(false);
    }

    function isValid() {
        var regex = /^([a-zA-Z0-9_.+-])+@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        var email = $.trim(form.find('[type=email]').val());
        return regex.test(email);
    }

    function postNewsLetterSignup() {
        var opts = {
            type: form.attr('method'),
            url: form.attr('action'),
            dataType: false, // if 'json', then jQuery attempts to parse an empty response & throws error
            contentType: 'application/json; charset=utf-8',
            crossDomain: true,
            data: JSON.stringify({
                'email_address': form.find('[type=email]').val(),
                'locale': form.find('[name=locale]').val()
            })
        };
        //console.dir && console.dir(opts);
        $.ajax(opts).done(submitSuccess).fail(submitFailure);
    }

    function insertNewsLetterSignupIntoDiv(targetId, divToInsertId) {
        var targetDiv = $('#' + targetId);
        var sourceDiv = $('#' + divToInsertId);

        if (targetDiv.length && sourceDiv.length) {
            targetDiv.append(sourceDiv);
        }
    }

    function init() {
        form.on('submit', function (e) {
            e.preventDefault();
            disableButton(true);
            form.find('.newsletter-error').addClass('hidden'); // hide any error messages

            if (isValid()) {
                postNewsLetterSignup();
            } else {
                showError(errValidation, true);
                disableButton(false);
            }
        });
    }

    return {
        setupSubscribeHandler: init,
        insertNewsLetterSignupIntoDiv: insertNewsLetterSignupIntoDiv
    };
}());
